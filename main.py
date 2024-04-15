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

def main():
    source='books/frankenstein.txt'
    text=get_text_from_file(source)
    words=word_count(text)
    print(f"{text} \nThere are {words} words in the document {source}.")
main()