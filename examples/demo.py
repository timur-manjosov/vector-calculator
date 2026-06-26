"""Runnable tour of the public :class:`vector_calculator.Vector` API.

Run it with::

    python examples/demo.py
"""

from __future__ import annotations

import math

from vector_calculator import Vector, ZeroVectorError


def main() -> None:
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    print(f"\nv1 + v2        = {v1 + v2}")
    print(f"v1 - v2        = {v1 - v2}")
    print(f"v1 * 2         = {v1 * 2}")
    print(f"2 * v1         = {2 * v1}")
    print(f"-v1            = {-v1}")

    print(f"\n|v1|           = {abs(v1)}")
    print(f"v1 . v2        = {v1.dot(v2)}")
    print(f"v1 normalized  = {v1.normalize()}  (length {v1.normalize().magnitude()})")

    # A dot product of 0 means the vectors are perpendicular.
    print(f"\nright . up     = {Vector(1, 0).dot(Vector(0, 1))}")
    angle = Vector(1, 0).angle(Vector(0, 1))
    print(f"angle(right, up) = {angle} rad ({math.degrees(angle)} deg)")
    print(f"project v1 onto x-axis = {v1.project_onto(Vector(1, 0))}")

    # Operations that are undefined for the zero vector raise a clear error.
    try:
        Vector(0, 0).normalize()
    except ZeroVectorError as error:
        print(f"\nCaught expected error: {error}")


if __name__ == "__main__":
    main()
