def word_count(text):
    try:
        words = text.split()
        count = len(words)
        return count

    except Exception as w:
        print("Couldn't count the words, because: {w}")

def main():
    try:
        frankenstein_string = "..."
        with open('books/frankenstein.txt', 'r') as f:
            frankenstein_string = f.read()
            print(frankenstein_string)

    except FileNotFoundError:
        print(f"File '{'books/frankenstein.txt'}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

    words=word_count(frankenstein_string)
    print(words)
main()