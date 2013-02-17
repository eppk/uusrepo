import sys, random

def encrypt(pfile, kfile, cfile):
	# read pfile content to byte string variable plain_str
	plain_str = open(pfile).read()
	# calculating length of plain_str
	plain_str_len = len(plain_str)
	# checking length of byte string, if more than 0 then continue with function and
	# converting plain text to integer
	if plain_str_len > 0:
		plain_int = ord(plain_str[0])
	# loop
		for counter in range( 1, plain_str_len):
			plain_int = plain_int << 8
			plain_int = plain_int | ord(plain_str[counter])
	# end of loop
	# now content of plain_str is converted to integer variable plain_int
	# length of key_int in bits is 8 times (length of byte) byte
		key_int = random.getrandbits(plain_str_len * 8)
	# XOR plain_int and key_int
		cipher_int = plain_int ^ key_int
	# converting key_int to byte string
	# getting first character
	# logical AND between key_int and 255 (binary as 11111111) gives lowest byte of key_int, 
	# because higher bits of 255 are zeros
		key_str = chr(key_int & 255)
		for counter in range( 1, plain_str_len):
	# shifting second byte to the place of first byte
			key_int = key_int >> 8
	# getting next character
			key_str = chr(key_int & 255) + key_str
	# saving key to file as byte text
		open(kfile, 'w').write(key_str)
	# converting cipher_int to byte string
		cipher_str = chr(cipher_int & 255)
		for counter in range( 1, plain_str_len):
			cipher_int = cipher_int >> 8
			cipher_str = chr(cipher_int & 255) + cipher_str
	# saving cipher to file as byte text
		open(cfile, 'w').write(cipher_str)
pass

def decrypt(cfile, kfile, pfile):
	# read cfile content to byte string variable cipher_str
	cipher_str = open(cfile).read()
	cipher_str_len = len(cipher_str)
	if cipher_str_len > 0:
		cipher_int = ord(cipher_str[0])
		for counter in range( 1, cipher_str_len):
			cipher_int = cipher_int << 8
			cipher_int = cipher_int | ord(cipher_str[counter])
	# read kfile content to byte string variable key_str
	key_str = open(kfile).read()
	key_str_len = len(key_str)
	if key_str_len > 0:
		key_int = ord(key_str[0])
		for counter in range( 1, key_str_len):
			key_int = key_int << 8
			key_int = key_int | ord(key_str[counter])
	plain_int = cipher_int ^ key_int
	plain_str = chr(plain_int & 255)
	for counter in range( 1, key_str_len):
		plain_int = plain_int >> 8
		plain_str = chr(plain_int & 255) + plain_str
	open(pfile, 'w').write(plain_str)
pass

def usage():
	print "Usage:"
	print "encrypt <plaintext file> <output key file> <ciphertext output file>"
	print "decrypt <ciphertext file> <key file> <plaintext output file>"
	sys.exit(1)

if len(sys.argv) != 5:
	usage()
elif sys.argv[1] == 'encrypt':
	encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == 'decrypt':
	decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
else:
	usage()
