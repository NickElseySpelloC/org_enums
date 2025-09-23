"""org_enums: shared StrEnum enumerations for multiple projects.

Import patterns:
    from org_enums.enum_power_controller import *   # all PowerController enums
    from org_enums.enum_scheduling import *         # all scheduling enums
    from org_enums import DeviceState          # (if exported in a submodule)
"""

from .enum_power_controller import (
    AppMode,
    RunPlanMode,
    RunPlanStatus,
    RunPlanTargetHours,
    StateReasonOff,
    StateReasonOn,
    SystemState,
)
from .enum_scheduling import DayPart, SchedulePolicy

__all__ = ("AppMode",
           "DayPart",
           "RunPlanMode",
           "RunPlanStatus",
           "RunPlanTargetHours",
           "SchedulePolicy",
           "StateReasonOff",
           "StateReasonOn",
           "SystemState")
