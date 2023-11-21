import pytest
import project.example as example


class TestExample:
    def test_myfun(self):
        assert example.myfun(10, 20) == 30


if __name__ == "__main__":
    pytest.main()
