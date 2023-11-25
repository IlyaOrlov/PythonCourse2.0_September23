import pytest
import to_roma


class TestTasksSuite:

    @pytest.mark.parametrize("num,roman", [("3", "III"), ("15", "XV"), ("21", "XXI")])
    def test_number(self, num, roman):
        assert to_roma.to_roman(num) == roman


if __name__ == "__main__":
    pytest.main()
