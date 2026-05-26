from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError  # type: ignore
from pydantic import model_validator  # type: ignore


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = False

    @model_validator(mode='after')
    def rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == "physical":
            if not self.is_verified:
                raise ValueError("Physical contact not verified")
        if self.contact_type == "telepathic":
            if self.witness_count < 3:
                raise ValueError("Thelepatic contact must have n>3 witness")
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Strong signal require a message")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    et_phone_home = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-05-25T12:00:00",
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="E.T Phone Home",
        is_verified=True
    )
    print("======================================")
    print("Valid contact report:")
    print(f"ID: {et_phone_home.contact_id}")
    print(f"Type: {et_phone_home.contact_type}")
    print(f"Location: {et_phone_home.location}")
    print(f"Signal: {et_phone_home.signal_strength}/10")
    print(f"Duration: {et_phone_home.duration_minutes} minutes")
    print(f"Witnesses {et_phone_home.witness_count}")
    print(f"Message: '{et_phone_home.message_received}'")
    try:
        et_phone_home = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-05-25T12:00:00",
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="E.T Phone Home",
            is_verified=True
        )
    except ValidationError as error:
        print("\n========================================")
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
