import logging
from logging.handlers import RotatingFileHandler
import sys

# global logger config
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    handlers=[
        RotatingFileHandler(
            "log",
            mode='a+',
            maxBytes=10*1024*1024,
            backupCount=10,
            encoding=None,
            delay=0
        ),
        logging.StreamHandler(sys.stdout)
    ]
)

# log handler
def log_handler(ack, client, context, event, payload, logger :logging.Logger, next):
    if event:
        logger.info(f"User {event['user']}@{event['channel']} triggered event: {event['type']}")
    
    if payload.get("command"):
        logger.info(f"User {payload['user_name']} is attempting {payload['command']} {payload['text']}")

    next()