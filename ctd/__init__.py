"""
Tools to load hydrographic data as pandas DataFrame with some handy methods for
data pre-processing and analysis.
"""

from .plotting import plot_cast
from .processing import (
    bindata,
    despike,
    lp_filter,
    movingaverage,
    press_check,
    remove_above_water,
    smooth,
    split,
)
from .read import (
    from_bl,
    from_btl,
    from_castaway_csv,
    from_cnv,
    from_edf,
    from_fsi,
    rosette_summary,
)

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"


__all__ = [
    "bindata",
    "despike",
    "from_bl",
    "from_btl",
    "from_castaway_csv",
    "from_cnv",
    "from_edf",
    "from_fsi",
    "lp_filter",
    "movingaverage",
    "plot_cast",
    "press_check",
    "remove_above_water",
    "rosette_summary",
    "smooth",
    "split",
]
