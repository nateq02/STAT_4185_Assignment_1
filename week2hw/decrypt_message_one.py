cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("/Users/natequan/STAT_4185_Assignment_1/week2hw/encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below

encrypted_letters = []

for i in encrypted_message:
    encrypted_letters.append(i)

#print(encrypted_letters)

for idx in range(len(encrypted_letters)):
    for key in cipher:
        if encrypted_letters[idx] == cipher[key]:
            encrypted_letters[idx] = key
            break

final_mess = ''

for i in encrypted_letters:
    final_mess += i

print(final_mess)