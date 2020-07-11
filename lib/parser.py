import csv
import json
from lib.objects import Question, Response, Responder


class Parser:

    def __init__(self):
        self.raw_csv = None
        self.responder_groups_json_file_path = "data/responder_groups.json"
        self.responder_groups = self._get_responder_groups()
        self.questions = list()
        self.responders = list()
        self.all_teachers = list()
        self.all_staff = list()
        self.overall = list()
        self.responses = list()

    def parse(self, file_path):
        self.raw_csv = self._extract_csv_rows(file_path)
        self.questions = self._get_questions()
        self.responders = self._get_responders()
        self.responses = self._get_responses()

    @staticmethod
    def _extract_csv_rows(file_path):
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

        return csv_rows

    def _get_responder_groups(self):
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
        number_of_columns = len(self.raw_csv[0])
        for question_value in self.raw_csv[0][21:number_of_columns]:
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

        for row in self.raw_csv[2:len(self.raw_csv)]:
            # grab the value in the fifth column

            raw_responder_group_name = row[4]
            # Make sure the responder provided a role
            if raw_responder_group_name == '':
                # TODO: Raise a more helpful error that provides the location of the missing data
                raise Exception("You must provide a role.")
            # compare the raw_responder_type to the mapping in the responder_groups to determine what responder type
            # this is
            responder_group_names = list()
            for json_element in self.responder_groups:
                if raw_responder_group_name in json_element["mappings"]:
                    responder_group_names.append(json_element["responder_group_name"])

            # If we didn't find a match, that is an error
            if len(responder_group_names) == 0:
                raise Exception(f"'{raw_responder_group_name}' does not map to any group names.")

            new_responder = Responder(responder_group_names)
            responders.append(new_responder)

        return responders

    @staticmethod
    def _get_responses():
        """

        :param rows:
        :return:
        """
        responses = list()

        return responses