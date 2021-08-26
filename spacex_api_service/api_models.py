from pydantic import BaseModel
from typing import List, Optional


class PayloadWeight(BaseModel):
    id: str
    kg: int


class SubRocket(BaseModel):
    id: str
    payload_weights: List[PayloadWeight]


class SubCore(BaseModel):
    id: str
    reuse_count: int


class Core(BaseModel):
    core: Optional[SubCore]
    reused: Optional[bool]


class FirstStage(BaseModel):
    cores: List[Core] = []


class Rocket(BaseModel):
    id: Optional[str]
    rocket: SubRocket
    first_stage: FirstStage


class Launch(BaseModel):
    id: int
    rocket: Rocket
    launch_success: Optional[bool]
    upcoming: bool


class ApiData(BaseModel):
    launches: List[Launch]
