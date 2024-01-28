from enum import Enum


class LogType(Enum):
    REQUEST = "request"
    ACTION = "action"
    APP = "app"
    EXTERNAL = "external"
    GLOBAL = "global"


class FilterOption(str, Enum):
    Is = "Is"
    Lower = "Lower"
    Greater = "Greater"
    Contains = "Contains"
    StartsWith = "StartsWith"
    EndsWith = "EndsWith"
    In = "In"
