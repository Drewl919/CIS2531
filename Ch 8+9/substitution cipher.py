import pickle
import random


def openEncryptedMessage(filename="EncryptedMessage.txt"):
    """Loads the encrypted text file and returns its contents"""
    infile = open(filename)
    contents = infile.read()
    infile.close()
    return contents


def buildCipher() -> dict:
    """Replaces each letter with a new new letter, creating a cipher"""
    newCipher = {}
    count = 97
    while count < 123:
        value = chr(random.randint(97,122))
        isChar = value in newCipher.values()
        if isChar or chr(count) == value:
            pass
        else:
            newCipher[chr(count)] = value
            count += 1
    return newCipher


def encryptMessage(text: str, cipher: dict):
    """Takes the provided string and returns a new encrypted string"""
    text = text.lower()
    newText = ""
    for character in text:
        isChar = character in cipher.keys()
        if isChar:
            newText += cipher[character]
        else:
            newText += character
    return newText


def loadCipher(fileName: str):
    """Loads a cipher from a supplied fileName and returns the new cipher"""
    cipher = pickle.load(open(fileName, "rb"))
    return cipher



def decrypt(text: str, cipher: dict):
    """Reads the supplied encrypted message and returns the decrypted message"""
    newText = ""
    for character in text:
        isChar = character in cipher.values()
        if isChar:
            for key, value in cipher.items():
                if character == value:
                    newText += key
        else:
            newText += character
    return newText


def main():
    """ Test Area
        Remove or add comments for functions to test
    """
    print("TESTING PART 1")
    #### Remove comments to test buildCypher function ####
    cipher = buildCipher()
    print(cipher)  # displays your cypher

    #### Remove comments to test encryptMessage Function ####
    message = "The Quick Brown Fox, Jumps Over the lazy Dog"
    encryptedMessage = encryptMessage(message, cipher)
    print(encryptedMessage)

    # Part 2
    print("\nTesting Part 2")
    #### Remove Comments to test decrypt function ####
    decryptedMessage = decrypt(encryptedMessage, cipher)
    print(decryptedMessage)

    #### Remove comments to test loadCypher Function ####
    new_cipher = loadCipher("cipher.dat")
    print(decrypt(openEncryptedMessage(), new_cipher))


if __name__ == '__main__':
    main()
