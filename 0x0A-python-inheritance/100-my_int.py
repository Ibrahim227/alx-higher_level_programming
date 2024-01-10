#!/usr/bin/python3
"""Defines Class"""


class MyInt(int):
    """Define Class MyInt"""
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
