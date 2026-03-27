# Micromod

## Overview

This project uses a BBC micro:bit v2 (and a KS0361 breakout board) and a Tetrapad to add motion control to a small portable modular synthesizer. It was created as part of INFO-697 Experience Design for the Internet of Things in spring 2026 at Pratt Institute's School of Information, taught by Monica Maceli.

## Usage

The a1_micromod.py file can be sideloaded onto your micro:bit using Microsoft MakeCode. Then connect your micro:bit's SDI and SCL pins (19 and 20) and ground to the corresponding pins on the Tetrapad, then click the B button, then click the A button.

The script as written maps the accelerometer's x, y, and z dimensions onto two outputs each. The last two outputs reflect the temperature and restricted to positive voltage. They are intended to incorporate a bit of the surrounding environment into your performance.
