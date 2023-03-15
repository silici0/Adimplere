from pydantic import BaseModel


class GameShortDescription(BaseModel):
    uuid: str
    short_description: str


class GameLongDescription(BaseModel):
    uuid: str
    long_description: str
