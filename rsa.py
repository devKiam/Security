from Crypto.Util.number import inverse
import libnum

# two prime numbers p & q
p = 189239861511125143212536989589123569301
q = 386123125371923651191219869811293586459

# n = p * q
n = 73069886771625642807435783661014062604264768481735145873508846925735521695159

phi_n = (p - 1) * (q - 1)

# public key exponent ...... 1 < e < phi_n ......... e is co-prime of phi_n
e = 65537

# private key exponent ..... d = (k * phi_n + 1) / e
d = inverse(e, phi_n)
# print(d)

# Encryption : cypher-text, c = message(m)^e mod n
c = 28767758880940662779934612526152562406674613203406706867456395986985664083182

# Decryption : message, m = c^d mod n
decrypted = pow(c, d, n)
print(libnum.n2s(decrypted).decode('utf-8'))
