from gensim.models import Word2Vec
from gensim.test.utils import datapath
from gensim.parsing.preprocessing import remove_stopwords
from gensim import utils
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MyCorpus(object):
    def __init__(self,path):
        self.path = path
    def __iter__(self):
        CorpusPath = DataPath(self.path)
        for line in open(CorpusPath):
            yield utils.simple_preprocess(line)

PathToFile = input("Enter the path to the corpus: ")
AllSentences = MyCorpus(PathToFile)