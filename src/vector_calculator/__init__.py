"""vector_calculator: a small, immutable n-dimensional vector library."""

from __future__ import annotations

from vector_calculator.exceptions import (
    DimensionMismatchError,
    VectorError,
    ZeroVectorError,
)
from vector_calculator.vector import Vector

__all__ = [
    "Vector",
    "VectorError",
    "DimensionMismatchError",
    "ZeroVectorError",
]
__version__ = "0.1.0"
