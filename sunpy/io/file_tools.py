from sunpy.util.exceptions import warn_deprecated
from ._file_tools import *
from . import _file_tools

__doc__ = _file_tools.__doc__
__all__ = _file_tools.__all__

warn_deprecated("The `sunpy.io.file_tools` module is deprecated, as it was designed "
                "for internal use.")
