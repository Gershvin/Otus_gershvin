import pytest
from src.Circle import Circle


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (4, 5, 18, 20),
                             (10, 20, 60, 200)
                         ])
def test_circle(side_a, side_b, perimeter, area):
    r = Circle(side_a, side_b)
    assert r.name == "Circle"
    assert r.area == area
    assert r.perimeter == perimeter


@pytest.mark.parametrize('radius',
                         [
                             (-4),
                             (0)
                         ])
def test_rectangle_negative (radius, perimeter, area):
    r = Circle(radius)
    assert r.name == "Rectangle"
    assert r.area == area
    assert r.perimeter== perimeter