import re
import operator
from enum import Enum
from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComputeOperation(str, Enum):
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"

class ComputeData(BaseModel):
    operation_type: Union[ComputeOperation, str]
    x: int
    y: int


def getResult(data: ComputeData) -> Union[int, None]:
    o_type = re.search("add|addition|sub|subtraction|subtract|multiplication|multiply", data.operation_type.lower())
    if o_type is not None:
        o_type = o_type.group()
        ops = {
            "add": operator.add,
            "addition": operator.add,
            "subtraction": operator.sub,
            "sub": operator.sub,
            "subtract": operator.sub,
            "multiplication": operator.mul,
            "multiply": operator.mul,
        }
        if o_type is not None:
            return ops[o_type](data.x, data.y)
    return None    


@app.post("/compute/")
def compute_operation(data: ComputeData):
    if getResult(data):
        return { "slackUsername": 'ali-sani', "result": getResult(data), "operation_type": data.operation_type  }
    return HTTPException(422)


@app.get("/")
def read_profile():
    return  { "slackUsername": "ali-sani", "backend": True, "age": 27, "bio": 'I am software developer who is very passionate about enterpreneuship. I joined HNG9 for the challenge and community.' }
