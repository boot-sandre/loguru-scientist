# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# Copyright © Simon ANDRÉ <simon@emencia.com> Emencia (https://www.emencia.com/)
# project: loguru-scientist
# github: https://github.com/boot-sandre/loguru-scientist/
from functools import partialmethod
from loguru import logger as logger_legacy


logger_legacy.level("METRIC", no=38, color="<green>", icon="📊")
logger_legacy.__class__.metric = partialmethod(logger_legacy.__class__.log, "METRIC")


logger = logger_legacy
__all__ = [
    "logger"
]
