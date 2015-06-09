# macro_module.py
from macropy.core.macros import *

macros = Macros()

ct = dict

@macros.expr
def d(tree, **kw):
    keyworded_args = [keyword(arg.id, arg) for arg in tree.args]
    return Call(tree.func, [], tree.keywords + keyworded_args, None, None)
