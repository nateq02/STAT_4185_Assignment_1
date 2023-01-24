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

encrypted_file = open("/Users/natequan/Desktop/Spring2023/STAT4185/Week 2/week2hw/encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below
print(encrypted_message)

e_list = []

for i in encrypted_message:
    e_list.append(i)

for i in range(len(e_list)):
    for key, val in cipher.items():
        if e_list[i] == val:
            e_list[i] = key

print(e_list)

#min_idx = 1
#pen_max_idx = len(e_list) - 2

#while pen_max_idx - min_idx >= 2:
    #e_list[min_idx], e_list[pen_max_idx] = e_list[pen_max_idx], e_list[min_idx]
    #min_idx += 2
    #pen_max_idx -= 2

#print(e_list)