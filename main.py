import sys
from lexer import generate_tokens
from my_parser import parse
from interpreter import interpret , symbol_table

# interactive mode or file mode

def interpret_text(text):
    tokens = generate_tokens(text)
    tree = parse(tokens)
    if tree is not None:
        interpret(tree)
        print(symbol_table)
    else:
        print("Empty text.")


if __name__ == "__main__":
    # check for command-line arguments
    if len(sys.argv) > 1:
        # file name
        file_name = sys.argv[1]
        try:
            with open(file_name, 'r') as file:
                text = file.read()
            interpret_text(text)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
    else:
        # no file name provided, continue interactive mode
        while True:
            try:
                text = input("Interpret > ")
                if text == "exit":
                    print("Exit successfully")
                    sys.exit()

                interpret_text(text)
            except Exception as e:
                print(e)