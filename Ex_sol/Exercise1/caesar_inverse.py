
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipherbet = alphabet[shift:27]+alphabet[0:shift]

plaintext = []
ciphertext = 'wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj'

for e in ciphertext:
    if e == ' ': 
        plaintext.append(' ') # Keep the spaces
    else:
        for a, c in zip(alphabet, cipherbet):
            if e == c:
                plaintext.append(a) 
                break # No need to finish the inner loop

plaintext = ''.join(plaintext) # Turn list into a string

print ciphertext 
print plaintext
            
    
    

