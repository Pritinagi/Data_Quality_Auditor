import logging
import config


logger=logging.getLogger("DATA QUALITY AUDITOR")

if not logger.handlers :
        # file handler
    logger.setLevel(logging.DEBUG)
    file_handler=logging.FileHandler(config.LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # formatter
    formatter=logging.Formatter(
        '%(asctime)s - %(name)s -%(levelname)s - %(message)s'
        )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

