hungry
======

Python library for easily “eating” exceptions in functions. Eating can mean
either returning a default value or calling another function.

Introduction
------------

This library is basically just a function, namely ``hungry.eat``. Initially, I
wrote it for a document parser in which there was a lot of exception handling
logic for stuff I didn’t really care particularly much about.

Example usage
-------------

Eat all errors and return `None` if one was raised:

::

    @hungry.eat()
    def foo():
        ...

Eat ``ValueError`` exceptions and return 0 if it was raised:

::

    @hungry.eat(ValueError, error_value=0)
    def foo():
        ...

Eat ``IndexError`` and ``ValueError`` and fall back to function
``get_first_element`` if one of them is raised:

::

    @hungry.eat(IndexError, ValueError, error_handler=bar)
    def foo():
        ...

In the example above, ``bar`` will be passed the exception as the first
argument, followed by all the other arguments and keyword arguments in the
decorated function. This means that ``bar`` would have e.g. the following
signature:

::

    def bar(ex, *args, **kwargs):
        ...

TODO
----

Complete the test suite.
