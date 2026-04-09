# Micromod

## Overview

This project uses a BBC micro:bit v2 (and a KS0361 breakout board) and a Tetrapad to add motion control to a small portable modular synthesizer. It was created as part of INFO-697 Experience Design for the Internet of Things in spring 2026 at Pratt Institute's School of Information, taught by Monica Maceli.

## Setup

- Sideload [micromod.py](./micromod.py) onto your micro:bit using the [micro:bit Python editor](https://python.microbit.org/v/3).
- Connect your micro:bit's SDI and SCL pins (19 and 20) and ground to corresponding pins on either of the Tetrapad's i2c connectors (see [documentation](./documentation/Tetrapad%20I2C%20Specs%20-%20Eurorack%20-%20Intellijel%20Forum.pdf)).
- Turn on power to the Tetrapad first, then the micro:bit.
- Click the micro:bit's B button to enable i2c handler mode. The Tetrapad should stop responding to touch input.
- Click the micro:bit's A button to begin streaming over i2c. Shake to your heart's content.

## Usage

The script as written maps the accelerometer's x, y, and z dimensions onto two outputs each. The last two outputs reflect the temperature and restricted to positive voltage. They are intended to incorporate a bit of the surrounding environment into your performance.

## Background & Methodology

This project adds motion control to a modular setup by connecting a [BBC micro:bit v2](https://microbit.org/get-started/what-is-the-microbit/) to an [Intellijel Tetrapad](https://intellijel.com/shop/eurorack/tetrapad/) using the Inter-Integrated Circuit (I<sup>2</sup>C) protocol.

I developed this code using the [micro:bit Python Editor](https://python.microbit.org/v/3) and flashed [micromod.hex](./micromod.hex) to the micro:bit using direct connection over Chrome.

This project translates the micro:bit's accelerometer into a range of values between -8 and +8 volts.

## Roadmap

- Add code sample for trigger signals (either high or low rather than continuous)
