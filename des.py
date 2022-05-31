from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


# def pad(text):
#     n = len(text) % 8
#     return text + (b' ' * n)

block_size = 24
key = b'hello123'
plain_text = b'javascript is the Best Language!'

des = DES.new(key, DES.MODE_ECB)

padded_text = pad(plain_text, block_size)
encrypted_text = des.encrypt(padded_text)

print(encrypted_text)
decrypted_text = des.decrypt(encrypted_text)
print(unpad(decrypted_text, block_size))
