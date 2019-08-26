#!/usr/bin/python3.6
 
import bs4 as bs
import urllib.request
import sqlite3
 

def grab_all_words():
    ''' Goes through the Ojibwe People's Dictionary and grabs the links and names for every word '''
    words = []
    letters = ['a','aa','b','ch','d','e','g','h',"'",'i','ii','j','k','m','n','o','oo','p','s','sh','t','w','y','z','zh']
    for letter in letters:
        page = 1
        while True:
            source = urllib.request.urlopen(f"https://ojibwe.lib.umn.edu/browse/ojibwe/{letter}?page={str(page)}").read()
            soup = bs.BeautifulSoup(source, 'html5lib')
     
            if soup.select("a[href*=main-entry]") != []:
                for anchor in soup.select("a[href*=main-entry]"):
                    words.append({'title': anchor.text, 'url': anchor['href']})
                    print(f'{anchor.text}: {anchor["href"]}')
            else:
                break
            page += 1
    return words

if __name__ == '__main__':
    conn = sqlite3.connect('words.db', isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS words(title TEXT, url TEXT, has_been_used INT)")

    #words = grab_all_words()

    with open('/home/gtgt9/Desktop/worDS') as f:
        for l in f.readlines():
            title, url = l.split(': ')
            
            c.execute("INSERT INTO words VALUES (?,?,0)", (title, url))


    #for word in words:
    #    c.execute("INSERT INTO words VALUES (?,?,0)", (words.title, words.url))
    conn.close()
