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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():
    source='books/frankenstein.txt'
    text=get_text_from_file(source)
    words=word_count(text)
    count_letters=count_letter(text)
    #print(f"{text} \nThere are {words} words in the document {source}.")
    #print(f"{count_letters}")
    chars_sorted_list = chars_dict_to_sorted_list(count_letters)
    print(f"--- Begin of the report for {source} ---")
    print(f"{words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End of the report ---")
main()