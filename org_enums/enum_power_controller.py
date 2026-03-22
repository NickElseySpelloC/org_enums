"""Holds enumerations for the PowerController application that are also used by various downstream projects."""

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
    """Override modes for the mobile app."""
    ON = "on"
    OFF = "off"
    AUTO = "auto"


class SystemState(StrEnum):
    """Enumerate the overall system state."""
    DATE_OFF = "DateOff condition met for today"
    INPUT_OVERRIDE = "Input has overridden the mode"
    APP_OVERRIDE = "App has overridden the mode"
    AUTO = "Automatic control based on schedule or best price"
    EXTERNAL_CONTROL = "External system is controlling the output"
    UPS_OVERRIDE = "Unhealthy UPS condition has overridden the mode"


class RunPlanMode(StrEnum):
    """Mode for creating run plans."""
    BEST_PRICE = "BestPrice"
    SCHEDULE = "Schedule"


class RunPlanTargetHours(StrEnum):
    """Mode for run plan target hours."""
    NORMAL = "run for target hours"
    ALL_HOURS = "all available hours"


class RunPlanStatus(StrEnum):
    """Status of the run plan creation."""
    NOTHING = "The required_hours were zero, so the run plan is empty."
    FAILED = "Unable to create the run plan. Could not allocate all required priority hours."
    BELOW_MINIMUM = "The run plan was only partially filled, not all the priority hours were allocated"
    PARTIAL = "The run plan was only partially filled, but the priority hours were allocated."
    READY = "The run plan was filled successfully."


class StateReasonOn(StrEnum):
    """Enumerate the reasons why the Output is on."""
    APP_MODE_ON = "App has overridden the mode to on"
    INPUT_SWITCH_ON = "Device input has overridden the mode to on"
    ACTIVE_RUN_PLAN = "Run plan dictates that the output should be on"
    MIN_ON_TIME = "Minimum on time has not yet elapsed"
    MAX_OFF_TIME = "Maximum off time has elapsed"
    TEMP_PROBE_CONSTRAINT = "A temperature probe constraint requires the output to be on"
    CHARGING_STARTED = "Tesla charging has started"
    POWER_INCREASE = "Power usage has increased beyond the threshold"
    DAY_START = "A new day has started"
    UPS_UNHEALTHY = "Unhealthy UPS condition requires the output to be on"


class StateReasonOff(StrEnum):
    """Enumerate the reasons why the Output is off."""
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
    MIN_OFF_TIME = "Minimum off time has not yet elapsed"
    METER_RESET = "Meter reading has reset"
    TEMP_PROBE_CONSTRAINT = "A temperature probe constraint requires the output to be off"
    CHARGING_ENDED = "Tesla charging has finished"
    POWER_DECREASE = "Power usage has decreased below the threshold"
    UPS_UNHEALTHY = "Unhealthy UPS condition requires the output to be off"
