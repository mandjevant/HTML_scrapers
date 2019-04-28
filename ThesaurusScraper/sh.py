from thesaurus import thesaurus
import pprint

ask = thesaurus('aforementioned').synonym()

pp = pprint.PrettyPrinter(indent = 1, width = 40)
pp.pprint(ask)