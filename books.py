import datetime
import pickle
from datas import*
def add_book(file_name):
    quantity = int(input("how many books do you want to add? "))
    count =1
    while count<=quantity:
        book_name = input("Enter the name of the book: ")
        author_name = input("Enter the name of the author: ")
        book_id = input("Enter the ID of the book: ")
        amount = int(input("Enter the quantity: "))

        book = {
            "name": book_name,
            "author": author_name,
            "id": book_id,
            "amount": amount,
            "borrowed_dates": []
        }
        count+=1
    books = load_data(file_name)
    books.append(book)
    save_data(file_name, books)

def remove_book(file_name):
    book_id = input("Enter the ID of the book to remove: ")
    books = load_data(file_name)
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_data(file_name, books)
            print(f"book with id {book_id} successfully removed.")
            break
    else:
        print(f"Book with ID {book_id} not found in the library.")


def borrow_book(members_file, books_file, borrowed_books_file):
    members = load_data(members_file)
    books = load_data(books_file)
    borrowed_books = load_data(borrowed_books_file)

    member_id = input("Enter the ID of the member: ")
    book_id = input("Enter the ID of the book to borrow: ")
    borrowing_date = datetime.datetime.now().strftime("%Y-%m-%d")

    for member in members:
        if member['id'] == member_id:
            for book in books:
                if book['id'] == book_id:
                    if book['amount'] - len(book['borrowed_dates']) > 0:
                        book['borrowed_dates'].append(borrowing_date)
                        borrowed_books.append(book)
                        save_data(borrowed_books_file, borrowed_books)
                        save_data(books_file, books)
                        print(f"Book with ID {book_id} has been borrowed by member with ID {member_id}.")
                        break
                    else:
                        print("Book not available for borrowing.")
                        break
            else:
                print(f"Book with ID {book_id} not found.")
            break
    else:
        print(f"Member with ID {member_id} not found.")
