import xml.etree.ElementTree as ET
from Answer import Answer

class QuestionXmlParser:
	def __init__(self, filename):
		self.__tree = ET.parse(filename)
		self.__root = self.__tree.getroot()
	def GetQuestionText(self):
		texts = self.__root.findall('text')
		return texts[0].text
	def GetQuestionAnswers(self):
		answersXml = self.__root.findall('answers/answer')
		answers = []
		for answerXml in answersXml:
			text = answerXml.text
			iscorrect = answerXml.attrib.get('iscorrect') == 'true'
			answer = Answer(text, iscorrect)
			answers.append(answer)
		return answers
	def GetQuestionTheme(self):
		return self.__root.attrib.get('theme')
