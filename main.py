input = "books/dracular.txt"

with open(f"{input}") as f:
    file_contents = f.read()

def main(book):
    letter_count = characters_decending(count_characters(book))
    print (f"--- Begin report for {input} ---")
    print (f"{count_words(book)} words fount in the docuemnt\n")
    for letter in letter_count:
        print (f"The {letter["character"]} character was found {letter["num"]} times")
    print ("--- End report ---")

def count_words(book):
    words = book.split()
    return(len(words))

def count_characters (book):
    letter_count = {}
    for letters in book:
        lowered_letter = letters.lower()
        if lowered_letter in letter_count:
            letter_count[lowered_letter] += 1
        else:
            letter_count[lowered_letter] = 1
    return (letter_count)

def sort_on(dict):
    return dict["num"]

def characters_decending (characters_count):
    letters_only = []
    for characters in characters_count:
        if characters.isalpha():
            letter_temp = {}
            letter_temp["character"] = characters
            letter_temp["num"] = characters_count[characters]
            letters_only.append(letter_temp)
    letters_only.sort(reverse=True, key=sort_on)
    return (letters_only)

main (file_contents)