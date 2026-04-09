# Micromod

## Overview

This project uses a BBC micro:bit v2 (and a KS0361 breakout board) and an Intellijel Tetrapad to add motion control to a small portable modular synthesizer. It was created as part of INFO-697 Experience Design for the Internet of Things in spring 2026 at Pratt Institute's School of Information, taught by Monica Maceli.

## Setup

- Sideload [micromod.py](./micromod.py) onto your micro:bit using the [micro:bit Python editor](https://python.microbit.org/v/3).
- Connect your micro:bit's SDI and SCL pins (19 and 20) and ground to corresponding pins on either of the Tetrapad's I<sup>2</sup>C connectors (see [documentation](./documentation/Tetrapad%20I2C%20Specs%20-%20Eurorack%20-%20Intellijel%20Forum.pdf)).
- Turn on power to the Tetrapad first, then the micro:bit.
- Click the micro:bit's B button to enable I<sup>2</sup>C handler mode. The Tetrapad should stop responding to touch input.
- Click the micro:bit's A button to begin streaming micro:bit sensor data over I<sup>2</sup>C. Connect patch cables from the Tetrapad to other modules and shake to your heart's content.

## Background & Methodology

This project adds motion control to a modular setup by connecting a [BBC micro:bit v2](https://microbit.org/get-started/what-is-the-microbit/) to an [Intellijel Tetrapad](https://intellijel.com/shop/eurorack/tetrapad/) using the Inter-Integrated Circuit (I<sup>2</sup>C) protocol.

The micro:bit's accelerometer outputs 3 values (`x`, `y`, and `z`) within the range [-1024, 1024]. This script maps those values onto the range [0, 4095], packs that array into a bytearray, and sends those bytes to the Tetrapad's first six CV outputs using the [`microbit.i2c`](https://microbit-micropython.readthedocs.io/en/latest/i2c.html) MicroPython module. The Tetrapad translates the I<sup>2</sup>C message into a CV signal between -8 V and +8 V.

The last two CV outputs are based on the micro:bit's temperature sensor to have a slower-moving signal for longer format performance.

I developed this code in the [micro:bit Python Editor](https://python.microbit.org/v/3) and flashed [`micromod.hex`](./micromod.hex) directly to the micro:bit from Chrome over WebUSB.

## Roadmap

- Add code sample for trigger signals (either high or low rather than continuous)
