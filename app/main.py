from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books

def main():
    db = SessionLocal()
    print("=== Категории ===")
    categories = get_categories(db)
    for cat in categories:
        print(f"ID: {cat.id}, Название: {cat.title}")

    print("\n=== Книги ===")
    books = get_books(db)
    for book in books:
        print(f"ID: {book.id}, Название: {book.title}, Цена: {book.price}, Категория: {book.category.title}")

    db.close()

if __name__ == "__main__":
    main()