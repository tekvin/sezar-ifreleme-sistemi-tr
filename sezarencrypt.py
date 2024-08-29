alphabet_lower = 'abcçdefgğhiıjklmnoöprsştuüvyz'
alphabet_upper = 'ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ'
key = -3
newMessage = ""

#Create Dict
alphabet_dict_lower = {char: idx for idx, char in enumerate(alphabet_lower)}
alphabet_dict_upper = {char: idx for idx, char in enumerate(alphabet_upper)}

message = input("Enter a message: ")

for character in message:
    if character in alphabet_lower:
        position = alphabet_dict_lower[character]
        #print(position)

        newPosition = (position + key) % 29
        #print(newPosition)

        newMessage += alphabet_lower[newPosition]

    elif character in alphabet_upper:
        position = alphabet_dict_upper[character]
        newPosition = (position + key) % 29
        newMessage += alphabet_upper[newPosition]
        

    else:
        newMessage += character


print("Encrypted message is ", newMessage)