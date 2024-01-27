from model import Field
import enums


class FieldExtractor:
    def extract(
        self, log_type: enums.LogType, datas: list[dict[str, str]]
    ) -> set[Field]:
        field_list = set()
        for data in datas:
            for key in data.keys():
                field_list.add(Field(value=key))
        return field_list
