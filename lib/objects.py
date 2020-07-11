

class Response:

    def __init__(self, response, question_id ):
        self.response = response
        self.question_id = question_id

class Question:

    def __init__(self, question_value):
        self.value = question_value

class Responder:

    def __init__(self, responder_group_names):
        self.group_name = responder_group_names
