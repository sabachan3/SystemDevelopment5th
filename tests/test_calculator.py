"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

def calc():
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self):
        """Test subtracting positive and negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self):
        """Test subtracting negative and positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_with_zero(self):
        """Test subtracting positive number with zero."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_with_positive(self):
        """Test subtracting zero with positive number."""
        # TODO: Implement
        calc = Calculator()
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_with_negative(self):
        """Test subtracting zero with negative number."""
        # TODO: Implement
        calc = Calculator()
        a = 0
        b = -5
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = -1.2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = -3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        # TODO: Implement   
        calc = Calculator()
        a = -5
        b = 3
        expected = -15

        # Act
        result = calc.multiply(a, b)
        # Assert
        assert result == expected
    
    def test_multiply_zero_with_positive(self):
        """Test multiplying zero with positive number."""
        # TODO: Implement
        calc = Calculator()
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


    def test_multiply_zero_with_negative(self):
        """Test multiplying zero with negative number."""
        # TODO: Implement
        calc = Calculator()
        a = 0
        b = -5
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 9.25

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
            """Test dividing positive numbers."""
            # TODO: Implement
            calc = Calculator()
            a = 5
            b = 3
            expected = 1.6666666666666667

            # Act
            result = calc.divide(a, b)

            # Assert
            assert result == expected
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -5
        b = -3
        expected = 1.6666666666666667

        # Act
        result = calc.divide(a, b)  

        # Assert
        assert result == expected

    def test_divide_positive_and_negative(self):
        """Test dividing positive and negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = -3
        expected = -1.6666666666666667

        # Act
        result = calc.divide(a, b)
        # Assert
        assert result == expected

    def test_divide_negative_and_positive(self):
        """Test dividing negative and positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -5
        b = 3
        expected = -1.6666666666666667
        # Act
        result = calc.divide(a, b)
        # Assert
        assert result == expected

    def test_divide_zero_with_positive(self):
        """Test dividing zero with positive number."""
        # TODO: Implement
        calc = Calculator()
        a = 0
        b = 5
        expected = 0
        # Act
        result = calc.divide(a, b)
        # Assert
        assert result == expected       

    def test_divide_zero_with_negative(self):
        """Test dividing zero with negative number."""
        # TODO: Implement
        calc = Calculator()
        a = 0
        b = -5
        expected = 0
        # Act
        result = calc.divide(a, b)
        # Assert
        assert result == expected


    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 0.6756756756756757
        # Act
        result = calc.divide(a, b)
        # Assert
        assert result == pytest.approx(expected)