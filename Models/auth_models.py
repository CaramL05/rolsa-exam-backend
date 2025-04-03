from pydantic import BaseModel

class LoginForm(BaseModel):
    fname : str
    username : str
    email : str
    password : str

class SignUpForm(BaseModel):
    email : str
    password : str