
PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names=name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content=letter.read()
    for name in names:
        strip_name=name.strip()
        new_letter=content.replace(PLACEHOLDER,strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt",mode="w") as complete_letter:
            complete_letter.write(new_letter)
print(f"Printed {len(names)} letters for with thier data in it")