import unittest

from survey import AnonymousSurvey


class SurveyTestCase(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        # question = "What language did you first learn to speak?"
        # survey1 = AnonymousSurvey(question)
        # survey1.store_response('English')
        # self.assertIn('English', survey1.answer)
        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.answer)

    def test_store_three_response(self):
        # question = "What language did you first learn to speak?"
        # survey2 = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        # for response in responses:
        #     survey2.store_response(response)
        # for respinse in responses:
        #     self.assertIn(response, survey2.answer)
        for response in self.responses:
            self.survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.answer)


unittest.main()
