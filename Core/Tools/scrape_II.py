#!/usr/bin/python3.6

from time import sleep as sleep_for_seconds


def grab_gloss(soup):
    gloss = soup.select()


def grab_examples(soup):
    pass


def one_to_infinity(start=1):
    i = start
    while True:
        yield i
        i += 1


letters = ['a','aa','b','ch','d','e','g','h',"'",'i',
    'ii','j','k','m','n','o','oo','p','s','sh','t','w','y','z','zh']

for letter in letters:
    for page in to_infinity():
        url = f"https://ojibwe.lib.umn.edu/browse/ojibwe/{letter}?page={str(page)}"
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'html5lib')
 
        # Means we've run out of pages for that letter.
        if soup.select("a[href*=main-entry]") == []:
            break
        else:

