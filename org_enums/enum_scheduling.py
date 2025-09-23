"""Just an example enum module for scheduling-related enums."""
from enum import StrEnum

__all__ = ["DayPart", "SchedulePolicy"]


class DayPart(StrEnum):
    MORNING = "MORNING"
    AFTERNOON = "AFTERNOON"
    EVENING = "EVENING"
    NIGHT = "NIGHT"


class SchedulePolicy(StrEnum):
    STRICT = "STRICT"
    FLEXIBLE = "FLEXIBLE"
