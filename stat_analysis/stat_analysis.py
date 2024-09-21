import ast
import jedi
import argparse
import glob


class CallGraphVisitor(ast.NodeVisitor):
    def __init__(self, file_name, jedi_script):
        self._file_name = file_name
        self._jedi_script = jedi_script

    def visit_Call(self, node):
        caller = self._jedi_script.get_context(node.lineno, node.col_offset)

        point_of_interest_col_offset = (
            self._jedi_script._code_lines[node.func.lineno - 1][
                node.func.col_offset :
            ].index("(")
            + node.func.col_offset
            - 1
        )
        point_of_interest_lineno = node.func.lineno

        callees = self._jedi_script.infer(
            point_of_interest_lineno, point_of_interest_col_offset
        )

        if len(list(filter(lambda c: c.module_name == "builtins", callees))) > 0:
            # infer tends sometimes to resolve it as builtins, instead of correct module name
            callees = self._jedi_script.goto(
                point_of_interest_lineno,
                point_of_interest_col_offset,
                follow_imports=True,
                follow_builtin_imports=True,
            )

        for callee in callees:
            print(
                f"{callee.module_name}\t{callee.full_name}\t{caller.full_name}\t{self._file_name}:{node.lineno}"
            )


def main():
    _, unknown_args = argparse.ArgumentParser().parse_known_args()

    for glob_pattern in unknown_args:
        for file_name in glob.glob(glob_pattern, recursive=True):
            with open(file_name, "rt", encoding="utf-8") as f:
                code = f.read()
            ast_tree = ast.parse(code, file_name)
            jedi_script = jedi.Script(code, path=file_name)
            CallGraphVisitor(file_name, jedi_script).visit(ast_tree)


if __name__ == "__main__":
    main()
