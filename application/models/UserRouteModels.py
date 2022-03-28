from pydantic import BaseModel

class LoginUser(BaseModel):
    useremail: str
    password: str
    
class CreateUser(BaseModel):
    user_name: str
    user_email: str
    user_password: str
    
class UserRead(BaseModel):
    user_name: str
    user_email: str
    created_at: str
    daily_calls: int
    api_key: str
    is_active: bool
    verified: bool

class UpdateUser(BaseModel):
    field: str
    value: str