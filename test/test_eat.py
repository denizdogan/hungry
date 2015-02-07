import pytest
from hungry import eat


def test_catch_one_exception():
    def f(val):
        return int(val[1])

    # should raise IndexError
    with pytest.raises(IndexError):
        f([1])

    # should NOT raise any exceptions
    f([1, 2])

    # decorate 'foo'
    foo = eat(IndexError)(f)

    # this time, the IndexError should be eaten
    foo([1])

    # ...but not ValueError
    with pytest.raises(ValueError):
        f([1, 'foo'])
