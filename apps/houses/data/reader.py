from .factory import Factory


class Reader:
    """Used to read

    Example:
        file_reader = FileReader()
        res = file_reader.read_file(factory, 'gzip', 'file/path/')
    """

    def read_file(self, factory: Factory, format, file_path):
        creator = factory.get_creator(format)
        creator.read(file_path)
        return creator.data
