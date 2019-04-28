from dict import definition
import pprint

ask = definition('encyclopedia').wordtype()

pp = pprint.PrettyPrinter(width=500)
pp.pprint(ask)