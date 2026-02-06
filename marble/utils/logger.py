"""
Logging utility module.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def get_logger(name: str, log_to_file: Optional[str] = None) -> logging.Logger:
    """
    Get a configured logger.

    Args:
        name (str): Name of the logger.
        log_to_file (Optional[str]): If provided, also log to this file path.
                                      Default: None (console only).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
        )

        # Console handler (always enabled)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # File handler (optional)
        if log_to_file:
            log_path = Path(log_to_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = RotatingFileHandler(
                log_to_file, maxBytes=10485760, backupCount=5
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
