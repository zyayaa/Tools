import sys
#By Miguel Freitas ^^
if len(sys.argv) != 2:
    print("Usage: permute.py <wordlist>")
    exit(0)
feed=sys.argv[1]
basewords = open(feed).readlines()
years = range(2000,2021)

for word in basewords:
    for year in years:
        newWord = word.strip() + str(year)
        print(newWord)
        newWord = newWord.capitalize()
        print(newWord)
