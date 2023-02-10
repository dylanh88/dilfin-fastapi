from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import auth, post, user, vote
from .config import settings

# Not needed with alembic.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# request comes in and reads python in order until a path and request match is found.

@app.get("/")
async def root():
    return {"message": "Hello World"}
