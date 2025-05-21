import streamlit as st
import json

# File to store the book data
FILE_NAME = "library.txt"

# Load books from file
def load_library():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save books to file
def save_library():
    with open(FILE_NAME, "w") as file:
        json.dump(library, file)

# Initialize library
library = load_library()

# Streamlit UI
st.title("📚 Personal Library Manager")

# Sidebar menu
menu = st.sidebar.radio("Menu", ["Add a Book", "Remove a Book", "Search Books", "View Library", "Statistics"])

# Add a Book
if menu == "Add a Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")

    if st.button("Add Book"):
        if title and author and genre:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read_status
            }
            library.append(book)
            save_library()
            st.success(f"✅ '{title}' added successfully!")
        else:
            st.warning("⚠️ Please fill all fields!")

# Remove a Book
elif menu == "Remove a Book":
    st.subheader("❌ Remove a Book")
    titles = [book["title"] for book in library]
    selected_book = st.selectbox("Select a book to remove", titles)

    if st.button("Remove Book"):
        library = [book for book in library if book["title"] != selected_book]
        save_library()
        st.success(f"✅ '{selected_book}' removed successfully!")

# Search for Books
elif menu == "Search Books":
    st.subheader("🔍 Search Books")
    search_query = st.text_input("Enter title or author")
    
    if st.button("Search"):
        results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        
        if results:
            for book in results:
                st.write(f"📖 **{book['title']}** by *{book['author']}* ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
        else:
            st.warning("⚠️ No matching books found.")

# View Library
elif menu == "View Library":
    st.subheader("📚 Your Library")
    if not library:
        st.info("⚠️ Your library is empty.")
    else:
        for book in library:
            st.write(f"📖 **{book['title']}** by *{book['author']}* ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")

# Statistics
elif menu == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books else 0

    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books}")
    st.write(f"📈 **Percentage Read:** {percentage_read:.2f}%")
