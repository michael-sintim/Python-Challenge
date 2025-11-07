#Create a program that asks users for their favorite books and saves them to a text file

name = input("What is your name:")
book = 0
book_list = []

while True:
        fav_book = input(f"book count({book+1}), Name all your 5 favourite Books: ")
        book_list.append(fav_book)
        book += 1
        if book == 5:
            break
        

with open(rf"C:\Users\user\Desktop\beginner\contacts{name}_books.txt", 'w') as file:
    for i, book in enumerate(book_list,start=1):
         file.write(f"Book {i}: {book}\n")

