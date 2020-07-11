import csv

file_path = "/Users/skylerholden/Downloads/SoGoSurvey_PES-GIS-Hanoi_0620_224-2.csv"

with open(file_path) as csv_file:
    # Open our CSV File
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    # Iterate through the file and append each row to our csv_rows list
    csv_rows = list()
    for row in csv_file_reader:
        csv_rows.append(row)

# Find all the unique questions that we are asking
# We know that in the extract, the questions are listed out starting on
# column 'V' (Column number 22) . We want to grab that column and
# iterate until we get to a blank.
number_of_rows = len(csv_rows)
number_of_columns = len(csv_rows[0])
print(f'Number of rows: {number_of_rows}')
print(f'Number of Columns: {number_of_columns}')

questions = list()
for question in csv_rows[0][21:number_of_columns]:
    questions.append(question)

print(questions)

# Get all of the answers to the questions. We know that the answers to
# the questions are below the questions
all_responses = list()
for row in csv_rows[2:number_of_rows]:
    all_responses.append(row[21:number_of_columns])

print(all_responses[1])

question_and_answers = list()
for response in all_responses:
    question_number = 0
    for answer in response:
        new_question_and_answer = {
            "question": questions[question_number],
            "answer": answer
        }
        question_and_answers.append(new_question_and_answer)
        question_number += 1

print(question_and_answers[2])




