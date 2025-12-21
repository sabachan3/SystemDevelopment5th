"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def calc():
    return Calculator()

class TestAddition:

    def test_add_positive_numbers(self, calc):
        assert calc.add(5, 3) == 8

    def test_add_negative_numbers(self, calc):
        assert calc.add(-5, -3) == -8

    def test_add_positive_and_negative(self, calc):
        assert calc.add(5, -3) == 2

    def test_add_negative_and_positive(self, calc):
        assert calc.add(-5, 3) == -2

    def test_add_positive_with_zero(self, calc):
        assert calc.add(5, 0) == 5

    def test_add_zero_with_positive(self, calc):
        assert calc.add(0, 5) == 5

    def test_add_floats(self, calc):
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtraction:

    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(5, 3) == 2

    def test_subtract_negative_numbers(self, calc):
        assert calc.subtract(-5, -3) == -2

    def test_subtract_positive_and_negative(self, calc):
        assert calc.subtract(5, -3) == 8

    def test_subtract_negative_and_positive(self, calc):
        assert calc.subtract(-5, 3) == -8

    def test_subtract_positive_with_zero(self, calc):
        assert calc.subtract(5, 0) == 5

    def test_subtract_zero_with_positive(self, calc):
        assert calc.subtract(0, 5) == -5

    def test_subtract_zero_with_negative(self, calc):
        assert calc.subtract(0, -5) == 5

    def test_subtract_floats(self, calc):
        assert calc.subtract(2.5, 3.7) == pytest.approx(-1.2)


class TestMultiplication:

    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(5, 3) == 15
    
    def test_multiply_negative_numbers(self, calc):
        assert calc.multiply(-5, -3) == 15

    def test_multiply_positive_and_negative(self, calc):
        assert calc.multiply(5, -3) == -15

    def test_multiply_negative_and_positive(self, calc):
        assert calc.multiply(-5, 3) == -15
    
    def test_multiply_zero_with_positive(self, calc):
        assert calc.multiply(0, 5) == 0

    def test_multiply_zero_with_negative(self, calc):
        assert calc.multiply(0, -5) == 0

    def test_multiply_floats(self, calc):
        assert calc.multiply(2.5, 3.7) == pytest.approx(9.25)


class TestDivision:

    def test_divide_positive_numbers(self, calc):
        assert calc.divide(5, 3) == pytest.approx(1.6666666666666667)

    def test_divide_negative_numbers(self, calc):
        assert calc.divide(-5, -3) == pytest.approx(1.6666666666666667)

    def test_divide_positive_and_negative(self, calc):
        assert calc.divide(5, -3) == pytest.approx(-1.6666666666666667)

    def test_divide_negative_and_positive(self, calc):
        assert calc.divide(-5, 3) == pytest.approx(-1.6666666666666667)

    def test_divide_zero_with_positive(self, calc):
        assert calc.divide(0, 5) == 0

    def test_divide_zero_with_negative(self, calc):
        assert calc.divide(0, -5) == 0

    def test_divide_floats(self, calc):
        assert calc.divide(2.5, 3.7) == pytest.approx(0.6756756756756757)

    def test_divide_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(10, 0)



class TestInvalidInputs:
    def test_add_input_too_large(self, calc):
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 1)

    def test_add_input_too_small(self, calc):
        with pytest.raises(InvalidInputException):
            calc.add(-1000001, 1)

    def test_add_invalid_second_argument(self, calc):
        with pytest.raises(InvalidInputException):
            calc.add(1, 1000001)

    def test_subtract_input_too_large(self, calc):
        with pytest.raises(InvalidInputException):
            calc.subtract(1000001, 1)

    def test_subtract_invalid_second_argument(self, calc):
        with pytest.raises(InvalidInputException):
            calc.subtract(1, -1000001)

    def test_multiply_input_too_large(self, calc):
        with pytest.raises(InvalidInputException):
            calc.multiply(1000001, 1)

    def test_multiply_invalid_second_argument(self, calc):
        with pytest.raises(InvalidInputException):
            calc.multiply(1, 1000001)


    def test_divide_input_too_large(self, calc):
        with pytest.raises(InvalidInputException):
            calc.divide(1000001, 1)

    def test_divide_invalid_second_argument(self, calc):

        with pytest.raises(InvalidInputException):
            calc.divide(1, 1000001)

class TestBoundaries:

    def test_boundary_max_value(self, calc):
        assert calc.add(1000000, 0) == 1000000

    def test_boundary_min_value(self, calc):
        assert calc.add(-1000000, 0) == -1000000

    def test_boundary_just_above_max(self, calc):
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 0)

    def test_boundary_just_below_min(self, calc):
        with pytest.raises(InvalidInputException):
            calc.add(-1000001, 0)