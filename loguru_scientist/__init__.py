from loguru import logger

from loguru_scientist import scientist, constant, tooling

# Always disable loguru in librairy context
# https://loguru.readthedocs.io/en/stable/overview.html#suitable-for-scripts-and-libraries
logger.disable("loguru_scientist")

# Add new metric level
logger = scientist.logger_guru(logger)


__all__ = [
    "logger",
    "scientist",
    "constant",
    "tooling"
]
