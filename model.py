from pydantic import BaseModel


class Field(BaseModel):
    value: str

    def is_number_type(self) -> bool:
        try:
            float(self.value)
            return True
        except ValueError:
            return False

    def __hash__(self) -> int:
        return hash(self.value)
