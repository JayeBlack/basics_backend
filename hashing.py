import hashlib

name = "jayeblack"
hash_obj = hashlib.sha3_256(name.encode()).hexdigest()


# print(hash_obj)
def simple_hash(text):
    summation = sum(ord(ch) for ch in text)
    return summation


print(simple_hash("j"))
print(hash("okay"))
print(hash("apple"))
print(hash("orange"))
