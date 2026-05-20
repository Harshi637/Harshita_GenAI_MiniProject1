def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Book '{title}' added successfully.")

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book ID {book_id} borrowed successfully.")
        else:
            print(f"Book ID {book_id} is already borrowed.")
    else:
        print(f"Book ID {book_id} does not exist.")

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")

def register_member(members, member_id):
    members.add(member_id)  
    print(f"Member ID {member_id} registered.")

def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")


catalog = {}         
borrowed_books = [] 
members = set()      

add_book(catalog, 101, "Python Basics", "John Smith", 2020)
add_book(catalog, 102, "Data Structures", "Alice Brown", 2019)
add_book(catalog, 103, "Machine Learning", "Andrew Ng", 2021)
add_book(catalog, 104, "Artificial Intelligence", "Stuart Russell", 2018)

register_member(members, 1)
register_member(members, 2)
register_member(members, 3)
register_member(members, 2)   

print("\nRegistered Members:", members)
borrow_book(catalog, borrowed_books, 101)
borrow_book(catalog, borrowed_books, 103)
print("\nBorrowed Books:", borrowed_books)
return_book(borrowed_books, 101)

print("\nBorrowed Books After Return:", borrowed_books)
show_available(catalog, borrowed_books)
