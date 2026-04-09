# Micromod

## Overview

This project uses a [BBC micro:bit v2](https://microbit.org/get-started/what-is-the-microbit/) (with a [Keyestudio KS0361 breakout board](https://docs.keyestudio.com/projects/KS0361-KS0365/en/latest/docs/KS0361-KS0365.html)) and an [Intellijel Tetrapad](https://intellijel.com/shop/eurorack/tetrapad/) to add motion control to a small portable modular synthesizer using the I<sup>2</sup>C protocol. It was created as part of INFO-697 Experience Design for the Internet of Things in spring 2026 at Pratt Institute's School of Information, taught by Monica Maceli.

## Background & Methodology

Modular synthesizer systems offer users almost endless customizability in terms of sound creation, but are somewhat limited as to physical control schemes. This project streams data from the micro:bit’s accelerometer and temperature sensors to the Tetrapad via the Inter-Integrated Circuit (I<sup>2</sup>C) protocol, which is commonly used to facilitate communication between microcontrollers.

The micro:bit's accelerometer outputs 3 values (`x`, `y`, and `z`) within the range [-1024, 1024]. This script maps those values onto the range [0, 4095], packs that array into a bytearray, and sends those bytes to the Tetrapad's first six CV outputs using the [`microbit.i2c`](https://microbit-micropython.readthedocs.io/en/latest/i2c.html) MicroPython module. The Tetrapad translates the I<sup>2</sup>C message into a CV signal between -8 V and +8 V.

The last two CV outputs are based on the micro:bit's temperature sensor to have a slower-moving signal for longer format performance.

I developed this code in the [micro:bit Python Editor](https://python.microbit.org/v/3) and flashed [micromod.hex](./micromod.hex) directly to the micro:bit from Chrome over WebUSB.

## Setup

- Flash [micromod.hex](./micromod.hex) onto micro:bit over USB or edit [micromod.py](./micromod.py) in the [micro:bit Python editor](https://python.microbit.org/v/3) and flash it to micro:bit via WebUSB in Chrome.
- Set the SCL and SDA jumpers on the back of Tetrapad to the On position (see configuration on page 11 of the [Tetrapad + Tête manual](https://intellijel.com/downloads/manuals/tete_manual_v1.2_2021.07.01.pdf)) If they are in any other configuration you will need to adjust `I2C_ADDR` in [micromod.py](./micromod.py).
- Connect micro:bit to the breakout board, then use jumper cables to connect the breakout's SDI and SCL pins (19 and 20) and ground to the corresponding pins on any of Tetrapad's four I<sup>2</sup>C connections (see [documentation](./documentation/Tetrapad%20I2C%20Specs%20-%20Eurorack%20-%20Intellijel%20Forum.pdf)).
- Turn on power to Tetrapad first, then micro:bit.
- Click micro:bit's B button to enable Tetrapad's I<sup>2</sup>C handler mode.  Tetrapad should stop responding to input at the panel.
- Click micro:bit's A button to begin streaming sensor data to Tetrapad. Connect patch cables from Tetrapad to other modules and shake to your heart's content.

## Roadmap

- Add code sample for trigger signals (either high or low rather than continuous)
