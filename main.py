from logger import logger
import enums
import errors
from file_reader import FileReader
from field_extractor import FieldExtractor

target_file = r"/Users/jungwoo/Desktop/pythonProject/log-filter/example.log"
log_type = ""

file_reader = FileReader(logger)
field_extractor = FieldExtractor()

# check if log_type in LogTypeEnum
try:
    log_type = enums.LogType[log_type]
except KeyError:
    # log type이 지정되지 않은 경우, GLOBAL로 지정
    log_type = enums.LogType.GLOBAL

# read file
try:
    json_datas = file_reader.read(target_file)
    fields = field_extractor.extract(log_type=log_type, datas=json_datas)

    ## TODO: 숫자 필드들만 추출
    ## TODO: 숫자 필드들은 통계를 수행 할 수 있어야 함
except (FileNotFoundError, errors.InvalidDataError):
    logger.info("parse failed")
except Exception as e:
    logger.info("unknown error occurred")
    logger.info(e)
