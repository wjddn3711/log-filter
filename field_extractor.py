from model import Field
import enums


class FieldExtractor:
    def extract(self, log_type: enums.LogType, datas: list[dict]) -> set[Field]:
        field_set = set()
        for data in datas:
            self._extract_fields(data, field_set, "")
        field_set.add(Field(name=log_type.value, value_type=str))
        return field_set

    def _extract_fields(self, data: dict, field_set: set[Field], parent: str):
        for key, value in data.items():
            if isinstance(value, dict):
                # 중첩된 dict인 경우, 부모 필드와 함께 필드를 추가
                self._extract_fields(
                    value, field_set, f"{parent}.{key}" if parent else key
                )
            else:
                # 중첩되지 않은 경우, 필드를 추가
                field_set.add(
                    Field(
                        name=f"{parent}.{key}" if parent else key,
                        value_type=type(value),
                    )
                )
