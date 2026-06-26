# vector-calculator

A small, immutable, object-oriented vector library written in Python. It works
with vectors of **any dimension** (2D, 3D, or higher) and implements the
fundamental operations of linear algebra. A `Vector` behaves like the numbers
and sequences you already know: you can add, scale, compare, iterate over, and
hash it.

## Features

- **Any dimension** — a vector can have any number of components.
- **Immutable & hashable** — operations return new vectors; instances can be
  used as dict keys or set members.
- **Operator overloading** — `v1 + v2`, `v1 - v2`, `2 * v`, `-v`, `v / 2`,
  `abs(v)`, `v1 == v2`.
- **Sequence protocol** — `len(v)`, `v[i]`, `for c in v`.
- **Vector operations** — `magnitude()`, `dot()`, `normalize()`, `angle()`,
  `project_onto()`.
- **Clear errors** — `DimensionMismatchError` and `ZeroVectorError`, both
  derived from a common `VectorError` (and from `ValueError`).

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from vector_calculator import Vector

v1 = Vector(3, 4)
v2 = Vector(1, 2)

v1 + v2            # Vector(4, 6)
2 * v1             # Vector(6, 8)
abs(v1)            # 5.0
v1.dot(v2)         # 11
v1.normalize()     # Vector(0.6, 0.8)
v1.project_onto(Vector(1, 0))   # Vector(3.0, 0.0)
```

See [`examples/demo.py`](examples/demo.py) for a full tour:

```bash
python examples/demo.py
```

## Project layout

```
vector-calculator/
├── pyproject.toml
├── README.md
├── src/
│   └── vector_calculator/
│       ├── __init__.py
│       ├── vector.py        # the Vector class
│       └── exceptions.py    # the error hierarchy
├── tests/
│   └── test_vector.py
└── examples/
    └── demo.py
```

## Development

```bash
pytest        # run the test suite
ruff check .  # lint
```
