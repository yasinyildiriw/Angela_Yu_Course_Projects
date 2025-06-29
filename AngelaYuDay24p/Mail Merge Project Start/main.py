PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as final_letter:
            final_letter.write(letter.replace(PLACEHOLDER,stripped_name))
