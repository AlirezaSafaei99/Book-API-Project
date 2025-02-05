from fastapi import FastAPI
from routes.author_routes import router as author_router
from routes.book_routes import router as book_router
from routes.user_routes import router as user_router
from routes.address_routes import router as address_router
import uvicorn

app = FastAPI(title="Book API", version="1.0", description="Online Book Store API")

app.include_router(author_router)
app.include_router(book_router)
app.include_router(user_router)
app.include_router(address_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Book API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
