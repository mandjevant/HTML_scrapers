import sys
from ra import ieee

search = input('Enter the search terms')


try:
	searches = int(input('Enter the desired number of searches: '))
except(SyntaxError, ValueError):
	print('You did not enter a valid number')
	sys.exit()


ask = ieee(str(search), searches).research()


print(ask)