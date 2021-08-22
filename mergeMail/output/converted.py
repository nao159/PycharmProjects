characters_array = []

with open("../input/name/names.txt") as data:
    characters_array = data.readlines()

for name in characters_array:
    stripped_name = name.strip()
    with open("../input/letter/letter.txt") as letter:
        converted_letter = letter.read()
        converted_letter = converted_letter.replace("[name]", stripped_name)
        print(converted_letter)
        with open(f"./letter_for_{stripped_name}.txt", mode="w") as invitational:
            invitational.write(converted_letter)