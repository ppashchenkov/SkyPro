import pytest
from labs import labs_shopping


@pytest.mark.parametrize('res_', [
    ("Total: $58.29")
    ])
def test_labs_shopping(res_):
    res = labs_shopping()

    assert res == res_
