from sunpy.util.exceptions import warn_deprecated
from . import _jp2

__doc__ = _jp2.__doc__
__all__ = _jp2.__all__

warn_deprecated("The `sunpy.io.fits` module is deprecated, as it was designed "
                "for internal use.")
