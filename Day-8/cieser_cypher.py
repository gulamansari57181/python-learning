alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
    
# To make ceser function which encrypts or decrypts text based on user input

def ceaser(message,shift,choice):
     # To take message in shift each charcacter nakward by shift amount
    ceser_message=""
    if choice =="decode":
            shift *=-1   
    for letter in range(len(message)):
        # To take each character in the message and replace it with next character with shift number
        
        position=alphabet.index(message[letter])
       
        new_position =position + shift
        if new_position>=26:
            new_position=new_position - 26
        elif new_position<0:
            new_position = new_position + 26
        ceser_message +=alphabet[new_position]
     
     
    return ceser_message
    
result=ceaser(message=text,shift=shift,choice=direction)

if direction =="encode":
    print(f"Encrypted message is : {result}")
else:
     print(f"Decrypted message is : {result}")