"""Tests for :class:`vector_calculator.Vector`.

The suite is grouped by behaviour: construction and protocols, arithmetic,
the vector operations, and error handling. Floating-point results are compared
with :func:`pytest.approx` / :func:`math.isclose`.
"""

from __future__ import annotations

import doctest
import math

import pytest

from vector_calculator import (
    DimensionMismatchError,
    Vector,
    VectorError,
    ZeroVectorError,
)
from vector_calculator import (
    vector as vector_module,
)

# -- Construction & protocols -----------------------------------------------


def test_components_and_dimension():
    v = Vector(1, 2, 3)
    assert v.components == (1, 2, 3)
    assert v.dimension == 3
    assert len(v) == 3


def test_repr_roundtrips_through_eval():
    v = Vector(3, 4)
    assert repr(v) == "Vector(3, 4)"
    assert eval(repr(v)) == v  # noqa: S307 - trusted input in a test


def test_is_immutable():
    v = Vector(1, 2)
    with pytest.raises(AttributeError):
        v.components = (9, 9)  # type: ignore[misc]


def test_iteration_and_indexing():
    v = Vector(5, 6, 7)
    assert list(v) == [5, 6, 7]
    assert v[0] == 5
    assert v[-1] == 7


def test_equality_and_hashing():
    assert Vector(1, 2) == Vector(1, 2)
    assert Vector(1, 2) != Vector(1, 3)
    assert Vector(1, 2) != (1, 2)  # a tuple is not a Vector
    assert hash(Vector(1, 2)) == hash(Vector(1, 2))
    assert {Vector(1, 2), Vector(1, 2)} == {Vector(1, 2)}


def test_bool_is_false_only_for_zero_vector():
    assert not Vector(0, 0)
    assert Vector(0, 1)


# -- Arithmetic --------------------------------------------------------------


def test_addition_and_subtraction():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
    assert Vector(3, 4) - Vector(1, 2) == Vector(2, 2)


def test_scalar_multiplication_is_commutative():
    assert Vector(1, 2) * 3 == Vector(3, 6)
    assert 3 * Vector(1, 2) == Vector(3, 6)


def test_scalar_division():
    assert Vector(2, 4) / 2 == Vector(1, 2)


def test_negation():
    assert -Vector(1, -2) == Vector(-1, 2)


@pytest.mark.parametrize("bad", ["x", None, [1, 2]])
def test_multiplication_by_non_scalar_is_rejected(bad):
    with pytest.raises(TypeError):
        _ = Vector(1, 2) * bad


def test_adding_a_non_vector_is_rejected():
    with pytest.raises(TypeError):
        _ = Vector(1, 2) + 5


# -- Vector operations -------------------------------------------------------


def test_magnitude():
    assert Vector(3, 4).magnitude() == 5.0
    assert abs(Vector(3, 4)) == 5.0
    assert Vector().magnitude() == 0.0


def test_dot_product():
    assert Vector(1, 2, 3).dot(Vector(4, 5, 6)) == 32
    # Perpendicular vectors have a dot product of zero.
    assert Vector(1, 0).dot(Vector(0, 1)) == 0


def test_normalize_returns_unit_vector():
    unit = Vector(3, 4).normalize()
    assert unit.magnitude() == pytest.approx(1.0)
    assert unit == Vector(0.6, 0.8)


def test_angle_between_perpendicular_and_parallel_vectors():
    assert Vector(1, 0).angle(Vector(0, 1)) == pytest.approx(math.pi / 2)
    assert Vector(1, 0).angle(Vector(2, 0)) == pytest.approx(0.0)
    assert Vector(1, 0).angle(Vector(-1, 0)) == pytest.approx(math.pi)


def test_angle_is_numerically_stable_for_identical_vectors():
    # Without clamping cos(theta) the rounding could exceed 1 and raise.
    v = Vector(1, 1, 1)
    assert v.angle(v) == pytest.approx(0.0)


def test_projection():
    # Projecting onto an axis keeps only that component.
    assert Vector(3, 4).project_onto(Vector(1, 0)) == Vector(3, 0)
    assert Vector(2, 2).project_onto(Vector(0, 5)) == Vector(0, 2)


# -- Error handling ----------------------------------------------------------


@pytest.mark.parametrize(
    "operation",
    [
        lambda a, b: a + b,
        lambda a, b: a - b,
        lambda a, b: a.dot(b),
        lambda a, b: a.angle(b),
        lambda a, b: a.project_onto(b),
    ],
)
def test_dimension_mismatch_raises(operation):
    with pytest.raises(DimensionMismatchError):
        operation(Vector(1, 2), Vector(1, 2, 3))


def test_normalize_zero_vector_raises():
    with pytest.raises(ZeroVectorError):
        Vector(0, 0).normalize()


def test_angle_with_zero_vector_raises():
    with pytest.raises(ZeroVectorError):
        Vector(0, 0).angle(Vector(1, 0))


def test_project_onto_zero_vector_raises():
    with pytest.raises(ZeroVectorError):
        Vector(1, 2).project_onto(Vector(0, 0))


def test_package_errors_share_a_common_base():
    # Backwards compatible with the previous ValueError-based API.
    assert issubclass(DimensionMismatchError, VectorError)
    assert issubclass(ZeroVectorError, VectorError)
    assert issubclass(VectorError, Exception)
    assert issubclass(DimensionMismatchError, ValueError)


# -- Documentation -----------------------------------------------------------


def test_docstring_examples():
    results = doctest.testmod(vector_module, verbose=False)
    assert results.failed == 0
