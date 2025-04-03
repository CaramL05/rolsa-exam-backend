from pydantic import BaseModel

class Login(BaseModel):
    fname : str
    username : str
    email : str
    password : str

class SignUp(BaseModel):
    email : str
    password : str