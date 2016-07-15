import urllib
import time
from BeautifulSoup import *
dictionary = dict()
for pageno in range(1,6):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B/?page="+str(pageno)
    html =urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,7):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_C-D/?page="+str(pageno)
    html =urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,6):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_E-G/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,5):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_H-K/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,5):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_L-N/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,6):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_O-P/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,4):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_Q-R/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,6):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_S/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,4):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_T/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
for pageno in range(1,4):
    url = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_U-Z/?page="+str(pageno)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags1 = soup.findAll('a')
    for tag in tags1:
        dictionary[tag.text] = tag.get('href',None)
#print(dictionary)
for key in dictionary:
    if key is None or dictionary[key] is None:
        del dictionary[key]
lst1 = list()
lst2 = list()
for word in dictionary:
    lst1.append(word)
    lst2.append(dictionary[word])
word = input('Enter the word you want to find')
for words in dictionary:
    if word == words:
        url1 = dictionary[words]
        #print(url1)
        html1 = urllib.urlopen(url1).read()
        soup1 = BeautifulSoup(html1)
        meaning = soup1.findAll('span',{'class' : 'def'})
        for mean in meaning:
            if mean.string is not None:
                print(mean.string)
        break
else:
    print("word not found")
    

