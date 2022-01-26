"""This module test the counter.py module regarding if statements"""
from castanet import counter
from castanet import generate_trees as generator

def test_match_if_statements_1():
    """Uses match_if_statements to identify all the if statements in the test_files directory"""
    directory = "./test_files"
    if_list = []
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    ifs = counter.match_if_statements(tree_dict)
    if_list += ifs
    assert len(if_list) == 5

def test_match_if_statements_2():
    """Uses match_if_statements to identify all the if-statements in the hello directory"""
    directory = "./hello"
    if_list = []
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    ifs = counter.match_if_statements(tree_dict)
    if_list += ifs
    assert len(if_list) == 2
