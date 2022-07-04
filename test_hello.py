from hello import toyou, add, subtract


def test_add():
    assert add(1, 2) == 3


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10
    function.y = 5


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x
    del function.y


def test_hello_subtract():
    assert subtract(test_hello_subtract.x, test_hello_subtract.y) == 5
