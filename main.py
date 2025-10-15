from fastapi import FastApi
from starlette.middleware.cors import CORSMiddleware

app = FastApi()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)