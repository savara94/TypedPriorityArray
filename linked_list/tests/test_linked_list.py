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

valid_args = ['hello', [1, 2, 3], [object(), 'hello'], [(1, 2), (2, 3), (3, 4)]]
invalid_args = [ object(), 1]

@pytest.mark.parametrize("test_input", valid_args)
def test_constructor(test_input):
    assert LinkedList(test_input) is not None

@pytest.mark.parametrize("test_input", invalid_args)
def test_constructor_fail(test_input):
    with pytest.raises(ValueError):
        LinkedList(test_input)
