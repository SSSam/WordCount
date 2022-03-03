from Stopword import removeStopwords
from Stopword import get_Word_Num
from collections import Counter
from Stopword import stopwords
import pandas as pd
import csv
import re

#Read the text file in the same directory 
with open('word.txt') as f:
    text = f.read()

#Force to all be lowercase because FISH and fish and Fish are the same
text = text.lower()
#Replace the line break with a space bar
text = text.replace('\n', ' ')

#Remove anything that isn't a word character or a space
text = re.sub("[^\w ]", "", text)
words = text.split(" ")

#Remove all the stop words in the text file
words=removeStopwords(words, stopwords)

#Show the top 10 common words in the text file
print("TOP 10 most frequent non stop words: " )
print(Counter(words).most_common(10))

''''
#Return the number of occurrences of a certain word. 
get_Word_Num(text) #search in the original text
get_Word_Num(words) #search in the edited text
''''

#Create a csv file and sort it as the database
wrd_cnt = Counter(words)
with open('Word_Stat.csv','w') as csvfile:
    fieldnames = ["weight", "word", "color", "url"]
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
    for key, value in wrd_cnt.items():
       writer.writerow([value]+ [key]) 

#Sort the List by the weight of the word (How many time it appears)
df= pd.read_csv('Word_Stat.csv')
sorted_df= df.sort_values(by=['weight'], ascending=False)
sorted_df.to_csv('Word_Stat.csv', index=False)
print("\nWord_Stat.csv file is ready to be downloaded")
print('''
Continue the visual generation at https://www.wordclouds.com/
1. Download the Word_Stat.csv file and upload it to the word clouds
2. Upload the csv at: Word_list/import_from_csv
3. Customize the image by "Shape", "Font", "Color" and more! 
4. Don't forget to save your work and... enjoy the result!!''')
