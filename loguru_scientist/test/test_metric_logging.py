import unittest

from loguru_scientist.constant import LOG_METRIC_NAME
from loguru_scientist.scientist import configure_metrics_file_sink
from loguru_scientist import logger
from contextlib import contextmanager

@contextmanager
def capture_logs(level="INFO", format="{level}:{name}:{message}"):
    """Capture loguru-based logs."""
    output = []
    handler_id = logger.add(output.append, level=level, format=format)
    yield output
    logger.remove(handler_id)


class MyTestCase(unittest.TestCase):
    def all_level(self):
        self.assertLogs(logger, level=LOG_METRIC_NAME)
        self.assertLogs(logger, level="INFO")
        self.assertLogs(logger, level="DEBUG")
        self.assertLogs(logger, level="TRACE")
        self.assertLogs(logger, level="ERROR")
        self.assertLogs(logger, level="WARNING")
        self.assertLogs(logger, level="SUCCESS")

    def test_configure_metrics_file_sink(self):
        self.all_level()
        configure_metrics_file_sink(logger)
        self.all_level()


if __name__ == '__main__':
    unittest.main()
