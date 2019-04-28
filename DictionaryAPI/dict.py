from bs4 import BeautifulSoup
import requests
import sys


class definition():
	def __init__(self, word):
		self.word = word
		self.response = requests.get('https://www.dictionary.com/browse/'+self.word) 

		if self.response.status_code != 200:
			print('Page failed to load with error code; ', str(self.response.status_code))

			sys.exit()

		else: 
			self.soup = BeautifulSoup(self.response.content, 'html.parser')


	def definition(self):		
		mydict = dict()
		count = 0

		for x in range(1,20):
			find = self.soup.find('div', {'value':str(x)})
			if find != None:
				count = count+1
				mydict.update({count: find.get_text()})
		
		return mydict


	def wordtype(self):
		find = self.soup.find('span', {'class':'luna-pos'})

		return find.get_text()


	def origin(self):
		mydict = dict()

		find = self.soup.find('div', {'class':'one-click-content css-1rstm3p e16svm7n1'}).get_text()

		year = self.soup.find('span', {'class':'luna-date'}).get_text()
		year = year.replace(';', '')

		return year, find


	def examples(self):
		text = list()
		find = self.soup.find_all('p', {'class':'one-click-content css-1o84u9 e15kc6du8'})
		for i in range(len(find)):
			text.append(find[i].get_text())

		return text