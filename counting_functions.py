from nltk import sent_tokenize, word_tokenize
import pandas as pd
import re

def get_context(text,word):
  sentences = sent_tokenize(text)
  context = [s for s in sentences if word.lower() in s.lower()]
  if len(context)>0:
    return context

def count_instance(text,word):
  count = re.findall(word.lower(),text.lower())
  return len(count)
  
