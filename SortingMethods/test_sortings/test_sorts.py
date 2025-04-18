"""
Author: Isaac Jarrells
Date: March 6, 2025,
File: test_sorts.py
Purpose: This is the bubblesort algorithm which works by swapping adjacent elements in an unsorted array.
"""
from timer import timer
from SortingMethods.Sorting import bubblesort, selectionsort, quicksort, mergesort, heapsort
import pytest


@pytest.fixture
def arr():
    data = [5, 9, 7, 1, 2, 4, 3, 8, 6]
    return data


@timer
def test_bubblesort(arr):
    """Testing of the Bubblesort Algorithm"""
    assert bubblesort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


@timer
def test_selectionsort(arr):
    """Testing of Selection Sort Algorithm"""
    assert selectionsort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


@timer
def test_quicksort(arr):
    """Testing of Selection Sort Algorithm"""
    assert quicksort(arr, 0, len(arr) - 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


@timer
def test_mergesort(arr):
    """Testing of Merge Sort Algorithm"""
    assert mergesort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


@timer
def test_heapsort(arr):
    """Testing of Heap Sort Algorithm"""
    assert heapsort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
