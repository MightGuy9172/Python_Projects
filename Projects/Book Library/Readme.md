# Book Library

A simple web application to manage your personal book collection. Built with Flask, SQLAlchemy, Flask-WTF, and styled using Tailwind CSS.

## Features

- Add new books with title, author, and rating.
- Edit the rating of existing books.
- Delete books from the library.
- View all books in a clean, responsive interface.

## Getting Started

1. **Clone the repository** and navigate to the project folder.
2. **Create a virtual environment** and activate it:
   - `python -m venv venv`
   - On Windows: `venv\Scripts\activate`
3. **Install Python dependencies**:
   - `pip install flask flask_sqlalchemy flask_wtf wtforms`
4. **Install Node.js dependencies** (for Tailwind CSS):
   - `npm install`
5. **Build Tailwind CSS**:
   - `npx tailwindcss -i static/input.css -o static/output.css --watch`
6. **Run the application**:
   - `python main.py`
7. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

- Click "Add New Book" to add a book.
- Use "Edit Rating" to update a book's rating.
- Click "Delete" to remove a book.

## Technologies

- Flask
- Flask-WTF
- SQLAlchemy
- Tailwind CSS

## License

ISC License

## Author

Manish Maurya
