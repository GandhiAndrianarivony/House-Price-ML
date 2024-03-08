class Factory:
    """Used to register creator
    
    Example:
        factory = ReaderFactory()
        factory.register_format('gzip', YAMLReader)
    """

    def __init__(self):
        self._creator = dict()

    def register(self, format: str, creator: object):
        self._creator[format] = creator

    def get_creator(self, format: str, *args, **kwargs):
        creator = self._creator.get(format, None)
        if not creator:
            raise ValueError(format)
        return creator(*args, **kwargs)
