from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_profile():
    return  { "slackUsername": "ali-sani", "backend": True, "age": 27, "bio": 'I am software developer who is very passionate about enterpreneuship. I joined HNG9 for the challenge and community.' }