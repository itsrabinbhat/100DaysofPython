import pandas

# Reading csv file
df = pandas.read_csv('nato_phonetic_alphabet.csv')

# converting the data in df file to a dict format
nato_alphabets = {row.letter: row.code for (idx, row) in df.iterrows()}

# converting user input into nato code
user_input = input("Enter a word: ").strip()
print(user_input)
nato_code = [nato_alphabets[letter.upper()] for letter in user_input]

print(f'Your NATO code for {user_input.capitalize()} is:\n\t{nato_code}')
