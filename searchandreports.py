from books import*
from members import*
from datas import*


def search_books(file_name, query):
    books = load_data(file_name)
    results = [book for book in books if query.lower() in book['name'].lower()[:2] or query.lower() in book['name'].lower() or query.lower() in book['author'].lower() or query.lower() in book['id'].lower()]
    if results:
        print("Search Results:")
        for book in results:
            print(f"Name: {book['name']}, Author: {book['author']}, ID: {book['id']}")
    else:
        print("No matching books found.")

def search_members(file_name, query):
    members = load_data(file_name)
    results = [member for member in members if query.lower() in member['name'].lower()[:2] or query.lower() in member['name'].lower() or query.lower() in member['id'].lower()]
    if results:
        print("Search Results:")
        for member in results:
            print(f"Name: {member['name']}, ID: {member['id']}")
    else:
        print("No matching members found.")

def generate_report(members_file, books_file,borrowed_books_file):
    members = load_data(members_file)
    books = load_data(books_file)
    borrowed_books = load_data(borrowed_books_file)
    print("------ Members ------")
    for member in members:
        print(f"Name: {member['name']}, ID: {member['id']}")

    print("\n------ Borrowed Books ------")
    for book in borrowed_books:
        print(f"Book Name: {book['name']}, Author: {book['author']}, ID: {book['id']}, Borrowed Dates: {', '.join(book['borrowed_dates'])}")

    print("\n------ Available Books ------")
    for book in books:
        print(f"Book Name: {book['name']}, Author: {book['author']}, ID: {book['id']}, Available Quantity: {book['amount'] - len(book['borrowed_dates'])}")