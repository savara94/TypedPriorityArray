import pytest
import sys
import os
import importlib
TypedPriorityArray = None

developer = sys.argv[1]
print(f'Trying tests for: {developer}')
module_str = f'typed_priority_array' 
sys.path.insert(0, os.path.abspath(f'../src/{developer}'))
module = importlib.import_module(module_str)
TypedPriorityArray = module.TypedPriorityArray
sys.argv.pop(1)
pytest.main()

def InvalidObject(object):
    pass

valid_args_types = [int, float]
valid_args_lists = [[0, 1, -1, 5, -5], [1, 2, 3], [0, 3, -1]]
valid_args = valid_args_types + valid_args_lists
invalid_args = [InvalidObject, object(), []]

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

@pytest.mark.parametrize("test_input", valid_args_lists)
def test_contains(test_input):
    tpa = TypedPriorityArray(*test_input)
    for x in test_input:
        assert x in tpa

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

@pytest.mark.parametrize("test_input", valid_args_lists)
def test_reverse(test_input):
    tpa = TypedPriorityArray(*test_input, reversed=True)

    sorted_input = sorted(test_input, reverse=True)
    tpa_len = len(tpa)
    for i in range(0, tpa_len):
        assert sorted_input[i] == tpa[i]

@pytest.mark.parametrize("test_input", valid_args_lists)
def test_cmp(test_input):
    tpa = TypedPriorityArray(*test_input, cmp=lambda x, y: y - x)

    sorted_input = sorted(test_input, reverse=True)
    tpa_len = len(tpa)
    for i in range(0, tpa_len):
        assert sorted_input[i] == tpa[i]




