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
    launchesPast: List[Launch]

    def filter_launches(self, successful, planned):
        if successful is None and planned is None:
            return

        def iterator(item):
            if successful is None:
                return item.upcoming == planned
            elif planned is None:
                return item.launch_success == successful
            else:
                return item.launch_success == successful and item.upcoming == planned

        self.launchesPast = list(filter(iterator, self.launchesPast))

    def return_most_used(self, count):
        self.launchesPast.sort(
            key=lambda launch: launch.rocket.first_stage.cores[0].core.reuse_count,
            reverse=True,
        )
