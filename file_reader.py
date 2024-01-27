import json
import logging

from errors import InvalidDataError


class FileReader:
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger

    def read(self, file_path: str) -> list[dict[str, str]]:
        # file is log file
        # each line is json format
        # read file
        datas = list()
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    try:
                        data = json.loads(line)
                        datas.append(data)
                    except json.JSONDecodeError:
                        self.logger.info("file is not valid json format")
                        raise InvalidDataError
                    except Exception as e:
                        self.logger.info(e)
                        raise e
            return datas
        except FileNotFoundError:
            self.logger.info("file not found")
            raise FileNotFoundError
