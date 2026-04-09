import logging
import importlib
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

def load_models():
    base_path = Path("database/models")

    for path in base_path.rglob("*.py"):
        if path.name == "__init__.py":
            continue

        module = ".".join(path.with_suffix("").parts)

        if module not in sys.modules:
            importlib.import_module(module)
            logger.info(f"Loaded model: {module}")
