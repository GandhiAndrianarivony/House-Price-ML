import yaml

from apps.houses.data.interface import ReaderInterface


class YAMLReader(ReaderInterface):
    """Used to read yaml file"""

    def read(self, yaml_file):
        with open(yaml_file, "r") as f:
            self._data = yaml.safe_load(f)
