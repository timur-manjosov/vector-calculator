"""Exception hierarchy for the :mod:`vector_calculator` package.

All package-specific errors derive from :class:`VectorError`, so callers can
catch every error this library raises with a single ``except VectorError``.
The concrete errors additionally inherit from :class:`ValueError` to stay
backwards compatible with the previous API, which raised plain ``ValueError``.
"""

from __future__ import annotations

__all__ = ["VectorError", "DimensionMismatchError", "ZeroVectorError"]


class VectorError(Exception):
    """Base class for every error raised by :mod:`vector_calculator`."""


class DimensionMismatchError(VectorError, ValueError):
    """Raised when an operation needs two vectors of equal dimension."""

    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right
        super().__init__(
            f"Vectors must have the same dimension, got {left} and {right}."
        )


class ZeroVectorError(VectorError, ValueError):
    """Raised when an operation is undefined for the zero vector.

    Examples are normalization, the angle to another vector, and projection
    onto the zero vector -- none of which have a defined direction.
    """
