from filters.composite_filter import CompositeFilter
from filters.field_filter import FieldFilter
from filters.filtering_option import FilteringOption
from logger import logger
import enums
import errors
from file_reader import FileReader
from field_extractor import FieldExtractor

target_file = "ext.log"
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
    numbered_fields = [field for field in fields if field.is_number_type()]

    ## TODO: 숫자 필드들은 통계를 수행 할 수 있어야 함

    # field_filter = FieldFilter(
    #     field_name="id",
    #     filtering_option=FilteringOption(
    #         option=enums.FilterOption.Is, value="1728217692"
    #     ),
    # )
    # composite_filter = CompositeFilter([field_filter])
    # filtered_entries = composite_filter.filter(json_datas)
    # print(filtered_entries)

except (FileNotFoundError, errors.InvalidDataError):
    logger.info("parse failed")
except Exception as e:
    logger.info("unknown error occurred")
    logger.info(e)
