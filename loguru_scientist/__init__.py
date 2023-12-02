from loguru import logger
from loguru._logger import Logger
from loguru_scientist import scientist, constant, tooling

# Always disable loguru in librairy context
# https://loguru.readthedocs.io/en/stable/overview.html#suitable-for-scripts-and-libraries
logger.disable("loguru_scientist")

# Add new metric level
logger: Logger = scientist.logger_guru(logger)


__all__ = ["logger", "scientist", "constant", "tooling"]
