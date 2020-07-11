from lib.parser import Parser

file_path = "data/PES-Hanoi.csv"

parser = Parser()

parser.parse(file_path)

for question in parser.questions:
    print(question)
