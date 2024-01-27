import logging
import json
from math import e
import sys


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "name": record.name,
            "level": record.levelname,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


# 로거 생성
logger = logging.getLogger("json_logger")
logger.setLevel(logging.DEBUG)

# 표준 출력을 대상으로 하는 핸들러 생성
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

# JSON 포매터 설정
formatter = JsonFormatter()
stdout_handler.setFormatter(formatter)

# 로거에 핸들러 추가
logger.addHandler(stdout_handler)
