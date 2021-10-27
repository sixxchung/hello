from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
print(user.id)

#> 123
print(repr(user.signup_ts))
#> datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
#> [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
from pydantic import BaseModel

class Model(BaseModel):
    a: int
    b: float
    c: str

print(Model(a=3.1415, b=' 2.72 ', c=123).dict())
#> {'a': 3, 'b': 2.72, 'c': '123'}

from pydantic import BaseModel

class Model(BaseModel):
    a: int
    b: float
    c: str

print(Model(a=3.1415, b=' 2.72 ', c=123).dict())
#> {'a': 3, 'b': 2.72, 'c': '123'}
m = Model(a=3.1415, b=' 2.72 ', c=123).dict()

Model()
