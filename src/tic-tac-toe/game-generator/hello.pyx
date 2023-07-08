#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Hello world for CPython.
"""

def say_hello_to(name: str) -> None:
    """
    Print the text for hello [name].

    :type name: str
    :param name: The name of the person.

    :rtype: None
    """
    print(f'Hi, {name}\!')

if __name__ == '__main__':
    say_hello_to('Zxf')
