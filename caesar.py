#this program takes in a string and moves each letter over by a specified amount given as an argument. any other characters and spaces stay the same
#The Caesar cipher is a type of substitution cipher where the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.
#Program written by Antonio Monje

#check the above function
def encrypt(cipher,shiftA):
    result = ""

    # traverse text
    for i in range(len(cipher)):
        char = cipher[i]
        #if its a space leave it as a space
        if (char == " " or not char.isalpha()) :
            result += chr((ord(char)))
        # encrypt uppercase characters
        elif (char.isupper()):
            result += chr((ord(char) + shiftA-65) % 26 + 65)
        # encrypt lowercase characters
        else:
            result += chr((ord(char) + shiftA-97) % 26 + 97)

    return result
def main():
    while True:
        #Get the string you want to encrypt or decrypt
        shiftA = 800
        cipher = raw_input("enter the ceaser cipher you want to encrypt or decrypt: ")
        print("If you encrypt you shift to the right decrypt shift to the left")
        while(shiftA > 26 or shiftA < -26):
            shiftA = input("How many numbers do you want to shift each character? ")
            if(shiftA > 26 or shiftA < -26):
                print("Please enter a number between -26 and 26")

        print "Shift : " + str(shiftA)
        if(shiftA < 0):
            #this part actually still shifts to the right. But we want it to look like its decrypting to the left
            print "Shift to the left by: " + str(shiftA)
            shiftA = shiftA * -1
            shiftA = 26 - shiftA
            print "Cipher decrpted: " + encrypt(cipher,shiftA)
        else:
            print "Shift to the right by: " + str(shiftA)
            print "Cipher encrpted: " + encrypt(cipher,shiftA)
if __name__ == '__main__':
    main()
