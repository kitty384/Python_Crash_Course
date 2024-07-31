class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.answer = []

    def show_questions(self):
        print(self.question)

    def store_response(self, new_response):
        self.answer.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.answer:
            print('-'+response)
