__version__ = "1.2.2"

from fastcore.imports import IN_IPYTHON
from .imports import *

if IN_IPYTHON:
    from .showdoc import show_doc
