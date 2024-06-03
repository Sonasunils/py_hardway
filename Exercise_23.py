#import modules
import sys
script, input_encoding, error = sys.argv

#define funtion
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
#define function
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)

script, input_encoding, error = sys.argv
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
