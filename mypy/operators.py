"""Information about Python operators"""

from typing_extensions import Final

# Map from binary operator id to related method name (in Python 3).
op_methods: Final = {
    "+": "__add__",
    "-": "__sub__",
    "*": "__mul__",
    "/": "__truediv__",
    "%": "__mod__",
    "divmod": "__divmod__",
    "//": "__floordiv__",
    "**": "__pow__",
    "@": "__matmul__",
    "&": "__and__",
    "|": "__or__",
    "^": "__xor__",
    "<<": "__lshift__",
    ">>": "__rshift__",
    "==": "__eq__",
    "!=": "__ne__",
    "<": "__lt__",
    ">=": "__ge__",
    ">": "__gt__",
    "<=": "__le__",
    "in": "__contains__",
}

op_methods_to_symbols: Final = {v: k for (k, v) in op_methods.items()}

ops_falling_back_to_cmp: Final = {"__ne__", "__eq__", "__lt__", "__le__", "__gt__", "__ge__"}


ops_with_inplace_method: Final = {
    "+",
    "-",
    "*",
    "/",
    "%",
    "//",
    "**",
    "@",
    "&",
    "|",
    "^",
    "<<",
    ">>",
}

inplace_operator_methods: Final = {"__i" + op_methods[op][2:] for op in ops_with_inplace_method}

reverse_op_methods: Final = {
    "__add__": "__radd__",
    "__sub__": "__rsub__",
    "__mul__": "__rmul__",
    "__truediv__": "__rtruediv__",
    "__mod__": "__rmod__",
    "__divmod__": "__rdivmod__",
    "__floordiv__": "__rfloordiv__",
    "__pow__": "__rpow__",
    "__matmul__": "__rmatmul__",
    "__and__": "__rand__",
    "__or__": "__ror__",
    "__xor__": "__rxor__",
    "__lshift__": "__rlshift__",
    "__rshift__": "__rrshift__",
    "__eq__": "__eq__",
    "__ne__": "__ne__",
    "__lt__": "__gt__",
    "__ge__": "__le__",
    "__gt__": "__lt__",
    "__le__": "__ge__",
}

reverse_op_method_names: Final = set(reverse_op_methods.values())

# Suppose we have some class A. When we do A() + A(), Python will only check
# the output of A().__add__(A()) and skip calling the __radd__ method entirely.
# This shortcut is used only for the following methods:
op_methods_that_shortcut: Final = {
    "__add__",
    "__sub__",
    "__mul__",
    "__truediv__",
    "__mod__",
    "__divmod__",
    "__floordiv__",
    "__pow__",
    "__matmul__",
    "__and__",
    "__or__",
    "__xor__",
    "__lshift__",
    "__rshift__",
}

normal_from_reverse_op: Final = {m: n for n, m in reverse_op_methods.items()}
reverse_op_method_set: Final = set(reverse_op_methods.values())

unary_op_methods: Final = {"-": "__neg__", "+": "__pos__", "~": "__invert__"}
