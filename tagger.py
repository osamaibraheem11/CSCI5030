import csv
from nltk.tokenize.treebank import TreebankWordDetokenizer
#import a file, one sentence at a time
#reference a dictionary file (This will list each word/part of speech combination) for each word in the sentence
#tag each word with its POS
#create new file, one sentence at a time

#Text from 
#D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
#In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012

#	Assumptions
#	1 Corpus document is a single file with one sentence on each row.
#	2 POS dictionary reference file is available 

def getWordFromSentence(pathToUntagged,pathToDict):
	#place each word from each sentence in an array
	#pass each word to tagger
	untaggedColumn = []
	untaggedSentence = []
	untaggedWord = ''
	taggedWord = ''
	taggedSentence = []
	taggedLog = []
	POSDictFile = pathToDict
	if POSDictFile=='':
		POSDictFile='deu_2019_10K_words_pos_base.txt'
	taggedCorpusName = input('Name new corpus file: ') + '.txt'
	createFile(taggedCorpusName)
	with open (pathToUntagged, 'r', encoding="utf8") as f:
		reader = csv.reader(f, delimiter='\t')
		for idx, row in enumerate(reader):
			untaggedSentence = row[1]
			wordCount=len(untaggedSentence.split())
			taggedSentence = []
			for i in range(0, wordCount):
				word = untaggedSentence.split()[i]
				taggedWord = getWordPOS(POSDictFile, word)
				if taggedWord== '':
					taggedWord = word
				taggedSentence.append(taggedWord)

			newSentence = listToString(taggedSentence)
			oldSentence = (untaggedSentence)
			line = (str(idx+1)+'\t'+newSentence+'\t'+oldSentence+'\n')
			writeToFile(taggedCorpusName, line)
			#need to add line breaks between sentence pairs
			

def listToString(list):
	str1=' '
	return (str1.join(list))


def getWordPOS(locationPath, word):
	newWordPOS = ''
	with open (locationPath, 'r', encoding="utf8") as f:
		reader = csv.reader(f,delimiter='\t')
		for row in reader:
			if row[1]==word:
				newWordPOS = word + '||' + row[2]
	return newWordPOS


def createFile(FileName):
	#create file and write to it (line#, original sentence, tagged sentence)
	with open(FileName, 'x', encoding="utf8"):
		pass


def writeToFile(FileName, Line):
	with open(FileName, 'a', encoding='utf8') as f:
		f.write(Line)

getWordFromSentence('Corpora\\tagger_test_untagged_corpus.txt','')