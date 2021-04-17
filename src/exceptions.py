# coding: utf8

class Error(Exception):
    pass


class DependencyNotFoundError(Error):
    """
    Exception used to indicate lack of dependency
    """
    pass


class WifiNotFoundError(Error):
    """
    Exception raised when the system has no wifi connection
    """
    pass