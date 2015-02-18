#!/usr/bin/env python
#
# Copyright (C) 2012 thuxnder@dexlabs.org
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
from DexFileParser import *


if __name__ == "__main__":
	if not len(sys.argv) == 4:
		print "USAGE: %s <dexfile> <class idx> <flag as hex value>"%sys.argv[0]
		exit(1)
	filename = sys.argv[1]
	cls = int(sys.argv[2])
	flag = int(sys.argv[3],16)
	data = array.array('c', open(filename, 'rb').read() )
	dexfile = DexFile(data)
	dexfile.classdefitems[cls].setFlags(flag)
	dexfile.setSignature("ee402b187725a2955b913d058edabe704122c6e0")
	dexfile.fixChecksum()
	file(filename, 'wb').write(dexfile._data)

