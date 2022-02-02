"""This module uses commands to call functions from counter.py."""
import typer
from castanet import generate_trees as generator
from castanet import counter

app = typer.Typer(help="CASTAnet: A tool that helps you count the contents of your Python files!")

def generate_trees(directory_path:str):
    """Generate CASTs for each Python file in a directory with LibCST."""
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    return tree_dict


@app.command()
def if_statements(directory_path):
    """Determine number of if statements in a Python directory."""
    cast_dict = generate_trees(directory_path)
    if_dictionary = counter.match_if_statements(cast_dict)
    total_if_statements = counter.sum_cast_dict(if_dictionary)
    print("Number of if statements: ", str(total_if_statements))


@app.command()
def looping_constructs(directory_path):
    """Determine number of looping constructs in a Python directory."""
    cast_dict = generate_trees(directory_path)
    while_loops_dict = counter.count_whileloops(cast_dict)
    for_loops_dict = counter.count_forloops(cast_dict)
    number_for_loops = counter.sum_cast_dict(for_loops_dict)
    number_while_loops = counter.sum_cast_dict(while_loops_dict)
    total_loops = number_for_loops + number_while_loops
    print("Number for loops: " + str(number_for_loops))
    print("Number while loops: " + str(number_while_loops))
    print("Number total looping constructs: " + str(total_loops))

@app.command()
def assignment(directory_path):
    """Determine number of assignment statements in a Python directory."""
    cast_dict = generate_trees(directory_path)
    assignment_count_dict = counter.assignment_count(cast_dict)
    aug_assignment_count_dict = counter.aug_assignment_count(cast_dict)
    number_assignment_count = counter.sum_cast_dict(assignment_count_dict)
    number_aug_assignment_count = counter.sum_cast_dict(aug_assignment_count_dict)
    total_loops = number_assignment_count + number_aug_assignment_count
    print("Number of assignments: " + str(number_assignment_count))
    print("Number of aug assignments: " + str(number_aug_assignment_count))
    print("Number total assignments in program: " + str(total_loops))



@app.command()
def comments(directory_path:str):
    """Determine number of comments in a Python directory."""
    cast_dict = generate_trees(directory_path)
    comment_dictionary = counter.match_comment(cast_dict)
    total_comments = counter.sum_cast_dict(comment_dictionary)
    print("Number of comments: " + str(total_comments))


@app.command()
def functions_without_docstrings(directory_path):
    """Determine number of functions without docstrings in a Python directory."""
    cast_dict = generate_trees(directory_path)
    functions_dictionary = counter.match_funcdefs(cast_dict)
    number_missing_docstrings = counter.count_function_without_docstrings(functions_dictionary)
    print("Number of functions without docstrings: " + str(number_missing_docstrings))


@app.command()
def imports(directory_path:str):
    """Determine number of import statements in a Python directory."""
    cast_dict = generate_trees(directory_path)
    import_dictionary = counter.match_imports(cast_dict)
    total_imports = counter.sum_cast_dict(import_dictionary)
    print("Number of imports: " + str(total_imports))


@app.command()
def function_with_or_without_docstring(directory_path:str, function_name:str):
    """Determine if a given function has a docstring."""
    cast_dict = generate_trees(directory_path)
    docstring_status = counter.exists_docstring(cast_dict, function_name)
    if docstring_status == -1:
        print("Function does not exist.")
    if docstring_status == 0:
        print("Function does not have a docstring.")
    if docstring_status == 1:
        print("Function has a docstring.")


if __name__ == "__main__":
    app()
