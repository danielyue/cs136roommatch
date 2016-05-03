import pkg_resources
from .irving1985 import *
from .sethuramanteo import *

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'
