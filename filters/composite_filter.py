from filters.field_filter import FieldFilter


class CompositeFilter:
    def __init__(self, filters: list[FieldFilter]):
        self.filters = filters

    def filter(self, log_entries: list[dict]) -> list[dict]:
        filtered_entries = []
        for log_entry in log_entries:
            # 모든 필터를 통과하는 경우에만 필터링
            passes_all_filters = all(
                filter_obj.filter(log_entry) for filter_obj in self.filters
            )
            if passes_all_filters:
                filtered_entries.append(log_entry)
        return filtered_entries
