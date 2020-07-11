from lib.parser import Parser

file_path = "data/PES-Haiphong.csv"

parser = Parser()

parser.parse(file_path)

for responder_group in parser.responses_groups:
    print(responder_group.name)
    for response in responder_group.responses:
        print(f'{response.question.value}: {response.answer}')
