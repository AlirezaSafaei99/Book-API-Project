# 📚 HelloBook API

HelloBook is a book API built with **FastAPI** and **PostgreSQL**. It allows users to manage books, authors, users, and addresses with search, sorting, and pagination features.

## 🚀 Features
- 📖 **CRUD operations** for books, authors, users, and addresses
- 🔍 **Search books** by title and author's nationality
- 🔢 **Sort books** by quantity and price
- 📑 **Pagination support** for listing users, books, and addresses efficiently
- ⚡ **Asynchronous database handling** with SQLAlchemy

## 📂 Project Structure
```
HelloBook-App/
│── db/                   # Database configuration
│── models/               # SQLAlchemy models
│── routes/               # API endpoints
│── schemas/              # Data validation with Pydantic
│── services/             # Business logic
│── scripts/              # Database seeding
│── utils/                # Utility functions
│── main.py               # FastAPI entry point
│── requirements.txt      # Dependencies
│── docker-compose.yaml   # Docker setup
│── README.md             # Documentation
```

## 🛠 Setup & Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/HelloBook.git && cd HelloBook
```

### 2️⃣ Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Start the PostgreSQL database using Docker
```bash
docker-compose up -d
```

### 4️⃣ Run the FastAPI server
```bash
uvicorn main:app --reload
```

### 5️⃣ Access API Documentation
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📝 API Endpoints
### 📚 Book Endpoints
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| `POST`  | `/books/`       | Add a new book |
| `GET`   | `/books/{id}`   | Get book details by ID |
| `PUT`   | `/books/{id}`   | Update book information |
| `DELETE`| `/books/{id}`   | Delete a book |
| `GET`   | `/books/search/` | Search books by title & nationality |
| `GET`   | `/books/sort/`   | Sort books by quantity or price |

### 🖊️ Author Endpoints
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| `POST`  | `/authors/`      | Add a new author |
| `GET`   | `/authors/{id}`  | Get author details by ID |
| `PUT`   | `/authors/{id}`  | Update author information |
| `DELETE`| `/authors/{id}`  | Delete an author |

### 👤 User Endpoints
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| `POST`  | `/users/`        | Create a new user |
| `GET`   | `/users/{id}`    | Get user details by ID |
| `PUT`   | `/users/{id}`    | Update user information |
| `DELETE`| `/users/{id}`    | Delete a user |
| `GET`   | `/users/`        | List users with pagination |

### 🏠 Address Endpoints
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| `POST`  | `/addresses/`     | Add a new address |
| `GET`   | `/addresses/{id}` | Get address details by ID |
| `PUT`   | `/addresses/{id}` | Update address information |
| `DELETE`| `/addresses/{id}` | Delete an address |

## 🔧 Next Steps & Improvements
- 🔐 Implement **JWT authentication** for user management
- 📊 Add **analytics features** for book sales tracking
- 🎨 Build a frontend interface to interact with the API
