"""An immutable, n-dimensional Euclidean vector.

The :class:`Vector` class supports vectors of any dimension and implements the
fundamental operations of linear algebra through Python's operator and
sequence protocols, so vectors behave like the numbers and sequences users
already know.
"""

from __future__ import annotations

import math
from collections.abc import Iterator

from vector_calculator.exceptions import DimensionMismatchError, ZeroVectorError

__all__ = ["Vector"]

# A real-number scalar. ``bool`` is intentionally accepted as a subclass of int.
type Scalar = int | float


class Vector:
    """An immutable Euclidean vector with an arbitrary number of components.

    A vector is created from its components and is hashable and comparable, so
    it can be used as a dictionary key or stored in a set. Every operation that
    produces a vector returns a *new* instance; existing vectors are never
    mutated.

    Args:
        *components: The scalar components of the vector. The number of
            components defines the vector's :attr:`dimension`.

    Examples:
        >>> v = Vector(3, 4)
        >>> v + Vector(1, 2)
        Vector(4, 6)
        >>> abs(v)
        5.0
        >>> v == Vector(3, 4)
        True
    """

    __slots__ = ("_components",)

    def __init__(self, *components: Scalar) -> None:
        # ``*components`` is already an immutable tuple, so no defensive copy
        # is needed -- this is what makes the instance safely immutable.
        self._components: tuple[float, ...] = components

    # -- Inspection ---------------------------------------------------------

    @property
    def components(self) -> tuple[float, ...]:
        """The vector's components as an immutable tuple."""
        return self._components

    @property
    def dimension(self) -> int:
        """The number of components (i.e. the dimensionality of the vector)."""
        return len(self._components)

    def __repr__(self) -> str:
        inner = ", ".join(repr(component) for component in self._components)
        return f"Vector({inner})"

    # -- Sequence protocol --------------------------------------------------

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self) -> Iterator[float]:
        return iter(self._components)

    def __getitem__(self, index: int) -> float:
        return self._components[index]

    # -- Equality / hashing -------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self._components == other._components

    def __hash__(self) -> int:
        return hash(self._components)

    def __bool__(self) -> bool:
        """``False`` for the zero vector, ``True`` otherwise."""
        return any(self._components)

    # -- Arithmetic ---------------------------------------------------------

    def __add__(self, other: object) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        self._check_same_dimension(other)
        return Vector(
            *(a + b for a, b in zip(self._components, other._components, strict=True))
        )

    def __sub__(self, other: object) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        self._check_same_dimension(other)
        return Vector(
            *(a - b for a, b in zip(self._components, other._components, strict=True))
        )

    def __mul__(self, scalar: object) -> Vector:
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(*(component * scalar for component in self._components))

    # Scalar multiplication is commutative: ``2 * v`` reuses ``v * 2``.
    __rmul__ = __mul__

    def __truediv__(self, scalar: object) -> Vector:
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(*(component / scalar for component in self._components))

    def __neg__(self) -> Vector:
        return self * -1

    def __abs__(self) -> float:
        """The Euclidean length, so ``abs(v)`` mirrors :meth:`magnitude`."""
        return self.magnitude()

    # -- Vector operations --------------------------------------------------

    def magnitude(self) -> float:
        """Return the Euclidean length (magnitude) of the vector.

        Returns:
            The non-negative length ``sqrt(sum(c**2 for c in components))``,
            computed with :func:`math.hypot` for numerical stability.
        """
        return math.hypot(*self._components)

    def dot(self, other: Vector) -> float:
        """Return the dot (scalar) product with ``other``.

        Args:
            other: A vector of the same dimension.

        Returns:
            The sum of the component-wise products. A result of ``0`` means the
            vectors are orthogonal (perpendicular).

        Raises:
            DimensionMismatchError: If the vectors differ in dimension.
        """
        self._check_same_dimension(other)
        return math.sumprod(self._components, other._components)

    def normalize(self) -> Vector:
        """Return a unit vector pointing in the same direction.

        Returns:
            A new vector with :meth:`magnitude` ``1`` and the same direction.

        Raises:
            ZeroVectorError: If this is the zero vector, which has no direction.
        """
        length = self.magnitude()
        if length == 0:
            raise ZeroVectorError(
                "The zero vector has no direction and cannot be normalized."
            )
        return self / length

    def angle(self, other: Vector) -> float:
        """Return the angle to ``other`` in radians, in the range ``[0, pi]``.

        Args:
            other: A vector of the same dimension.

        Returns:
            The angle between the two vectors in radians.

        Raises:
            DimensionMismatchError: If the vectors differ in dimension.
            ZeroVectorError: If either vector is the zero vector.
        """
        self._check_same_dimension(other)
        magnitudes = self.magnitude() * other.magnitude()
        if magnitudes == 0:
            raise ZeroVectorError("The angle to the zero vector is undefined.")
        # Clamp to ``[-1, 1]`` to absorb floating-point error before acos.
        cos_theta = max(-1.0, min(1.0, self.dot(other) / magnitudes))
        return math.acos(cos_theta)

    def project_onto(self, other: Vector) -> Vector:
        """Return the vector projection of this vector onto ``other``.

        Args:
            other: The vector to project onto; must be non-zero.

        Returns:
            The component of this vector that lies along ``other``.

        Raises:
            DimensionMismatchError: If the vectors differ in dimension.
            ZeroVectorError: If ``other`` is the zero vector.
        """
        self._check_same_dimension(other)
        other_squared = other.dot(other)
        if other_squared == 0:
            raise ZeroVectorError("Cannot project onto the zero vector.")
        return (self.dot(other) / other_squared) * other

    # -- Internal helpers ---------------------------------------------------

    def _check_same_dimension(self, other: Vector) -> None:
        if self.dimension != other.dimension:
            raise DimensionMismatchError(self.dimension, other.dimension)
