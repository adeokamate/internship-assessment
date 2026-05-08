from exercises.basics import collatz, distinct_numbers
from constants import collatz_1m, collatz_556

def test_collatz_1():
    assert collatz(3) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
    assert collatz(1) == [1]


def test_collatz_2():
    assert collatz(20) == [20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(15) == [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(17) == [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_collatz_3():
    assert collatz(1000000) == collatz_1m
    assert collatz(556443) ==  collatz_556


def test_distinct_numbers_1():
    assert distinct_numbers([2, 3, 2, 2, 3]) == 2
    assert distinct_numbers([5, 3, 1, 2, 10, 8, 7, 4, 6, 9]) == 10
    assert distinct_numbers([]) == 0


def test_distinct_numbers_2():
    assert distinct_numbers(collatz_1m) == 153
    assert distinct_numbers(collatz_556) == 116

