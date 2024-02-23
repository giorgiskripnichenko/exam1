# project book


import json
json_file_path = 'bookManager.json'

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return(f'{self.title}, {self.author}, {self.year} \n')

class BookManager:
    def __init__(self):
        pass

    def addBook(self, title, author, year):
        new_book = Book(title, author, year)
        print('\n'*2,'-----------დაემატა ახალი წიგნი-----------')
        print('ახალი წიგნი----', new_book)
        print('\n'*2,'------------------------------------')

        try:
            with open(json_file_path, 'r') as file:
                existing_data = json.load(file)
        except:
            file = open(json_file_path, "w")
            file.close()
            with open(json_file_path, 'r') as file:
                existing_data = []

        existing_data.append(new_book.__dict__)

        with open(json_file_path, 'w') as file:
            json.dump(existing_data, file)

    def showAllBooks(self):
        print('\n'*2,'-----------ყველა წიგნი-----------')
        with open("bookManager.json", mode='r', encoding='utf-8') as file:
            file_content = json.load(file)
            print(file_content)
        print('\n'*2,'-----------------------------------')

    def searchBookByTitle(self, search_title):
        with open("bookManager.json", mode='r', encoding='utf-8') as file:
            existing_data = json.load(file)
            matching_books = [book for book in existing_data if book.get('title', '').lower() == search_title.lower()]
            if matching_books:
                print('\n'*2,'-----------ძებნის შედეგი-----------')
                print(matching_books)
                print('\n'*2,'-----------------------------------')
            else:
                print('ასეთი წიგნი არაა ნაპოვნი')
    
print('\n'*10)
book_manager = BookManager()
while True:
    print('#####################################################')
    a = int(input(f'''აირჩიე ციფრი:
                  1:'წიგნის დამატება'
                  2:'ყველა წიგნის ნახვა'
                  3:'წიგნის ძებნა სათაურით',
                  0:'გამოსვლა'
                   \n'''))
    if a == 1:
        try:
            title,author,year = input("""შეიყვანეთ წიგნის მონაცემები 'title','author','year' და გამოყავით ისინი ერთმანეთისგან მძიმით   \n """).split(',')
            book_manager.addBook(title,author,year)
        except:
            print('არასწორი მონაცემების შეყვანა')

    if a == 2:
        book_manager.showAllBooks()

    if a == 3:
        try:
            searchBookByTitle = input('''შეიყვანეთ წიგნის დასახელება
                                      ''')
            book_manager.searchBookByTitle(searchBookByTitle)
        except:
            print('არასწორი მონაცემების შეყვანა')

    if a == 0:
        exit()

