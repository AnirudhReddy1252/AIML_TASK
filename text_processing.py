#!/usr/bin/env python
# coding: utf-8

# In[9]:


def remove_punc(input_text):
    punctuation_marks = ['.',',','!','?','/','(',')','[',']']
    output_text = ""
    for char in input_text:
        if char not in punctuation_marks:
            output_text += char
    return output_text


# In[11]:


remove_punc('''Hello!, "How are you?"''')


# In[15]:


def remove_stopwords(input_text):
    stop_words =[ "is", "and", "the", "a", "an", "in", "on", "they", "he", "she"]
    words = input_text.split()
    filtered_words = []
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
    output_text = ' '.join(filtered_words)
    return (output_text)


# In[17]:


remove_stopwords("my name is ram")


# In[19]:


remove_stopwords("the movie was good and it is a hit")


# In[ ]:




