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

# Determine the board revision (1 or 2) from board revision code (2 - 6),
# according to http://www.raspberrypi.org/archives/1929

boardRevision = -1

def getBoardRevision() :
	global boardRevision
	if (boardRevision == -1) :
		file = open( "/proc/cpuinfo", "r" )
		for line in file:
			if (line.startswith('Revision')) :
				boardRevisionCode = int(line.split(':')[1])
				if (boardRevisionCode == 2 or boardRevsionCode == 3) :
					boardRevision = 1
				elif (boardRevisionCode >= 4 and boardRevisionCode <= 6) :
					boardRevision = 2
		file.close()
	return boardRevision