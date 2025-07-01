import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in data.iterrows()}
word = input("Enter a word:").upper()
result = [nato[letter]for letter in word]
print(result)