import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetice_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("input a word: ").upper()

print([phonetice_dictionary[letter] for letter in word])