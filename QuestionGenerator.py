from Question import Question
from Answer import Answer
import os

class QuestionGenerator:
	def __init__(self, dirName = "./Content/"):
		self.__dirName = dirName

	def GetQuestionsFilenames(self):		
		onlyNames = os.listdir(self.__dirName)
		names = []
		for onlyName in onlyNames:
			names.append(os.path.join(self.__dirName, onlyName))
		return names

	def GetQuestions(self):
		filenames = self.GetQuestionsFilenames()
		questions = []
		for filename in filenames:
			question = Question(filename)
			questions.append(question)
		return questions
