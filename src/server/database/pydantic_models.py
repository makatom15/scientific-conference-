from pydantic import BaseModel

class ModifyBaseModel(BaseModel):
    id: int = 0

class LoginData(BaseModel):
    password: str
    login: str

class ChangePassword(BaseModel):
    password: str

class User(ModifyBaseModel):
    position: str = ''
    login: str = ''
    password: str = ''
    power_level: int = 0