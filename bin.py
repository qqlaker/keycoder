from config import keys

def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)

def make_str(out):
    revert = ''.join([chr(int(s, 2)) for s in out.split()])
    print(revert)

s = ''


for i in range(1, len(keys)+1):



#Str -> bit
string = make_bitseq(s)

#Writing bit in bin file
f = open('key.bin', 'wb')
f.write(string)
f.close()

