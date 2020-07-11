from lib.parser import Parser

file_path = "data/PES-Haiphong.csv"

parser = Parser()

parser.parse(file_path)


print('Overall:')
for responder in parser.overall:
    print(responder.group_name)
    for response in responder.responses:
        print(f'{response.question.value}: {response.response}')
