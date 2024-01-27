from enum import Enum


class LogType(Enum):
    REQUEST = "request"
    ACTION = "action"
    APP = "app"
    EXTERNAL = "external"
    GLOBAL = "global"
