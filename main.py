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
main()