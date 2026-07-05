from app.db.db import engine, SessionLocal
from app.db import models
from app.db.crud import create_category, create_book

def init_db():
    # Создаём таблицы (если их нет)
    models.Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Добавляем категории
    category_names = ["Художественная литература", "Научно-популярная"]
    categories = {}
    for name in category_names:
        cat = create_category(db, title=name)
        categories[name] = cat.id

    # Книги для первой категории
    books_data = [
        {"title": "Война и мир", "description": "Роман-эпопея", "price": 500.0, "category_id": categories["Художественная литература"]},
        {"title": "Преступление и наказание", "description": "Роман", "price": 400.0, "category_id": categories["Художественная литература"]},
        {"title": "Мастер и Маргарита", "description": "Мистический роман", "price": 450.0, "category_id": categories["Художественная литература"]},
    ]
    for book in books_data:
        create_book(db, **book)

    # Книги для второй категории
    books_data2 = [
        {"title": "Краткая история времени", "description": "Научно-популярная", "price": 600.0, "category_id": categories["Научно-популярная"]},
        {"title": "Сознание и мозг", "description": "Нейробиология", "price": 550.0, "category_id": categories["Научно-популярная"]},
    ]
    for book in books_data2:
        create_book(db, **book)

    db.close()
    print("База данных инициализирована, добавлены категории и книги.")

if __name__ == "__main__":
    init_db()