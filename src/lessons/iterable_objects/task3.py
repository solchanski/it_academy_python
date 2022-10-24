import csv

search = input('Enter subjects: ')
subjects_search = set(search.split(','))
search_num = input('Enter number of books: ')

s = ''
books = []

with open('library.csv') as f:
    reader = csv.DictReader(f, delimiter='|', quotechar='|', fieldnames=['writer', 'book', 'year', 'subject'])
    for d in reader:
        s = d.get('subject')
        s = str(s)
        subjects = set(s.split(','))
        match = subjects & subjects_search
        if match:
            d['match'] = len(match)
            books.append(d)
result = sorted(books, key=lambda d: d['match'], reverse=True)

if search_num == '':
    for i in result:
        print(i)
else:
    for i in result[:int(search_num)]:
        print(i)

# Gogol 2004
#('Gogol, Nikolai Vasilevich', 'Dead Souls', '2004', 'Humorous stories,Russia,Satire,Swindlers and swindling')