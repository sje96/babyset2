# test_babyset.py
# Demonstrates unit testing using the pytest module.
# pytest must be installed through pip.
import unittest

from baby_set import BabySet

def test_init():
    bset = BabySet([2, 4, 4])
    assert bset.size() == 2

def test_init_empty():
    bset = BabySet()
    assert bset.size() == 0

def test_add():
    bset = BabySet([2, 4, 4])
    bset.add(4)
    assert bset.size() == 2

def test_addSeq():
    pass

def test_get():
	pass

def test_remove():
    pass

def test_clear():
	pass
