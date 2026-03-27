from microbit import *

I2C_ADDR = 0x3B # Tetrapad I2C address, configurable using jumpers on the back of the board

def pack_12bit(values):
    """
    Packs a list of 12-bit integers into a bytearray of 8-bit bytes.
    Every 2 values (24 bits) fit exactly into 3 bytes.
    """
    if len(values) % 2 != 0:
        values.append(0)
        
    result = bytearray()
    for i in range(0, len(values), 2):
        # Ensure values are strictly within 12-bit range (0-4095)
        v1 = int(max(0, min(4095, values[i])))
        v2 = int(max(0, min(4095, values[i+1])))
        
        b0 = (v1 >> 4) & 0xFF
        b1 = ((v1 & 0x0F) << 4) | ((v2 >> 8) & 0x0F)
        b2 = v2 & 0xFF
        
        result.append(b0)
        result.append(b1)
        result.append(b2)
        
    return result

def map_accel_to_cv(accel_val):
    """Maps -1024/1024 to 0/4095 (Center 0V is 2047)"""
    # Normalize to -1.0 to 1.0, then scale to the 12-bit range
    normalized = accel_val / 1024.0
    cv_val = (normalized * 2047) + 2047
    return cv_val

def map_temp_to_cv(temp_val, min_temp=15.0, max_temp=35.0):
    """
    Maps a temperature (in Celsius) to positive CV voltages.
    0V is 2047. Max positive voltage is 4095.
    """
    # 1. Clamp the temperature so it doesn't go outside our expected range
    temp_val = max(min_temp, min(max_temp, temp_val))
    
    # 2. Normalize the temperature to a 0.0 to 1.0 scale
    normalized = (temp_val - min_temp) / (max_temp - min_temp)
    
    # 3. Scale it to the positive half of the Tetrapad's 12-bit range
    # 2047 is 0V, we add up to 2048 to reach the 4095 maximum.
    cv_val = int((normalized * 2048) + 2047)
    
    # 4. Final safety clamp to ensure we never break the 12-bit packing limit
    return max(2047, min(4095, cv_val))

def main():
    i2c.init(freq=100000)
    sleep(1000)
    
    is_handler_enabled = False
    is_streaming_cv = False
    
    print("Press B: Enable Handler")
    print("Press A: Toggle CV Streaming")
    
    while True:
        # --- B button: Enable Handler (Write Only) ---
        if button_b.was_pressed():
            try:
                i2c.write(I2C_ADDR, b'\x00') # 0x00 is ENABLE_HANDLER
                is_handler_enabled = True
                print("Handler: ENABLED")
            except OSError as e:
                print("Enable Error:", e)

        # --- A button: Toggle CV Streaming ---
        if button_a.was_pressed():
            if is_handler_enabled:
                is_streaming_cv = not is_streaming_cv
                print("CV Streaming:", "ON" if is_streaming_cv else "OFF")
            else:
                print("Press B to enable handler first!")

        # --- Stream Accelerometer to Tetrapad Outputs ---
        if is_streaming_cv:
            # 1. Read the accelerometer
            x = accelerometer.get_x()
            y = accelerometer.get_y()
            z = accelerometer.get_z()
            
            # 2. Map X, Y, Z to 12-bit CV values
            cv_x = map_accel_to_cv(x)
            cv_y = map_accel_to_cv(y)
            cv_z = map_accel_to_cv(z)

            current_temp = temperature()
            
            # Map temperature to strictly positive CV
            cv_temp = map_temp_to_cv(current_temp)
            
            # Map x to outputs 1 and 2, y to outputs 3 and 4, z to outputs 5 and 6.
            # Map temperature to outputs 7 and 8.
            output_values = [cv_x, cv_x, cv_y, cv_y, cv_z, cv_z, cv_temp, cv_temp]
            
            # 4. Pack into 12 bytes
            payload = pack_12bit(output_values)
            
            # 5. Send SET_OUTPUTS command (0x04) + the 12 byte payload
            try:
                i2c.write(I2C_ADDR, bytes([0x04]) + payload)
            except OSError as e:
                # If we hit Error 19 here, it means the 13-byte total payload
                # is still tripping up the buffer.
                print("CV Write Error:", e)
                is_streaming_cv = False # Turn off streaming to prevent crash loops
                
        # Sleep to run at roughly 20Hz. Sending I2C data too fast can lock the bus.
        sleep(50)

main()