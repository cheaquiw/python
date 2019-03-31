from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
import csv


#extracts substantial words as a list from a webpage
def parse(site):
    try:
        url = requests.get(str(site)).text
        soup = BeautifulSoup(url, features='html.parser')
        for script in soup (["script", "style"]):
            script.extract()
        soup = soup.text.split()
        remove = set(stopwords.words('english'))
        [soup.remove(word) for word in soup if word in remove]
        soup = [word.lower() for word in soup]
        print(len(soup))
        return soup
    except:
        return

'''extracts substantial, English words as a list from all pages
from a website including any other urls listed on the website'''

def parsetxt(files):
    file  = open(files, "r")
    file = file.read()

    words = file.split()

    remove = set(stopwords.words('english'))
    [words.remove(word) for word in words if word in remove]

    words = [word.lower() for word in words]

    englishDictionary = parse('http://www-personal.umich.edu/~jlawler/wordlist')
    t = []
    [t.append(word) for word in words if word in englishDictionary]

    print(len(t))
    return t

f = 'C:/Users/willc/Desktop/New folder/HRC_Words.txt'
print(parsetxt(f))
entityDict = {'HRC_Words': f}

#creates dictionary for each group and saves it to a file as csv with seperate subfolder and file for each group
for k, v in entityDict.items():
        print(k)
        data = parsetxt(v)
        dictionary = {key:data.count(key) for key in data}

        print(dictionary)

        with open(k + 'wordsDict.csv', 'w', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(['Word', 'Frequency', 'DictionaryWebsite'])
            for ke, va in dictionary.items():
                thewriter.writerow([ke, va, 'https://www.merriam-webster.com/dictionary/' + ke])
