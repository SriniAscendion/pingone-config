import logging
import yaml
from pathlib import Path
from typing import Dict, Any


import logging

def setup_logging(name: str = "pingone_orchestrator", level: int = logging.INFO) -> logging.Logger:
    """
    Sets up and returns a logger with a consistent format.
    
    Args:
        name (str): Name of the logger.
        level (int): Logging level.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Don't let this logger propagate to the root logger
    logger.propagate = False

    return logger


def load_config(env_name: str) -> Dict[str, Any]:
    """
    Load the YAML configuration for the specified environment.
    """
    config_path = Path(__file__).parent.parent / "configs" / f"{env_name}.yaml"
    if not config_path.exists():
        logging.error(f" Configuration file not found: {config_path}")
        raise FileNotFoundError(f"No config found for environment: {env_name}")

    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            logging.info(f" Loaded config for environment: {env_name}")
            return config
    except yaml.YAMLError as e:
        logging.exception(" Error parsing the YAML config file.")
        raise
