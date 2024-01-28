from pydantic import BaseModel


class Field(BaseModel):
    name: str
    value_type: type

    def is_number_type(self) -> bool:
        try:
            # check value type is number and is not bool
            return issubclass(self.value_type, (int, float)) and not issubclass(
                self.value_type, bool
            )
        except ValueError:
            return False

    def __hash__(self) -> int:
        return hash(self.name)
