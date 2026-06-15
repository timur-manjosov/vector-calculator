# vector-calculator

A small object-oriented vector library written in Python. It works with
vectors of **any dimension** (2D, 3D, or higher) and implements the
fundamental operations of linear algebra. Each vector is represented as an
object that knows how to operate on itself.

## Features

- **Any dimension**: a vector can have any number of components
- **Addition** via operator overloading: write `v1 + v2` directly
  (raises an error if the vectors have different dimensions)
- **Scalar multiplication**: scale a vector by a number (stretch or shrink)
- **Magnitude**: the length of a vector, computed with the Pythagorean theorem
  generalized to any number of dimensions
- **Dot product**: measures how much two vectors point in the same direction
  (a dot product of 0 means the vectors are perpendicular)

## How to run

This project requires Python 3.

```bash
python main.py
```


