ciphertxt = list(map(str, input().split()))
ciphertxt = ciphertxt = [list(i) for i in ciphertxt]
ciphertxt = [[chr(((ord(j)-65+13)%26)+65) for j in i]for i in ciphertxt]
ciphertxt = [''.join(i) for i in ciphertxt]
ciphertxt = ' '.join(ciphertxt)
print(ciphertxt)