import pytest
import sys
import os
import importlib
import math
import functools

LinkedList = None

developer = sys.argv[1]
print(f'Trying tests for: {developer}')
module_str = 'linked_list' 
sys.path.insert(0, os.path.abspath(f'../src/{developer}'))
module = importlib.import_module(module_str)
LinkedList = module.LinkedList
sys.argv.pop(1)
pytest.main()

valid_args = ['hello', [1, 2, 3], [object(), 'hello'], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]]
invalid_args = [object(), 1]

@pytest.mark.parametrize("test_input", valid_args)
def test_constructor(test_input):
    assert LinkedList(test_input) is not None

@pytest.mark.parametrize("test_input", invalid_args)
def test_constructor_fail(test_input):
    with pytest.raises(ValueError):
        LinkedList(test_input)

@pytest.mark.parametrize("test_input", [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
def test_constructor_fail_max_size(test_input):
    with pytest.raises(MemoryError):
        LinkedList(test_input, max_size=5)

def test_max_size():
    ll1 = LinkedList('example')
    assert ll1.max_size == None

    ll2 = LinkedList([1, 2, 3], max_size=50)
    assert ll2.max_size == 50

@pytest.mark.parametrize("test_input", valid_args)
def test_length(test_input):
    ll = LinkedList(test_input)

    assert len(ll) == len(test_input) == ll.length

@pytest.mark.parametrize("test_input", valid_args)
def test_get_item(test_input):
    ll = LinkedList(test_input)

    for i, _ in enumerate(test_input):
        assert ll[i] == test_input[i]

@pytest.mark.parametrize("test_input", valid_args)
def test_index_of(test_input):
    ll = LinkedList(test_input)

    for x in test_input:
        assert test_input.index(x) == ll.index_of(x)

@pytest.mark.parametrize("test_input", valid_args)
def test_iterator(test_input):
    ll = LinkedList(test_input)

    for i, x in enumerate(ll):
        assert test_input[i] == x

@pytest.mark.parametrize("test_input", valid_args)
def test_append(test_input):
    ll = LinkedList(test_input)

    if 'append' in dir(test_input):
        for i in range(10):
            ll.append(i)
            test_input.append(i)

    for i, x in enumerate(ll):
        assert x == test_input[i]

def test_str():
    ll = LinkedList([1, 2, 3])
    assert str(ll) == "1 -> 2 -> 3"
    
    ll = LinkedList([1, 2, 3, [1, 2, 3]])
    assert str(ll) == "1 -> 2 -> 3 -> [1, 2, 3]"

@pytest.mark.parametrize("test_input", valid_args)
def test_contains(test_input):
    ll = LinkedList(test_input)

    for x in test_input:
        assert x in ll

def test_not_contains():
    test_input = [1, 2, 3, 4]
    ll = LinkedList(test_input)

    assert 5 not in  ll

@pytest.mark.parametrize("test_input", valid_args)
def test_reverse(test_input):
    ll = LinkedList(test_input)
    length = len(test_input)

    for i, x in enumerate(reversed(ll)):
        assert x == test_input[length - i - 1]

@pytest.mark.parametrize("test_input", valid_args)
def test_pop(test_input):
    if isinstance(test_input, list):        
        ll = LinkedList(test_input)
        
        while len(test_input) > 0:
            index = len(test_input) // 2
            assert ll.pop(index) == test_input.pop(index)
            assert list(iter(ll)) == test_input

@pytest.mark.parametrize("test_input", valid_args)
def test_insert(test_input):
    if isinstance(test_input, list):        
        ll = LinkedList(test_input)

        indices = [len(test_input) - 1, len(test_input) // 2, 0]
        
        for index in indices:
            ll.insert(index, index)
            test_input.insert(index, index)
            assert list(iter(ll)) == test_input

@pytest.mark.parametrize("test_input", valid_args)
def test_inverse(test_input):
    ll = LinkedList(test_input, max_size=100)
    ll_i = ll.inverse()
    assert isinstance(ll_i, LinkedList)
    assert ll_i.max_size == ll.max_size

    assert list(ll_i) == list(reversed(test_input))