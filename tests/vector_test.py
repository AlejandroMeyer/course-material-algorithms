import pytest
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'solutions' / 'data_structures'))

from vector import Vector3D

def test_vector3d_initialization():
    v = Vector3D(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3

def test_vector3d_addition():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    result = v1 + v2
    assert result.x == 5
    assert result.y == 7
    assert result.z == 9

def test_vector3d_dot_product():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    result = v1.dot_product(v2)
    assert result == 32  # 1*4 + 2*5 + 3*6

def test_vector3d_magnitude():
    v = Vector3D(1, 2, 2)
    result = v.magnitude()
    assert result == 3  # sqrt(1^2 + 2^2 + 2^2)

def test_vector3d_str():
    v = Vector3D(1, 2, 3)
    result = str(v)
    assert result == "(1, 2, 3)"