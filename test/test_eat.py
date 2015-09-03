import pytest
from hungry import eat


@eat()
def divide_element_by_two(elems, index):
    return elems[index] / 2


@eat(ValueError)
def convert_element_to_int(elems, index):
    return int(elems[index])


@eat(ValueError, IndexError, error_value='cat')
def add_to_element(elems, index, integer):
    return elems[index] + int(integer)


def echo_handler(ex, *args, **kwargs):
    """
    Example error handler which echoes the exception and the arguments.
    """
    return '%s/%s/%s' % (ex.message, ','.join(['%s' % arg for arg in args]), kwargs)


@eat(NameError, error_handler=echo_handler)
def access_unknown_variable(*args, **kwargs):
    return imaginary


def test_catch_all():
    assert None is divide_element_by_two([], 0)  # IndexError, caught
    assert None is divide_element_by_two(['a'], 0)  # TypeError, caught
    assert 5 == divide_element_by_two([10], 0)  # no problem


def test_catch_one():
    assert None is convert_element_to_int(['a'], 0)  # ValueError, caught
    with pytest.raises(IndexError):
        convert_element_to_int([], 0)  # IndexError


def test_catch_with_error_value():
    assert 'cat' is add_to_element([], 0, 'anything')  # IndexError, caught
    assert 'cat' is add_to_element([0], 0, 'string')  # ValueError, caught
    with pytest.raises(TypeError):
        add_to_element(['string'], 0, 1)  # TypeError


def test_catch_with_error_handler():
    assert "global name 'imaginary' is not defined//{}" == \
           access_unknown_variable()
    assert "global name 'imaginary' is not defined/4/{}" == \
           access_unknown_variable(4)
    assert "global name 'imaginary' is not defined/4,5,hello/\
{'foo': 'bar', 'cool': 'story'}" == access_unknown_variable(
        4, 5, 'hello', foo='bar', cool='story')
