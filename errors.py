class InvalidDataError(Exception):
    # Custom message for invalid data
    def __str__(self) -> str:
        return "파일이 유효한 JSON 형식이 아닙니다"
