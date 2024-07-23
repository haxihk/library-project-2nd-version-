from datas import*
from books import*
from members import*
from searchandreports  import*
members_file = "library_members.pickle"
books_file = "library_books.pickle"
borrowed_books_file = "borrowed_books.pickle"

while True:
        print("\n1.Add a book\n2.Remove a book\n3.borrow book\n4.add member\n5.remove members with exipred accounts\n6.renew subcription\n7.search for books\n8.search for members\n9.library comprehensive report\n10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books_file)
        elif choice == '2':
            remove_book(books_file)
        elif choice == '3':
            borrow_book(members_file, books_file,borrowed_books_file)
        elif choice == '4':
            add_member(members_file)
        elif choice == '5':
            remove_expired_members(members_file)
        elif choice == '6':
            renew_subscription(members_file)
        elif choice == '7':
            query = input("Enter the search query: ")
            search_books(books_file, query)
        elif choice == '8':
            query = input("Enter the search query: ")
            search_members(members_file, query)
        elif choice == '9':
           generate_report(members_file, books_file,borrowed_books_file)
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")