hungry
======

Python library for easily “eating” exceptions in functions. Eating can
mean either returning a default value or calling another function.

Introduction
------------

This library is basically just a function, namely ``hungry.eat``.
Initially, I wrote it for a document parser in which there was a lot of
exception handling logic for stuff I didn’t really care particularly
much about.

Example usage
-------------

Eat ``ValueError`` exceptions and return 0.

::

    @hungry.eat(ValueError, error_value=0)


Eat ``IndexError`` and ``ValueError`` and fall back to function
``get_first_element`` on errors.

::

    @hungry.eat(IndexError, ValueError, error_handler=get_first_element)

In the example above, ``get_first_element`` will be passed the exception
as the first argument, followed by all the other arguments and keyword
arguments in the decorated function. This means that
``get_first_element`` would have e.g. the following signature:

::

    def get_first_element(exception, *args, **kwargs):

Running tests
-------------

The tests use `pytest`_. To run the tests without installing anything,
execute:

::

    $ python runtests.py

TODO
----

Complete the test suite.

.. _pytest: http://pytest.org/latest/