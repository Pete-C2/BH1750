# BH1750


Python driver module for [BH1750 Digital 16-bit ambient light sensor](http://www.mouser.com/ds/2/348/bh1750fvi-e-186247.pdf).

Requires:
- The smbus library for I2C bus access.
- The time library
- Hardware with [BH1750 Digital 16-bit ambient light sensor](http://www.mouser.com/ds/2/348/bh1750fvi-e-186247.pdf).

## Basic Use
See the testlight.py file for example uses and refer to the datasheet for the available modes.
Continuous and one time measurements are possible; more options are included in the data sheet but not yet defined in the library module.


## Changelog

V1.0
Initial release.