import requests
import sys
from bs4 import BeautifulSoup


class thesaurus:
    def __init__(self, word):
        self.word = word
        self.response = requests.get("http://www.thesaurus.com/browse/" + self.word)

        if self.response.status_code != 200:
            print('Word; ', self.word, ' failed to load with error code; ', str(self.response.status_code))

            sys.exit()

        else: 
            self.soup = BeautifulSoup(self.response.content, 'html.parser')


    def synonym(self):
        prioritylist = ['css-15n8j60 etbu2a31', 'css-1hlsbfu etbu2a31', 'css-z20i5j etbu2a31']
        return self.prioritycombined(prioritylist)


    def antonym(self):
        prioritylist = ['css-18z1mto etbu2a31', 'css-1eoctnx etbu2a31', 'css-1kmlnvs etbu2a31']
        return self.prioritycombined(prioritylist)


    def spaceremove(self,x):
        if str.find(x, r'%20') > -1:
            y = x.replace(r'%20', " ")
            print()
        else:
            y = x

        return y


    def prioritycombined(self, prior):
        listerino = list()

        for x in range(len(prior)):
            mydict = dict()
            mylist = list()

            for i in self.soup.find_all('a', {'class':prior[x]}):
                mylist.append(i['href'])

            for y in mylist:
                if str.find(y, r'/browse/') > -1:
                    z = self.spaceremove(y)
                    r = z.replace(r'/browse/', '')
                    mydict.update({r:x+1})
                else:
                    mydict.update({y:x+1})

            listerino.append(mydict)

        return listerino