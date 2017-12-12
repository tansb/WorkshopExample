import numpy as np
import pytest

from some_module import integrate_trapz
from some_module import extract_sentence_containing_word


# Testing the zero case. Plenty of other tests to write!
def test_integrate_trapz_1():
    xs, ys = np.linspace(0, 10, 10), np.zeros(10)
    assert integrate_trapz(xs, ys) == 0

def test_integrate_trapz_2():
    xs, ys = np.linspace(0, 10, 10), np.zeros(10)
    assert integrate_trapz(xs, ys) == 0


def test_extract_sentence_containing_word_1():
    assert extract_sentence_containing_word('Hello friend. Trying to test.', 'friend') == 'Hello friend'



# Testing too much - ensuring it fails on weird input
# Normally this would be an AssertionException or a specific
# exception, not the general Exception class.
def test_integrate_trapz_failure():
    with pytest.raises(Exception):
        integrate_trapz("Some", "Values")
