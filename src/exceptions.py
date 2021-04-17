# coding: utf8

class Error(Exception):
    pass


class DependencyNotFoundError(Error):
    """
    Exception used to indicate lack of dependency
    """
    pass
