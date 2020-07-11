import csv
import json
from lib.objects import Question, Responder, ResponderGroup


class Parser:

    def __init__(self):
        self.raw_csv = None
        self.responder_groups_json_file_path = "data/response_groups.json"
        self.responder_groups_json = self._get_responder_groups_json()
        self.number_of_rows = 0
        self.number_of_columns = 0
        self.questions = list()
        self.responders = list()
        self.responses_groups = list()

        self.questions_starting_column = 20
        self.answers_starting_row = 2

    def parse(self, file_path):
        self.raw_csv = self._extract_csv_rows(file_path)
        self.questions = self._get_questions()
        self.responders = self._get_responders()
        self._build_responder_groups()
        self._get_responses()
        self._categorize_responses()

    def _extract_csv_rows(self, file_path):
        """
        Given a file path, return me a list object containing the rows in the csv
        :return: csv_rows
        """
        with open(file_path) as csv_file:
            # Open our CSV File
            csv_file_reader = csv.reader(csv_file, delimiter=',')

            # Iterate through the file and append each row to our csv_rows list
            csv_rows = list()
            for row in csv_file_reader:
                csv_rows.append(row)
        self.number_of_columns = len(csv_rows[0])
        self.number_of_rows = len(csv_rows)
        return csv_rows

    def _get_responder_groups_json(self):
        """
        Given a file path, return me a list object containing the rows in the csv
        :return: csv_rows
        """

        with open(self.responder_groups_json_file_path) as json_file:
            # Open our CSV File
            json_data = json.load(json_file)

        return json_data

    def _get_questions(self):
        """
        Get all of the unique questions
        :param rows: the rows from a csv file that we need to parse through to get the questions
        :return: a list of questions
        """
        questions_list = list()
        # Find all the unique questions that we are asking
        # We know that in the extract, the questions are listed out starting on
        # column 'V' (Column number 22) . We want to grab that column and
        # iterate until we get to a blank.

        for question_value in self.raw_csv[0][self.questions_starting_column:self.number_of_columns]:
            new_question = Question(question_value=question_value)
            questions_list.append(new_question)

        return questions_list

    def _get_responders(self):
        """
        Get all of the responders
        :param rows:
        :return:
        """
        responders = list()
        # Extract the Responder Type data from the raw file and map it to our pre-defined types

        for row in self.raw_csv[self.answers_starting_row:len(self.raw_csv)]:
            # grab the value in the fifth column

            raw_responder_group_name = row[4]
            # Make sure the responder provided a role
            if raw_responder_group_name == '':
                # TODO: Raise a more helpful error that provides the location of the missing data
                raise Exception("You must provide a role.")
            # compare the raw_responder_type to the mapping in the responder_groups_json to determine what responder
            # type this is
            responder_group_name = None
            for json_element in self.responder_groups_json:
                if raw_responder_group_name in json_element["mappings"]:
                    responder_group_name = json_element["responder_group_name"]

            # If we didn't find a match, that is an error
            if responder_group_name is None:
                raise Exception(f"'{raw_responder_group_name}' does not map to any group names.")

            new_responder = Responder(responder_group_name)
            responders.append(new_responder)

        return responders

    def _get_responses(self):
        """

        :param rows:
        :return:
        """
        responder_number = 0
        for responder in self.responders:
            question_number = 0
            current_row = self.answers_starting_row + responder_number
            for column_value in self.raw_csv[current_row][self.questions_starting_column:self.number_of_columns]:
                current_question = self.questions[question_number]
                responder.add_response(response=column_value, question=current_question)
                question_number += 1

            responder_number += 1

    def _categorize_responses(self):
        # Create the Response Groups

        for responder in self.responders:
            target_group_names = ['Overall', responder.group_name]

            # If the responder is not a parent, add it to the all_staff list
            if responder.group_name != 'Parents':
                target_group_names.append('All Staff')

            if 'Teacher' in responder.group_name:
                target_group_names.append('All Teachers')

            # Find the ResponseGroups by name, and add the responder to the group
            for responder_group in self.responses_groups:
                for target_group_name in target_group_names:
                    if target_group_name == responder_group.name:
                        for response in responder.responses:
                            responder_group.add_response(response)

    def _build_responder_groups(self):

        # Build the responder groups defined in the JSON file
        for responder_group_element in self.responder_groups_json:
            responder_group_name = responder_group_element["responder_group_name"]
            new_responder_group = ResponderGroup(responder_group_name)
            self.responses_groups.append(new_responder_group)


