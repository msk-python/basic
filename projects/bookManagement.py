import os

class Books:
    def __init__(self) -> None:
        self.books_list = {}

    def add_book(self):
        book_name = input('\nEnter Book Name: ')
        book_qty = int(input('Enter Book Quantity: '))  # Converting input to integer
        self.books_list[book_name] = book_qty
        os.system('cls')

    def all_books(self):
        if self.books_list:
            print("\n#------------------------- Start Available books: ----------------------------#")
            for book, qty in self.books_list.items():
                print(f"{book}: {qty} copies")
            print("\n#------------------------- End Available books: ----------------------------#")
        else:
            print("\nNo books available.")

if __name__ == "__main__":
    my_books = Books()  
    
    while True:
        print('\n\n1. View all books')
        print('2. Add a book')
        print('3. Exit')  
        user_choice = input("Your Choice: ")
        
        if user_choice == '1':
            my_books.all_books()  
        elif user_choice == '2':
            my_books.add_book()
        elif user_choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        
