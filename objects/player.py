from pydantic import BaseModel


class Vector3:
    x: float
    y: float
    z: float


class Player(BaseModel):
    uuid: str
    name: str
    health: int
    position: Vector3
