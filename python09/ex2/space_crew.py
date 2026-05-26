from enum import Enum
from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError  # type: ignore
from pydantic import model_validator  # type: ignore


class Rank(str, Enum):
    CADET = "cadet"
    OFFICIER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1,  max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def safety(self) -> "SpaceMission":
        is_graded: bool = False
        ex_crew: int = 0
        total_crew: int = 0
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID should start with the letter 'M'")
        for people in self.crew:
            if people.rank == "commander" or people.rank == "captain":
                is_graded = True
        if not is_graded:
            raise ValueError("There is no graded crew, please be promoted")
        if self.duration_days > 365:
            for people in self.crew:
                total_crew += 1
                if people.years_experience >= 5:
                    ex_crew += 1
            if total_crew/2 > ex_crew:
                raise ValueError("The mission effective is to low experienced")
        for people in self.crew:
            if not people.is_active:
                raise ValueError("Someone is taking advantage of unemployment")
        return (self)


def main() -> None:
    print("Space Mission Crew Validation")
    sarah: CrewMember = CrewMember(
        member_id="C001", name="Sarah Connor", rank="commander",
        age=45, specialization="Mission Command", years_experience=15,
        is_active=True
    )
    john: CrewMember = CrewMember(
        member_id="C002", name="John Smith", rank="lieutenant",
        age=35, specialization="Navigation", years_experience=8, is_active=True
    )
    alice: CrewMember = CrewMember(
        member_id="C003", name="Alice Johnson", rank="officer",
        age=28, specialization="Engineering", years_experience=3,
        is_active=True
    )
    mission: SpaceMission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-05-25T12:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[sarah, john, alice]
    )
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for people in mission.crew:
        print(f" - {people.name} ({people.rank.value}) - "
              f"{people.specialization}")
    sarah = CrewMember(
        member_id="C001", name="Sarah Connor", rank="lieutenant",
        age=45, specialization="Mission Command", years_experience=15,
        is_active=True
    )
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-05-25T12:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[sarah, john, alice]
        )
    except ValidationError as error:
        print("\n=========================================")
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
