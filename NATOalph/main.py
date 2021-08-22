import pandas


nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_alpha_converted = {}
for (index, row) in nato_alphabet.iterrows():
    nato_alpha_converted[row.letter] = row.code

print(nato_alpha_converted)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
your_name = input("Enter your name: ").upper()
your_name_array = []
for letter in your_name:
    your_name_array += letter
nato_alpha_dict = {letter: nato_alpha_converted[letter] for letter in your_name_array}
print(nato_alpha_dict)
