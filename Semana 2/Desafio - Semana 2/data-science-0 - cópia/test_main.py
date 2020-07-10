from main import *


def test_q1():
    result = q1()

    assert type(result) == tuple
    assert len(result) == 2


def test_q2():
    result = q2()

    assert type(result) == int


def test_q3():
    result = q3()

    assert type(result) == int


def test_q4():
    result = q4()

    assert type(result) == int


def test_q5():
    result = q5()

    assert type(result) == float
    assert 0.0 <= result <= 1.0


def test_q6():
    result = q6()

    assert type(result) == int


def test_q7():
    result = q7()

    assert result


def test_q8():
    result = q8()

    assert type(result) == float
    assert 0.0 <= result <= 1.0


def test_q9():
    result = q9()

    assert type(result) == int


def test_q10():
    result = q10()

    assert type(result) == bool