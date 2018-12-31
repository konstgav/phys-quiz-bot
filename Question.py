from QuestionXmlParser import QuestionXmlParser
from Answer import Answer

class Question:
	def __init__(self, filename):
		self.__parser = QuestionXmlParser(filename)
		self.Text = self.__parser.GetQuestionText()
		self.Answers = self.__parser.GetQuestionAnswers()
		self.Theme = self.__parser.GetQuestionTheme()

