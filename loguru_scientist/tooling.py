from .constant import LOG_METRIC_NO


def metric_only(record) -> bool:
    return record["level"].no == LOG_METRIC_NO
