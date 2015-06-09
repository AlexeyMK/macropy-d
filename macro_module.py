# macro_module.py
from macropy.core.macros import *

macros = Macros()

ct = dict

@macros.expr
def d(*args, **kw):
    tree = kw["tree"]
    keyworded_args = [keyword(arg.id, arg) for arg in tree.args]
    return Call(Name('dict', Load()), [], tree.keywords + keyworded_args, None, None)
