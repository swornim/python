alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

def caesar(msg,direction,shift):

    msg_list = []
    alpha_num = 0
    cipher_msg = ''
    if direction == 'decode':
        shift *= -1
    for i in range(len(msg)):

        alpha_num = ord(msg[i])
        alpha_num -= 97
    
        alpha_num = (alpha_num + shift)%26
        alpha_num += 97
        alpha = chr(alpha_num)
        msg_list.append(alpha)

    for i in range(len(msg_list)):
        cipher_msg += msg_list[i]
    print(f"your {direction}d message is {cipher_msg}")

repeat = 'yes'
while repeat == 'yes':

    direction = input("type 'encode' to encrypt , type 'decode' to decrypt: \n")
    text = input("Type your msg:\n").lower()
    shift = int(input("type the shift number \n"))

    caesar(msg = text,shift = shift, direction  = direction)

    check = input("do you want to continue? yes or no? ").lower()
    if check == 'no':
        repeat = 'no'
