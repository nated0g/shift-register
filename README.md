# shiftRegister

Python library for interacting with SN74HC164 and SN54HC164 shift registers on a Raspberry Pi.

[Datasheet](http://www.ti.com/lit/ds/symlink/sn74hc164.pdf)

### Prerequisites

This library relys on [pigpio](http://abyz.me.uk/rpi/pigpio/index.html), both `pigpiod` and the `pigpio` python module must be installed on your Pi.

On Raspbian:
```
sudo apt-get update
sudo apt-get install pigpio python-pigpio python3-pigpio
```

### Installing

`pip install shift-register`


## Usage

```
import pigpio
from shiftregister import ShiftRegister

pi = pigpio.pi()

a_pin = 19
b_pin = 26
clr_pin = 20
clk_pin = 21

sr = ShiftRegister(pi, a_pin, b_pin, clr_pin, clk_pin)

sr.update(0b10101010) # Register outputs 10101010

sr.clear() # Register outputs 00000000

sr.toggle(0) # Register outputs 00000001

sr.toggle(7) # Register outputs 10000001

sr.write(7, 0) # Register outputs 00000001

sr.write(4, 1) # Register outputs 00010001

```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

