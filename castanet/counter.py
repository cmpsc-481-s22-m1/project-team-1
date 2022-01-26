# Import necessary types for typing
from typing import List, Tuple, Dict, Optional
# Import LibCST
import libcst as cst
from castanet import generate_trees as generator

import libcst.matchers as match


def match_imports(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports = match.findall(cast, match.Imports())
        imports_dictionary[file] = len(imports)

    return imports_dictionary


def total_imports(imports_dict):
    """Find and combine the number of import statements in Python files in a specific directory."""
    total_imports = 0
    for file in imports_dict:
        amount_of_imports = imports_dict[file]
        total_imports += amount_of_imports
    
    return total_imports


if __name__ == "__main__":
    directory = "/home/mkapfhammer/Documents/Allegheny/2022/Spring/CMPSC481/project-team-1/hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    imports_dictionary = match_imports(tree_dict)
    print(imports_dictionary)

