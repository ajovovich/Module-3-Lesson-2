#Task 1: Library System Enhancement

def add_book(genre):
    title = input("Write the book you'd like to add!")
    author = input("Who is the author of this book?")
    for book, writer in genre:
        if book == title:
            print("The book already exists!")
            return genre
    else:
        temp_library = list(genre)
        temp_library.append((title, author))
        return tuple(temp_library)


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

library = add_book(library)
print(library)
