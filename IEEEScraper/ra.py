import os
import sys
import requests
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ieee:
	def __init__(self, word, searches=5):
		self.word = word
		self.searches = searches
		self.searchbase = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText='
		self.searchurl = self.searchbase + urllib.parse.quote(self.word)
		self.abstractbase = 'https://ieeexplore.ieee.org'
		self.response = requests.get(self.searchurl)

		if self.response.status_code != 200:
			print('Page failed to load with error code; ', str(self.response.status_code))

			sys.exit()


	def research(self):
		articles = list()

		for f in self.ieeesearch(self.searchurl):
			articles.append(self.abstractbase + f['href'])

		if len(articles) == 0:
			print('Unable to find results for', self.word, '. Please try a different search.')

			sys.exit()

		for x in range(self.searches):
			if articles[x] == None:
				print('Only ', x-1, ' articles found.')
				sys.exit()

			NEWURL = articles[x]

			abstract, title = self.ieeeabstract(NEWURL)

			if abstract == None: 
				print('No abstract found for page; ', NEWURL)

			else: 
				print('')
				print(NEWURL)
				print('')
				print('Abstract; ', title)
				print('----------')
				print(abstract[0])
				print('----------')

		sys.exit()


	def ieeesearch(self, url):
		html = self.fetchHtmlForThePage(url, 8, 'ng-SearchResults')
		soup = BeautifulSoup(html, features='html.parser')
		find = soup.find_all('a', {'class':'icon-html'})

		return find


	def fetchHtmlForThePage(self, url, delay, block_name):
		chrome_options = Options()
		chrome_options.add_argument("--headless")

		capabilities = DesiredCapabilities.CHROME.copy()
		capabilities['acceptSslCerts'] = True 
		capabilities['acceptInsecureCerts'] = True

		browser = webdriver.Chrome(os.path.dirname(os.path.realpath(__file__)) + r'/Applications/chromedriver.exe', chrome_options=chrome_options, desired_capabilities=capabilities)
		browser.minimize_window()
		browser.get(url)

		try: 
			element_present = EC.presence_of_element_located((By.ID, block_name))
			WebDriverWait(browser, delay).until(element_present)
		except:
			print("")

		html = browser.page_source
		browser.quit()

		return html


	def ieeeabstract(self, url):
		html = self.fetchHtmlForThePage(url, 3, 'ng-SearchResults')
		soup = BeautifulSoup(html, features='html.parser')
		find = soup.find_all('div', {'class':'abstract-text row'})

		x = self.abstractfind1(find)

		mylist = list()
		for y in x:
			for r in y:
				i = r.find_all('div', {'_ngcontent-c9':""})
				for m in i:
					if m.get_text() != None:
						mylist.append(m.get_text())

		titlefind = soup.find('h1', {'class':"document-title"})
		
		return mylist, titlefind.get_text()


	def abstractfind1(self, find):
		x = list()
		for f in find:
			x.append(f.find_all('div', {'class':'u-mb-1'}))

		return x