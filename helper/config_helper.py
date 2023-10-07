import os
from typing import Any
import yaml


class ConfigurationHelper:

    @classmethod
    def load_config(cls) -> dict:
        """Loads the configuration from the 'config.yml' file.

        Returns:
            A dictionary containing the loaded configuration.
        """
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(current_dir)
        except Exception as e:
            print(f"Error determining project root directory: {e}")
            project_root = cls.project_dir()

        file_path = os.path.join(project_root, 'config.yml')

        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
        return config

    @classmethod
    def get_conf(cls, key: str, default_value=None) -> Any:
        """Gets the value for a given key in the configuration file."""
        config = cls.load_config()
        keys = key.split(".")
        value = config
        try:
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            return default_value

    @staticmethod
    def project_dir():
        """Project directory"""
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
