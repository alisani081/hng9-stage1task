from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_profile():
    return  { "slackUsername": "ali-sani", "backend": True, "age": 27, "bio": 'I am software developer who is very passionate about enterpreneuship. I joined HNG9 for the challenge and community.' }