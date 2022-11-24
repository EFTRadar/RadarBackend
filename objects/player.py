from pydantic import BaseModel
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Vector3:
    x: float
    y: float
    z: float


@dataclass(frozen=True, eq=True)
class Vector2:
    x: float
    y: float


class Player(BaseModel):
    uuid: str
    name: str
    health: int
    isAlive: bool
    position: Vector3
    rotation: Vector2
