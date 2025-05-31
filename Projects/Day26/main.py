#NATO Alphabet
import pandas

data=pandas.read_csv("data.csv")

phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetic():
    word=input("Enter Word: ").upper()
    try:
        data_list=[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Enter alphabet Only!")
        generate_phonetic()
    else:
        print(data_list)

generate_phonetic()