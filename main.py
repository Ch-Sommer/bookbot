def get_text_from_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
            

    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

def word_count(string):
    try:
        words = string.split()
        count = len(words)
        return count

    except Exception as w:
        print("Couldn't count the words, because: {w}")

def count_letter(stext):
    lwc_string = stext.lower()
    letters = ["a","e","i","o","u","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    letter_dict = {}
    for letter in letters:
        letter_dict[letter] = None
    for l in letter_dict:
        count =0
        for letter in lwc_string:
            if letter == l:
                count += 1
        letter_dict[l] = count
# Only 1 loop necessary
#        chars = {}
#    for c in text:
#        lowered = c.lower()
#        if lowered in chars:
#            chars[lowered] += 1
#        else:
#            chars[lowered] = 1
#    return chars


    return letter_dict

def main():
    source='books/frankenstein.txt'
    text=get_text_from_file(source)
    words=word_count(text)
    count_letters=count_letter(text)
    print(f"{text} \nThere are {words} words in the document {source}.")
    print(f"{count_letters}")
main()