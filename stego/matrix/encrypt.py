#!/usr/bin/python3

import sys
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt(filein, fileout):
	key = random.randbytes(32)
	cipher = AES.new(key, AES.MODE_ECB) # AES ECB Type
	
	fi = open(filein, 'rb')
	fo = open(fileout, 'wb')

	dat = fi.read()
	# Image: 2480x1748 = 4335040 % 32 != 0 won't fit in blocks :/
	enc = cipher.encrypt(pad(dat, 32)) # <- needs pudding
	fo.write(enc)

	fi.close()
	fo.close()

def main():
	encrypt(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()