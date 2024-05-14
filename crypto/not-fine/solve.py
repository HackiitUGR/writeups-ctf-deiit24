#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Extraemos la información conocida

# Leemos el fichero de sailida, que de texto tiene poco
file = open('output.text', 'rb')
ciphertext = file.read()
file.close() # Esta vez hacemos las cosas bien

# Copiamos del "código" la parte de mensaje que conocemos
msg = 'Super secret cipher text, thats nobody are gonna never read it:'

# Sabemos la longitud de la clave de cifrado
key_len = 16

def xor(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

# Podemos conseguir la clave, puesto que conocemos el texto en claro y cifrado. (Knowm Plain Text)
key = xor(msg[:16].encode(), ciphertext[:16])
print(key)


# Ahora desciframos
text = xor(ciphertext, key*6)

print(text.decode())
