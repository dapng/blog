import uvicorn, models

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database import engine
from routers import blog, user, auth, redirect

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(redirect.router)
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

# uvicorn.run("main:app", host="127.0.0.1", reload=True)