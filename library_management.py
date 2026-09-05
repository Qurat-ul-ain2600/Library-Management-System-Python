import csv
import os


class Book:
    """Represents a book in the library."""

    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_issued = False
        self.issued_to = ""

    def issue_book(self, student_name):
        if self.is_issued:
            return False
        self.is_issued = True
        self.issued_to = student_name
        return True

    def return_book(self):
        if not self.is_issued:
            return False
        self.is_issued = False
        self.issued_to = ""
        return True


class Library:
    """Manages the library system."""

    FILE_NAME = "library_books.csv"

    def __init__(self):
        self.books = []
        self.categories = set()
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    book = Book(
                        row["book_id"],
                        row["title"],
                        row["author"],
                        row["category"]
                    )
                    book.is_issued = row["is_issued"] == "True"
                    book.issued_to = row["issued_to"]

                    self.books.append(book)
                    self.categories.add(book.category)

        except (FileNotFoundError, KeyError, csv.Error) as error:
            print(f"Error loading library data: {error}")

    def save_books(self):
        try:
            with open(self.FILE_NAME, "w", newline="", encoding="utf-8") as file:
                fieldnames = [
                    "book_id", "title", "author",
                    "category", "is_issued", "issued_to"
                ]

                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for book in self.books:
                    writer.writerow({
                        "book_id": book.book_id,
                        "title": book.title,
                        "author": book.author,
                        "category": book.category,
                        "is_issued": book.is_issued,
                        "issued_to": book.issued_to
                    })

        except PermissionError:
            print("Error: Permission denied while saving data.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def get_available_books(self):
        return [book for book in self.books if not book.is_issued]

    def add_book(self):
        print("\n========== ADD NEW BOOK ==========")

        book_id = input("Enter Book ID: ").strip()

        if not book_id:
            print("Book ID cannot be empty.")
            return

        if self.find_book(book_id):
            print("A book with this ID already exists.")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()
        category = input("Enter Category: ").strip()

        if not title or not author or not category:
            print("All fields are required.")
            return

        book = Book(book_id, title, author, category)
        self.books.append(book)
        self.categories.add(category)
        self.save_books()

        print("Book added successfully!")

    def view_books(self):
        print("\n========== ALL BOOKS ==========")

        if not self.books:
            print("No books found in the library.")
            return

        print("-" * 85)
        print(
            f"{'ID':<10}{'Title':<25}{'Author':<20}"
            f"{'Category':<15}{'Status':<10}"
        )
        print("-" * 85)

        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(
                f"{book.book_id:<10}{book.title[:23]:<25}"
                f"{book.author[:18]:<20}{book.category[:13]:<15}"
                f"{status:<10}"
            )

        print("-" * 85)

    def search_book(self):
        print("\n========== SEARCH BOOK ==========")

        keyword = input(
            "Enter Book ID, title, author, or category: "
        ).strip().lower()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        results = []

        for book in self.books:
            if (
                keyword in book.book_id.lower()
                or keyword in book.title.lower()
                or keyword in book.author.lower()
                or keyword in book.category.lower()
            ):
                results.append(book)

        if not results:
            print("No matching books found.")
            return

        print(f"\nFound {len(results)} book(s):")

        for book in results:
            status = "Issued" if book.is_issued else "Available"

            print(
                f"\nBook ID   : {book.book_id}"
                f"\nTitle     : {book.title}"
                f"\nAuthor    : {book.author}"
                f"\nCategory  : {book.category}"
                f"\nStatus    : {status}"
            )

            if book.is_issued:
                print(f"Issued To : {book.issued_to}")

    def issue_book(self):
        print("\n========== ISSUE BOOK ==========")

        book_id = input("Enter Book ID: ").strip()
        book = self.find_book(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.is_issued:
            print(f"This book is already issued to {book.issued_to}.")
            return

        student_name = input("Enter student name: ").strip()

        if not student_name:
            print("Student name cannot be empty.")
            return

        if book.issue_book(student_name):
            self.save_books()
            print(f"'{book.title}' has been issued successfully.")

    def return_book(self):
        print("\n========== RETURN BOOK ==========")

        book_id = input("Enter Book ID: ").strip()
        book = self.find_book(book_id)

        if book is None:
            print("Book not found.")
            return

        if not book.is_issued:
            print("This book is not currently issued.")
            return

        previous_student = book.issued_to

        if book.return_book():
            self.save_books()
            print(
                f"Book returned successfully.\n"
                f"Previously issued to: {previous_student}"
            )

    def remove_book(self):
        print("\n========== REMOVE BOOK ==========")

        book_id = input("Enter Book ID: ").strip()
        book = self.find_book(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.is_issued:
            print("Cannot remove a book that is currently issued.")
            return

        confirmation = input(
            f"Are you sure you want to remove '{book.title}'? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            self.books.remove(book)
            self.categories = {book.category for book in self.books}
            self.save_books()
            print("Book removed successfully.")
        else:
            print("Operation cancelled.")

    def show_categories(self):
        print("\n========== BOOK CATEGORIES ==========")

        if not self.categories:
            print("No categories available.")
            return

        for number, category in enumerate(sorted(self.categories), start=1):
            print(f"{number}. {category}")

    def issued_books(self):
        print("\n========== ISSUED BOOKS ==========")

        issued = [book for book in self.books if book.is_issued]

        if not issued:
            print("No books are currently issued.")
            return

        for book in issued:
            print(
                f"\nBook ID   : {book.book_id}"
                f"\nTitle     : {book.title}"
                f"\nIssued To : {book.issued_to}"
                f"\nCategory  : {book.category}"
            )

    def statistics(self):
        print("\n========== LIBRARY STATISTICS ==========")

        total_books = len(self.books)
        available_books = len(self.get_available_books())
        issued_books = total_books - available_books
        total_categories = len(self.categories)

        print(f"Total Books       : {total_books}")
        print(f"Available Books   : {available_books}")
        print(f"Issued Books      : {issued_books}")
        print(f"Total Categories  : {total_categories}")

        if total_books > 0:
            percentage = (available_books / total_books) * 100
            print(f"Availability      : {percentage:.2f}%")


def display_menu():
    print("\n" + "=" * 55)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Remove Book")
    print("7. View Book Categories")
    print("8. View Issued Books")
    print("9. Library Statistics")
    print("10. Exit")
    print("=" * 55)


def main():
    library = Library()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-10): "))

            if choice == 1:
                library.add_book()
            elif choice == 2:
                library.view_books()
            elif choice == 3:
                library.search_book()
            elif choice == 4:
                library.issue_book()
            elif choice == 5:
                library.return_book()
            elif choice == 6:
                library.remove_book()
            elif choice == 7:
                library.show_categories()
            elif choice == 8:
                library.issued_books()
            elif choice == 9:
                library.statistics()
            elif choice == 10:
                print("\nThank you for using the Library Management System!")
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please select 1-10.")

        except ValueError:
            print("Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as error:
            print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
