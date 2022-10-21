import csv

search = input('Enter the writer and additional argument:')
search = search.split()

w = search[0]
y = search[1]

writer_counter = 0
year_counter = 0
years = []

with open('library.csv') as f:
    reader = csv.DictReader(f, delimiter='|', quotechar='|', fieldnames=['writer', 'book', 'year', 'subject'])
    for row in reader:
        if w in row['writer']:
            writer_counter += 1
            if y != 'First' and y != 'Last':
                if y in row['year']:
                    print('Result of search: \nbook: ', row['book'], '\nsubject: ', row['subject'])
                    year_counter += 1
            else:
                i = row.get('year')
                years.append(i)
                first = min(years)
                last = max(years)
                if first in row['year'] and y == 'First':
                    first_book_name = row.get('book')
                    first_book_subject = row.get('subject')
                elif last in row['year'] and y == 'Last':
                    last_book_name = row.get('book')
                    last_book_subject = row.get('subject')

if writer_counter == 0 or year_counter == 0 :
    print('Not found')
if y == 'First':
    print('Result of search: \nbook: ', first_book_name, '\nsubject: ', first_book_subject, '\nyear: ', first)
elif y == 'Last':
    print('Result of search: \nbook: ', row['book'], '\nsubject: ', row['subject'], '\nyear: ', last)


# Gogol 2004
#('Gogol, Nikolai Vasilevich', 'Dead Souls', '2004', 'Humorous stories,Russia,Satire,Swindlers and swindling')



