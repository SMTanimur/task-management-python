"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from datetime import datetime

# Loguru
from loguru import logger

from typing import Any, TypeAlias, Union
import os

LoadData: TypeAlias = dict[
    str, Union[int, bool, dict[str, dict[str, Union[str, None, bool]]]]
]


def get_current_date():
    return datetime.now().strftime('%d-%m-%Y')


# ERROR
logger.add(
    f'logs/{get_current_date()}_task-management.log',
    rotation='00:00',
    retention='1 day',
    level='ERROR',
    format='{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}',
)

# WARNING
logger.add(
    f'logs/{get_current_date()}_task-management.log',
    rotation='00:00',
    retention='1 day',
    level='WARNING',
    format='{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}',
)

# INFO
logger.add(
    f'logs/{get_current_date()}_task-management.log',
    rotation='00:00',
    retention='1 day',
    level='INFO',
    format='{time:DD/MM/YYYY HH:mm:ss} | {level} | {message}',
)


classmethod
def execute_config(cls) -> LoadData:
    """
    Set up the configuration for logging.
    Additionally, check if the directory with the log file exists,
    where all the logs will be recorded.
    If the directory and file do not exist, we will create them.
    """
    # Increase the logging level for watchfiles.main to avoid log spam,
    # which could otherwise overload the system.
    logger = logger.getLogger("watchfiles.main")
    logger.setLevel(logger.WARNING)

    if os.path.exists("logs/app.log"):
        return cls.__load_config()
    # This check is related to Docker. In Docker, when the application is deployed,
    # the logs directory is created, as it is associated with the name of a volume,
    # so we only need to create the file.
    elif os.path.exists("logs/"):
        open("logs/app.log", "w").close()
        return cls.__load_config()
    else:
        os.mkdir("logs")
        open("logs/app.log", "w").close()
        return cls.__load_config()
