import csv

book_1 = {"title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960}
book_2 = {"title": "Jane Eyre", "author": "Charlotte Brontë", "published_year": 1847}
book_3 = {"title": "1984", "author": "George Orwell", "published_year": 1949}

books = [book_1, book_2, book_3]


with open('data/write_example.csv', 'w') as file:
    writer = csv.DictWriter(file, ('title', 'author', 'published_year'))
    writer.writeheader()
    writer.writerows(books)
