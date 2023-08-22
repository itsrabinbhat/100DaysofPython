# Reading invited names
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

# Reading the sample letter
with open('./Input/Letters/starting_letter.txt') as file:
    letter = file.read()

for name in names:
    x = name.replace('\n', "")
    with open(f'./Output/ReadyToSend/letter_to_{x}.txt', 'w') as f:
        new_letter = letter.replace('[name]', x)
        f.write(new_letter)
