print("Enter The Text : ")
text = input()
print("Enter The key :")
key = int(input())

def Encrption(text , key ):
    cipherText = ""
    for char in text :
        if(char >= 'A' and char <= 'Z' or char >= 'a' and char <= 'z'):
            if(char.isupper()):
                cipherText += chr((ord(char) + key - 65) % 26 + 65)
            else:
                cipherText += chr((ord(char) + key - 97) % 26 + 97)
        else:
            print("This Not char ")
    return cipherText

def Degreb(text , key):
    degreptionText = ""
    for char in text:
        if (char >= 'A' and char <= 'Z' or char >= 'a' and char <= 'z'):
            if (char.isupper()):
                degreptionText += chr((ord(char) - key - 65) % 26 + 65)
            else:
                degreptionText += chr((ord(char) - key - 97) % 26 + 97)
        else:
            print("This Not char ")
    return degreptionText

cipherText = Encrption(text , key)
print("Cipher Text = " + cipherText)

degreptionText = Degreb(cipherText , key)
print("Degrebtion Text = " + degreptionText)
