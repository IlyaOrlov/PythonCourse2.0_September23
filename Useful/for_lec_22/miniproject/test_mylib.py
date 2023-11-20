import pytest
import mylib
import os


class TestFun:
    @classmethod
    def setup_class(cls):
        cls._filename = "file_for_test.txt"

    def teardown(self):
        if os.path.exists(self._filename):
            os.remove(self._filename)

    @pytest.fixture(
        scope='function',
        params=[{"args": (0, 1), "res": 0},
                {"args": (2, 2), "res": 4},
                {"args": (5, 1), "res": 5}],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrizer_mul(self, request):
        return request.param

    @pytest.fixture(
        scope='function',
        params=[{"args": (0, 1), "res": 1},
                {"args": (2, 2), "res": 4},
                {"args": (5, 1), "res": 6}],
        ids=lambda args: f"Test with args: {args}"
    )
    def parametrizer_sum(self, request):
        return request.param

    def test_mul(self, parametrizer_mul):
        args = parametrizer_mul['args']
        result = parametrizer_mul['res']
        mylib.fun("*", self._filename, *args)
        with open(self._filename) as f:
            actual_result = int(f.read().strip())
        assert actual_result == result

    def test_sum(self, parametrizer_sum):
        args = parametrizer_sum['args']
        result = parametrizer_sum['res']
        mylib.fun("+", self._filename,*args)
        with open(self._filename) as f:
            actual_result = int(f.read().strip())
        assert actual_result == result
