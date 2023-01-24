encrypted_file = open("/Users/natequan/STAT_4185_Assignment_1/week2hw/encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

encrypted_letters = []

for i in encrypted_message:
    encrypted_letters.append(i)

#print(encrypted_letters)

beg_counter = 1
end_counter = len(encrypted_letters) - 2

while end_counter > beg_counter:
    encrypted_letters[beg_counter], encrypted_letters[end_counter] = encrypted_letters[end_counter], encrypted_letters[beg_counter]
    beg_counter += 2
    end_counter -= 2

final_mess = ''
for i in encrypted_letters:
    final_mess += i

print(final_mess)