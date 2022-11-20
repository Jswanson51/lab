import pytest
from account import *


class Test:

    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Austin', 10)

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'Austin'
        assert self.a2.get_balance() == pytest.approx(10.0, abs=0.001)

    def test_deposit(self):
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(50) is True
        assert self.a1.get_balance() == pytest.approx(50.0, abs=0.001)

        assert self.a1.deposit(-50) is False
        assert self.a1.get_balance() == pytest.approx(50.0, abs=0.001)

    def test_withdraw(self):
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(-5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(50) is False
        assert self.a1.get_balance() == 0

        assert self.a2.withdraw(5) is True
        assert self.a2.get_balance() == pytest.approx(5.0, abs=0.001)
