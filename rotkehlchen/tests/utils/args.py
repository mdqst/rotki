from typing import NamedTuple

from rotkehlchen.constants.misc import (
    DEFAULT_MAX_LOG_BACKUP_FILES,
    DEFAULT_MAX_LOG_SIZE_IN_MB,
    DEFAULT_SQL_VM_INSTRUCTIONS_CB,
)
from rotkehlchen.db.drivers.server import DEFAULT_DB_WRITER_PORT
from rotkehlchen.tasks.server import DEFAULT_BG_WORKER_PORT


class ConfigurationArgs(NamedTuple):
    data_dir: str | None
    ethrpc_endpoint: str | None
    logfile: str | None
    logtarget: str | None
    loglevel: str
    logfromothermodules: bool
    max_size_in_mb_all_logs: int = DEFAULT_MAX_LOG_SIZE_IN_MB
    max_logfiles_num: int = DEFAULT_MAX_LOG_BACKUP_FILES
    sqlite_instructions: int = DEFAULT_SQL_VM_INSTRUCTIONS_CB
    process: str = 'api_server'
    db_api_port: int = DEFAULT_DB_WRITER_PORT
    bg_worker_port: int = DEFAULT_BG_WORKER_PORT


def default_args(
        data_dir: str | None = None,
        ethrpc_endpoint: str | None = None,
        max_size_in_mb_all_logs: int = DEFAULT_MAX_LOG_SIZE_IN_MB,
        loglevel: str = 'debug',
        process: str = 'api_server',
        db_writer_port: int = DEFAULT_DB_WRITER_PORT,
        bg_worker_port: int = DEFAULT_BG_WORKER_PORT,
):
    return ConfigurationArgs(
        loglevel=loglevel,
        logfromothermodules=False,
        data_dir=data_dir,
        ethrpc_endpoint=ethrpc_endpoint,
        max_size_in_mb_all_logs=max_size_in_mb_all_logs,
        max_logfiles_num=DEFAULT_MAX_LOG_BACKUP_FILES,
        sqlite_instructions=DEFAULT_SQL_VM_INSTRUCTIONS_CB,
        logfile=None,
        logtarget=None,
        db_api_port=db_writer_port,
        bg_worker_port=bg_worker_port,
        process=process,
    )
