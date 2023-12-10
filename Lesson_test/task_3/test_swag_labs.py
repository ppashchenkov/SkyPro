import pytest
from users import Users
from swag_labs import swag_labs_shopping

my_users = Users("Петя", "Петечкин", "101001")


@pytest.mark.parametrize('users_, res_', [
    (my_users, "Total: $58.29")
    ])
def test_swag_labs_shopping(users_, res_):
    res = swag_labs_shopping(users_)

    assert res == res_
