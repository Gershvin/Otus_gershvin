import pytest
from src.Rectangle import Rectangle


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (4, 5, 18, 20),
                             (10, 20, 60, 200)
                         ])
def test_rectangle(side_a, side_b, perimeter, area):
    r = Rectangle(side_a, side_b)
    assert r.name == "Rectangle"
    assert r.area == area
    assert r.perimeter== perimeter


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (-4, 5, 2, -20),
                             (0, 20, 40, 0)
                         ])
def test_rectangle_negative(side_a, side_b, perimeter, area):
    r = Rectangle(side_a, side_b)
    assert r.name == "Rectangle"
    assert r.area == area
    assert r.perimeter== perimeter