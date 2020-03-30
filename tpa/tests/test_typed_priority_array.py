import pytest
import sys
import os
import importlib
import math
import functools

TypedPriorityArray = None

developer = sys.argv[1]
print(f'Trying tests for: {developer}')
module_str = 'typed_priority_array' 
sys.path.insert(0, os.path.abspath(f'../src/{developer}'))
module = importlib.import_module(module_str)
TypedPriorityArray = module.TypedPriorityArray
sys.argv.pop(1)
pytest.main()

class InvalidType(object):
    pass

class ValidType(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if not isinstance(other, ValidType):
            raise TypeError
        return self.x < other.x

    def __gt__(self, other):
        if not isinstance(other, ValidType):
            raise TypeError
        return self.x > other.x

    def __eq__(self, other):
        if not isinstance(other, ValidType):
            raise TypeError
        return self.x == other.x

def sqr_tuple(x):
    return x[0] ** 2 + x[1] ** 2

valid_args_types = [int, float, list, ValidType]
valid_args_lists = [[0, 1, -1, 5, -5], [1, 2, 3], [0, 3, -1], [[1, 2, 3], [1, 2], [-1]]]
valid_args_tuples =[(6, 6), (-5, -5), (1, 1), (20, 0), (30, -20)]
valid_args_custom_objects = [[ValidType(1, 0), ValidType(-1, 0), ValidType(3, 'something'), ValidType(-5, 'new')]]
valid_args_tuples_cmps = [
    lambda x,y : sqr_tuple(x) - sqr_tuple(y), 
    lambda x, y: x[0] - y[0], 
    lambda x, y: 1/(sqr_tuple(x) + 1) - 1/(sqr_tuple(y)+1)
]
valid_args = valid_args_types + valid_args_lists
invalid_args = [InvalidType, object(), []]

@pytest.mark.parametrize("test_input", valid_args_types)
def test_constructor_types(test_input):
    assert TypedPriorityArray(test_input) is not None

@pytest.mark.parametrize("test_input", valid_args_lists)
def test_constructor_lists(test_input):
    assert TypedPriorityArray(*test_input) is not None

@pytest.mark.parametrize("test_input", invalid_args)
def test_failing_constructor(test_input):
    with pytest.raises(TypeError):
        TypedPriorityArray(test_input)

@pytest.mark.parametrize("test_input", valid_args_lists + valid_args_custom_objects)
def test_contains(test_input):
    tpa = TypedPriorityArray(*test_input)
    for x in test_input:
        assert x in tpa

@pytest.mark.parametrize("test_input", valid_args_lists)
def test_insert(test_input):
    tpa = TypedPriorityArray(*test_input)
    value_to_insert = 3 if isinstance(test_input[0], int) else [5,4,3,2,1]
    tpa.insert(value_to_insert)
    sorted_input = list(test_input)
    sorted_input.append(value_to_insert)
    sorted_input.sort()

    for i in range(tpa.length):
        assert sorted_input[i] == tpa[i]

@pytest.mark.parametrize("test_input", valid_args)
def test_length(test_input):
    if isinstance(test_input, type):
        tpa = TypedPriorityArray(test_input)
        assert tpa.length == 0
        assert len(tpa) == 0
    elif isinstance(test_input, list):
        tpa = TypedPriorityArray(*test_input)
        assert tpa.length == len(test_input)
        assert len(tpa) == len(test_input)

@pytest.mark.parametrize("test_input", valid_args)
def test_array_type(test_input):
    if isinstance(test_input, type):
        tpa = TypedPriorityArray(test_input)
        assert tpa.array_type == test_input
    elif isinstance(test_input, list):
        tpa = TypedPriorityArray(*test_input)
        assert tpa.array_type == type(test_input[0])

@pytest.mark.parametrize("test_input", valid_args)
def test_element_type(test_input):
    if isinstance(test_input, type):
        tpa = TypedPriorityArray(test_input)
        assert tpa.array_type == test_input
    elif isinstance(test_input, list):
        tpa = TypedPriorityArray(*test_input)
        assert tpa.array_type == type(test_input[0])

@pytest.mark.parametrize("test_input", [[1, 4, 3, 5]])
def test_str(test_input):
    tpa = TypedPriorityArray(*test_input)
    assert str(tpa) == "[1 <= 3 <= 4 <= 5]"

@pytest.mark.parametrize("test_input", [[1, 4, 3, 5]])
def test_str_reversed(test_input):
    tpa = TypedPriorityArray(*test_input, reversed=True)
    assert str(tpa) == "[5 >= 4 >= 3 >= 1]"

@pytest.mark.parametrize("test_input", valid_args_lists + valid_args_custom_objects)
def test_reverse(test_input):
    tpa = TypedPriorityArray(*test_input, reversed=True)

    sorted_input = sorted(test_input, reverse=True)
    tpa_len = len(tpa)
    for i in range(0, tpa_len):
        assert sorted_input[i] == tpa[i]

    sorted_input = sorted(test_input)
    tpa.reversed = False
    for i in range(0, tpa.length):
        assert sorted_input[i] == tpa[i]

@pytest.mark.parametrize("test_input", [x for x in valid_args_lists if isinstance(x[0], (int, float))])
def test_cmp_nums(test_input):
    tpa = TypedPriorityArray(*test_input, cmp=lambda x, y: y - x)

    sorted_input = sorted(test_input, reverse=True)
    tpa_len = len(tpa)
    for i in range(0, tpa_len):
        assert sorted_input[i] == tpa[i]

@pytest.mark.parametrize("test_input", valid_args_tuples_cmps)
def test_cmp_tuples(test_input):
    tpa = TypedPriorityArray(*valid_args_tuples, cmp=test_input)

    sorted_input = sorted(valid_args_tuples, key=functools.cmp_to_key(test_input))
    tpa_len = len(tpa)
    for i in range(0, tpa_len):
        assert sorted_input[i] == tpa[i]
