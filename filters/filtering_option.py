from typing import Any
from pydantic import BaseModel
from enums import FilterOption


class FilteringOption(BaseModel):
    option: FilterOption
    value: Any

    def apply(self, field_value):
        if self.option == FilterOption.Is:
            return field_value == self.value
        elif self.option == FilterOption.Lower:
            return field_value < self.value
        elif self.option == FilterOption.Greater:
            return field_value > self.value
        elif self.option == FilterOption.Contains:
            return self.value in field_value
        elif self.option == FilterOption.StartsWith:
            return field_value.startswith(self.value)
        elif self.option == FilterOption.EndsWith:
            return field_value.endswith(self.value)
        elif self.option == FilterOption.In:
            return field_value in self.value
        else:
            return False  # 알 수 없는 옵션은 기본적으로 False를 반환
