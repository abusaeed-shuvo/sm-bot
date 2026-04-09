import logging
import os
from logging.handlers import TimedRotatingFileHandler
from rich.logging import RichHandler

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    
    # Path for the base log file
    log_file = "logs/bot.log"
    
    # Setup the Rotating Handler
    # 'when="midnight"' creates a new file every day
    # 'backupCount=7' keeps only the last 7 days of logs
    file_handler = TimedRotatingFileHandler(
        log_file, 
        when="midnight", 
        interval=1, 
        backupCount=7,
        encoding="utf-8"
    )
    
    # Set the suffix to match your yyyy_mm_dd preference
    # This appends to the filename after rotation
    file_handler.suffix = "%Y_%m_%d"

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s", # Rich handles its own timestamps/levels for console
        datefmt="[%X]",
        handlers=[
            file_handler,
            RichHandler(rich_tracebacks=True)
        ]
    )
    
    # Optional: Apply a specific format just to the file handler
    file_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
    file_handler.setFormatter(file_formatter)
