from pydantic import BaseModel, Field, ValidationError  # type: ignore
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200, default=None)


def main() -> None:
    print("Space Station Data Validation")
    my_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-05-25T12:00:00"
    )
    print("========================================")
    print("Valid station created:")
    print(f"Name: {my_station.station_id}")
    print(f"ID: {my_station.name}")
    print(f"Crew: {my_station.crew_size} people")
    print(f"Power: {my_station.power_level}%")
    print(f"Oxygen: {my_station.oxygen_level}%")
    if my_station.is_operational:
        print("Status: Operational")
    try:
        my_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=42,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-05-25T12:00:00"
        )
    except ValidationError as error:
        print("\n========================================")
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
