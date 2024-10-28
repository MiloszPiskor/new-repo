import pandas

# 1. Creating a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# our_dictionary = {}
# for (index, row) in alphabet_df.iterrows():      # Conservative method
#     our_dictionary[row.letter] = row.code

new_dictionary = {row.letter:row.code for (index,row) in alphabet_df.iterrows()}

print(new_dictionary)

# 2. Creating a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

# list_to_check = [letter for letter in word]
# output = []
# for letter in list_to_check:                  # Longer Way
#     for key, value in new_dictionary.items():
#         if key == letter:
#             output.append(value)

output = [new_dictionary[letter] for letter in word]

print(output)


