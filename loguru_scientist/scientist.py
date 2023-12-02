# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# Copyright © Simon ANDRÉ <simon@emencia.com> Emencia (https://www.emencia.com/)
# project: loguru-scientist
# github: https://github.com/boot-sandre/loguru-scientist/
from functools import partial, partialmethod

from loguru._logger import Logger

from loguru_scientist.constant import (
    LOG_METRIC_COLOR,
    LOG_METRIC_ICON,
    LOG_METRIC_NAME,
    LOG_METRIC_NO,
)

from loguru_scientist.tooling import metric_only


def logger_guru(logger: Logger) -> Logger:
    # Configure metrics level logs
    # https://loguru.readthedocs.io/en/stable/resources/recipes.html#using-logging-function-based-on-custom-added-levels
    logger.level(
        LOG_METRIC_NAME, no=LOG_METRIC_NO, color=LOG_METRIC_COLOR, icon=LOG_METRIC_ICON
    )
    logger.__class__.metric = partialmethod(logger.__class__.log, LOG_METRIC_NAME)

    # Make by default some logger option
    # https://loguru.readthedocs.io/en/stable/resources/recipes.html#preserving-an-opt-parameter-for-the-whole-module
    logger.opt(lazy=False, capture=True)
    logger.opt = partial(logger.opt, lazy=False, capture=True)
    return logger


def configure_metrics_file_sink(
    logger: Logger, log_filepath: str = "metric/metrics.log", rotation="1 hour"
) -> Logger:
    """Add logging handler dedicated to metrics.

    The metrics logs record will be stored in file located`log_filepath` with json formatted lines
    """
    logger.add(
        sink=log_filepath,
        level=LOG_METRIC_NAME,
        format="{message}",
        filter=metric_only,
        serialize=True,
        rotation=rotation,
    )
    return logger
