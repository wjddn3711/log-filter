from pydantic import BaseModel
from filters.filtering_option import FilteringOption


class FieldFilter(BaseModel):
    field_name: str
    filtering_option: FilteringOption

    def __field_name_list(self):
        # 필드명을 .을 기준으로 분리
        # ex) "a.b.c" -> ["a", "b", "c"]
        return self.field_name.split(".")

    def filter(self, log_entry: dict) -> bool:
        # 중첩된 필드에 접근하기 위한 함수
        def get_nested_field(data, keys):
            for key in keys:
                if isinstance(data, dict) and key in data:
                    data = data[key]
                else:
                    return None
            return data

        # 중첩된 필드에 대한 값을 가져옴
        field_value = get_nested_field(log_entry, self.__field_name_list())

        # FilteringOption을 사용하여 필터링
        return field_value is not None and self.filtering_option.apply(field_value)
