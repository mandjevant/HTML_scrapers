import sys
import requests
from bs4 import BeautifulSoup


class scholar():
	def __init__(self, search):
		self.search = self.removespaces(search)
		self.searchurl = 'https://scholar.google.nl/scholar?hl=nl&as_sdt=0%2C5&q=' + self.search + '&btnG='
		self.response = requests.get(self.searchurl)

		if self.response.status_code != 200:
			print('Search; ', self.search, ' failed to load with error code; ', self.response.status_code)
		
			sys.exit()
		
		else: 
			self.soup = BeautifulSoup(self.response.content, 'html.parser')


	def searcher(self):
		sortfind = self.soup.find_all('div', {'class':'gs_r gs_or gs_scl'})

		for x in sortfind:
			sfind = x.find('div', {'class':'gs_ggs gs_fl'})
			if sfind != None:
				linkplacefind = sfind.find('div', {'class':'gs_or_ggsm'})
				linkfind = linkplacefind.find('a')
			else:
				linkplacefind = x.find('h3', {'class':'gs_rt'})
				linkfind = linkplacefind.find('a')

			find = x.find('div', {'class':'gs_ri'})
			f = find.find('h3', {'class':'gs_rt'})
			title = f.get_text()
			
			print("")
			print(title)
			print(linkfind['href'])


	def removespaces(self, srch):
		if str.find(srch, r' ') > -1:
			y = srch.replace(r' ', '+')
		else:
			y = srch

		return y


