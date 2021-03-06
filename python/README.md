# Test Scripts

This directory contains a number of test scripts to verify the hardware is working.

## buttonshift
This is the python class for managing the shift register for button presses. The script __buttontest.py__ shows how to create the instance
and determine which buttons are pressed.

```
from buttonshift import *

b = buttonshift()

( button_value, button_count ) = b.poll_buttons()
```
The instance can be created using positional parameters to specify which pins on the Raspberry Pi are used. BCM numbering is expected:
* buttonPin (default=17) - This is the pin which is used to test if a button has been pressed. __GPIO.HIGH__ is yes, __GPIO.LOW__ is no.
* serialPin (default=3) - The input pin used to send data to the shift register
* latchPin (default=4) - The pin used to latch data from the shift register to the output pins
* clockPin (default=27) - The pin used to shift data one position.
* clearPin (default=22) - The pin used to clear the output pins.

__poll_buttons()__ returns a tuple of values.
* __button_value__ is an integer showing the binary value of which buttons are pressed. B:utton 1 is 1, button 2 is 2, button 3 is 4 etc. etc. Pressing buttons 2 and 3 together will give the value __6__
* __button_count__ is the highest button position that was pressed. So, if you press buttons 2, 3 and 4 together, the value will be __4__

__discover()__ returns the __button_count__ value from __poll_buttons()__ __AND__ will set the internal button count to that value.
This allows the polling to only poll the buttons that are present. See the __testshift.py__ script for how that method gets used. It only
needs to be used once before entering any loop for continued polling.

__set_num_buttons()__ allows a script to set the number of buttons available without needing to call the __discover()__ method.

__reset()__ toggles the shift register's CLEAR pin to set all output pins to low. This is useful to prevent random results from __poll_buttons()__

__selftest()__ puts the class into a permanent loop polling the buttons and printing the result when the result differs from the previous one.

## ledshift
This is the python class for managing the shift register responsible for LEDs. The script __ledtest.py__ shows how to create the instance
and light LEDs.

```
from ledshift import *

l = ledshift()

l.shift_byte(45)
```
The instance can be created using positional parameters to specify which pins on the Raspberry Pi are used. BCM numbering is expected:
* numLEDs (default=8) - This affects how a number is shifted through the shift register. If this value does not match the number of LEDs
available, the display will be incorrect.
* serialPin (default=18) - The input pin used to send data to the shift register
* latchPin (default=23) - The pin used to latch data from the shift register to the output pins
* clockPin (default=24) - The pin used to shift data one position.
* clearPin (default=25) - The pin used to clear the output pins.

__shift_byte( byte )__ will output the byte to the shift register pins to be displayed on the LEDs 
__reset()__ toggles the shift register's CLEAR pin to set all output pins to low. 
__selftest()__ outputs a series of random numbers to test all LEDs are working

## testshift

This combines the __buttonshift__ and __ledshift__ classes in combination. Each button press will light the corresponding LED.

## raveloxmidi
Using __config__, __miditest__ and  __config.json__ the __miditest__ script will read the __config.json__ file and assign MIDI notes to button presses. Using the __raveloxmidi__ class, the
MIDI events will be sent to a running __raveloxmidi__ daemon using the port defined by the raveloxmidi __network.local.port__ value.

__config.json__ has the following settings:

```
{
	"num_buttons":0,
	"buttons" : [
		{ "button_id":1, "name":"Kick", "type":"note", "midi_channel":6, "midi_id":36, "midi_value":127},
		{ "button_id":2, "name":"Snare", "type":"note", "midi_channel":6, "midi_id":38, "midi_value":127 },
		{ "button_id":4, "name":"Tom", "type":"note", "midi_channel":6, "midi_id":40, "midi_value":127 }
	],
	"remote_host":"localhost",
	"remote_port":5006
}
```
__num_buttons__ is the number of available buttons on the controller. If set to __0__, the __miditest.py__ script will go through the discovery process to determine the number of buttons.

__buttons__ is an array of button configurations.

* __button_id__ is the value for the button used in determining button presses. It should be a power of 2 such as 1, 2, 4, 8 etc.
* __name__ is a freeform label for the button
* __type__ denotes what type of MIDI event should occur. At present, this is ignored and should be __"note"__
* __midi_channel__ is the MIDI channel to send the event to
* __midi_id__ is the event number.
* __midi_value__ is the value for the event

__remote_host__ is the name of the host running raveloxmidi

__remote_port__ is port number that the raveloxmidi instance is listening on, this is defined by the network.local.port value in the raveloxmidi config file.
