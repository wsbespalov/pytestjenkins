import pytest
import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)

from app.server import Wallet


def test_amount():
    w = Wallet(10)
    assert w.amount() == float(10.0)

def test_debet():
    w = Wallet(10)
    w.debet(10)
    assert w.amount() == float(0.0)

def test_credit():
    w = Wallet(10)
    w.credit(10)
    assert w.amount() == float(20.0)