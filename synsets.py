#!/usr/bin/env python
# coding: utf-8

# In[1]:


#all required imports
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english')) 


# In[2]:


#defining my dictionary
my_dictionary = {"politics":"the activities concerned with governing a country or area", 
                 "justice":"quality of being morally and lawfully right", 
                 "food":"any substance that people or animals eat or drink or that plants absorb to maintain life and growth", 
                 "patience":"the ability to accept delay or trouble calmly"}


# In[3]:


#defining function
def wordnet(word):
    print("My definiton of", word, "is : ", my_dictionary[word])
    
    #tokenising my definition
    word_tokens1 = word_tokenize(my_dictionary[word]) 
    filtered_sentence1 = [] 
    
    #stop word removal for my definition
    for w in word_tokens1: 
        if w not in stop_words: 
            filtered_sentence1.append(w)
            
    list1 = set(filtered_sentence1)
    count=len(wn.synsets(word, pos = 'n'))
    
    for i in range(count):
        syn = wn.synsets(word, pos = 'n')[i]
        print(" Defintion of Sysnet", syn.name(), ":", syn.definition())
        
        #tokenising wordnet definition
        word_tokens2 = word_tokenize(syn.definition()) 
        filtered_sentence2 = [] 
        
        #stop word removal for wordnet definition
        for w in word_tokens2: 
            if w not in stop_words: 
                filtered_sentence2.append(w)
                
        #finding common words in my definition and wordnet definition
        intersection = list1.intersection(filtered_sentence2)
        common_words = list(intersection)
        print("common words are :",len(common_words))   


# In[4]:


#function calling
wordnet("politics")
wordnet("justice")
wordnet("food")
wordnet("patience")

