
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipherbet = alphabet[shift:27]+alphabet[0:shift]

plaintext = []
ciphertext = 'wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj'

for p in plaintext:
    if p == ' ': 
        ciphertext.append(' ') # Keep the spaces
    else:
        for a, c in zip(alphabet, cipherbet):
            if p == a:
                ciphertext.append(c) 
                break # No need to finish the inner loop

ciphertext = ''.join(ciphertext) # Turn list into a string

print plaintext
print ciphertext 
            
    
    

