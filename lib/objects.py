

class Response:

    def __init__(self, answer, question):
        self.answer = answer
        self.question = question


class Question:

    def __init__(self, question_value):
        self.value = question_value


class Responder:

    def __init__(self, responder_group_name):
        self.group_name = responder_group_name
        self.responses = list()

    def add_response(self, response, question):
        """

        :param response: the numeric value of the answer
        :param question: the question object
        :return:
        """
        new_response = Response(response, question)
        self.responses.append(new_response)


class ResponderGroup:

    def __init__(self, name):
        self.name = name
        self.responses = list()

    def add_response(self, response):
        self.responses.append(response)
