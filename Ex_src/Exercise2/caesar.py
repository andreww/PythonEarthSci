
def encode(plaintext, shift):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherbet = alphabet[shift:27]+alphabet[0:shift]

    # Put code in here.

    ciphertext = ''.join(ciphertext) # Turn list into a string

    return ciphertext

def decode(ciphertext, shift):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherbet = alphabet[shift:27]+alphabet[0:shift]

    # Put code in here.

    plaintext = ''.join(plaintext) # Turn list into a string

    return plaintext

if __name__ == "__main__":
    import sys
    if (len(sys.argv)!=3):
        print "ERROR: Two arguments needed, mode and shift"
    else:
        mode = sys.argv[1]
        shift = int(sys.argv[2])
        for line in sys.stdin:
            if mode == 'encode':
                print encode(line, shift)
            elif mode == 'decode':
                print decode(line, shift)
            else:
                print "ERROR: mode must be encode or decode"
