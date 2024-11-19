import pytest
from saxonche import *

@pytest.fixture
def proc():
    return PySaxonProcessor()

def test_get_empty_sequence(proc):
    empty = proc.empty_sequence()
    assert isinstance(empty, PyXdmValue)
    assert empty.size == 0
