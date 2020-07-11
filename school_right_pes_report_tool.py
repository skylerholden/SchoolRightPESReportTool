from lib.parser import Parser

file_path = "data/PES-Hanoi.csv"

parser = Parser()

parser.parse(file_path)

for question in parser.questions:
    print(question)

print('All Staff:')
for responder in parser.all_staff:
    print(responder.group_name)

print('All Teachers:')
for responder in parser.all_teachers:
    print(responder.group_name)

print('Overall:')
for responder in parser.overall:
    print(responder.group_name)
