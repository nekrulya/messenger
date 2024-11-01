from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict


class UserBase(BaseModel):
    username: Annotated[str, Field(..., min_length=3, max_length=20)]

    config = ConfigDict(from_attributes=True)


class UserReadRequest(UserBase):
    pass


class UserReadResponse(UserBase):
    pass


class UserCreateRequest(UserBase):
    password: Annotated[str, Field(..., min_length=3, max_length=20)]
    tg_id: Annotated[int, Field(..., gt=0)]


class UserCreateResponse(UserBase):
    pass
