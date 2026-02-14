def classify_books(*genre, **books):
    genre = list(genre)
    fiction_books = {}
    non_fiction_books = {}

    for genre_type, book_name in genre:

        if genre_type == "fiction":
            fiction_books[book_name] = ""
        else:
            non_fiction_books[book_name] = ""

    for number, book in books.items():
        if book in fiction_books:
            fiction_books[book] = number
        else:
            non_fiction_books[book] = number

    fiction_books = dict(sorted(fiction_books.items(), key=lambda x: x[1]))
    non_fiction_books = dict(sorted(non_fiction_books.items(), key=lambda x: x[1], reverse=True))

    result = []
    if fiction_books:
        result.append("Fiction Books:")
        for book_name, num in fiction_books.items():
            result.append(f"~~~{num}#{book_name}")
    if non_fiction_books:
        result.append("Non-Fiction Books:")
        for book_name, num in non_fiction_books.items():
            result.append(f"***{num}#{book_name}")

    return "\n".join(result)



print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))
print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
