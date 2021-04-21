import logic
from gensim.models import Word2Vec



def SetUpDB(language):
    try:
        logic.SQLQuery(f"ALTER TABLE {language}_corpus ADD vector DOUBLE;")
    except:
        pass

language = input("What language will you be training? ")
model = input('What is the name of the model you would like to use? ')
model = Word2Vec.load(f"models/{model}.model")

data_lists = logic.VectorData("SELECT Line_ID, Line_text FROM english_corpus;")

for lists in data_lists:
    sentence = lists[1]
    sentence = sentence.split()
    sentenceVector = 0
    for words in sentence:
        words = words.split("/",1)
        words = words[0]
        vector = model.wv[f'{words}']
        print(vector.mean())
        




SetUpDB(language)