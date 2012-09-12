# Copyright 2012 Matthew Lowden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This GPIO Sample code uses PIN3 and PIN6 on the Raspberry Pi GPIO header.
# With Rev1 boards PIN3 is GPIO 0, which is pulled up.
# Rev2 boards changed the pin assignment of PIN3 to GPIO 2.
# PIN6 is GND (Ground).
# Connecting PIN3 and PIN6 results in PIN3 changing from high (true) to low (false). 
	
# The schematic below identifies the pins used.
#
#         Raspberry Pi Top             __ Composite Video (yellow)
#       ______________________________|  |__
#      |                              |  |
#      |  - - 6 - - - - - - - - - - 
#      |  - 3 - - - - - - - - - - -
#      |
#  ____|
# |    |
# | SD |
# |    |
	
# More information on Raspberry Pi GPIO can be found here:
# http://elinux.org/RPi_Low-level_peripherals

# This sample code is dependent on the RPi.GPIO library available here:
# http://pypi.python.org/pypi/RPi.GPIO/

import RPi.GPIO as GPIO
from sys import stdout

from boardRevision import getBoardRevision

usedGPIOPinRev1 = 0
usedGPIOPinRev2 = 2

try:
	boardRevision = getBoardRevision()
	if (boardRevision == 1) :
		usedGPIOPin = usedGPIOPinRev1
	elif (boardRevision == 2) :
		usedGPIOPin = usedGPIOPinRev2
	else :
		raise Exception("Unsupported board revision: %s" % boardRevision)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(usedGPIOPin, GPIO.IN)
	while True:
		# Input from pin 3 (GPIO 0 / GPIO 2)
		state = GPIO.input(usedGPIOPin)
		if state == True:
			stdout.write ("\r----- Switch opened -----")
		else:
			stdout.write ("\r+++++ Switch closed +++++")
		stdout.flush ()
except KeyboardInterrupt:
	stdout.write ("\n")
except Exception:
	raise
