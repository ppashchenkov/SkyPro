import pytest
from slow_calculator import calculator


@pytest.mark.parametrize('delay_, res_', [
    (45, "15")
    ])
def test_calculator_45(delay_, res_):
    res = calculator(delay_)

    assert res == res_


@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('delay_, res_', [
    (44, "15")
    ])
def test_calculator_44(delay_, res_):
    res = calculator(delay_)

    assert res == res_
