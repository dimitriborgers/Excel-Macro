import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

#Get rid of stop words || POS + Lemmatizer
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

#removes doubles, stop_words, and lemmatizes the outcome
def process_content(text):
    try:
        #create three empty lists
        list1, list2, list3 = ([] for i in range(3))
        
        #Run through each sentence by tokenizing each word and making sure they are not stop words
        for w in word_tokenize(text):
            if w not in stop_words:
                list1.append(w)
        #attribute each word with the correct word type
        tagged = pos_tag(list1)
        #simply each word type
        for a, b in tagged:
            if b[0] in ('J','N','R','V','I'):
                list2.append((a,b))
        #lemmatize each word based on what word type it is and add it to the list
        for a, b in list2:
            x = lemmatizer.lemmatize(a.lower(),get_wordnet_pos(b))
            if x not in list3:
                list3.append(x)
        return list3

    #if lists are empty, throw an error
    except Exception as e:
        print(str(e))

#This function is called to make sure the lemmatizer works on the proper word type
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J') or treebank_tag.startswith('I'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

#Calculates the word count for each inputted list, as well as the jaccard score and overlap
#Returns each of these values
def compare_lists(list1, list2):
    word_count_1 = len(list1)
    word_count_2 = len(list2)
    
    jaccard_score = jaccard_sim(list1,list2)
    word_overlap = len(set(list1).intersection(set(list2)))
    
    return jaccard_score, word_count_1, word_count_2, list1, list2, word_overlap

#Calculates jaccard score of two different sets
def jaccard_sim(x,y):
    i = len(set.intersection(*[set(x),set(y)]))
    j = len(set.union(*[set(x),set(y)]))
    return i/float(j)
