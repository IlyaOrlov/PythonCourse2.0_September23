from unittest import mock
import mylib2


class TestFun:
    def test_fun(self):
        # class Service:
        #     def __init__(self):
        #         self.service_started = False
        #         self.data = "123"
        #     def start(self):
        #         self.service_started = True
        #     def get_data(self):
        #         return self.data

        service = mock.Mock()
        data = "123"
        service.get_data.return_value = data
        res = mylib2.fun(service)
        assert service.start.called
        assert res == data
