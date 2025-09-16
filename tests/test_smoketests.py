import sys
sys.path.append('.')

import bin.normalize as nm

def test_of_pytest():
    assert True


def test_norm_hello_world():
    response = nm.hello_world("Efrain")
    assert response == "Hello World! and hi Efrain", f"Did not get expected answer in {response}"
