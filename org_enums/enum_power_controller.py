"""Holds enumerations for the PowerController application that are also used by downstream projects."""

from enum import StrEnum

__all__ = [
    "AppMode",
    "RunPlanMode",
    "RunPlanStatus",
    "RunPlanTargetHours",
    "StateReasonOff",
    "StateReasonOn",
    "SystemState",
]


class AppMode(StrEnum):
    """Override modes for the mobile app"""
    ON = "on"
    OFF = "off"
    AUTO = "auto"


class SystemState(StrEnum):
    """Enumerate the overall system state"""
    DATE_OFF = "DateOff condition met for today"
    INPUT_OVERRIDE = "Input has overridden the mode"
    APP_OVERRIDE = "App has overridden the mode"
    AUTO = "Automatic control based on schedule or best price"


class RunPlanMode(StrEnum):
    """Mode for creating run plans"""
    BEST_PRICE = "BestPrice"
    SCHEDULE = "Schedule"


class RunPlanTargetHours(StrEnum):
    """Mode for run plan target hours"""
    NORMAL = "run for target hours"
    ALL_HOURS = "all available hours"


class RunPlanStatus(StrEnum):
    """Status of the run plan creation"""
    NOTHING = "The required_hours were zero, so the run plan is empty."
    FAILED = "Unable to create the run plan. Could not allocate all required priority hours."
    PARTIAL = "The run plan was only partially filled, but the priority hours were allocated."
    READY = "The run plan was filled successfully."


class StateReasonOn(StrEnum):
    """Enumerate the reasons why the Output is on"""
    APP_MODE_ON = "App has overridden the mode to on"
    INPUT_SWITCH_ON = "Device input has overridden the mode to on"
    ACTIVE_RUN_PLAN = "Run plan dictates that the output should be on"


class StateReasonOff(StrEnum):
    """Enumerate the reasons why the Output is off"""
    NO_RUN_PLAN = "No run plan available"
    RUN_PLAN_COMPLETE = "No more run time required today"
    INACTIVE_RUN_PLAN = "Run plan dictates that the output should be off"
    APP_MODE_OFF = "App has overridden the mode to off"
    INPUT_SWITCH_OFF = "Device input has overridden the mode to off"
    DATE_OFF = "DateOff condition met for today"
    PARENT_OFF = "Parent output is off"
    STATUS_CHANGE = "Mode remains on but the status has changed"
    DAY_END = "A new day has started"
    SHUTDOWN = "System is shutting down"
    DEVICE_OFFLINE = "Device is offline"
