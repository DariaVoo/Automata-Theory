from funs.fun_bool_expr import fun_bool_expr
from funs.fun_expr import fun_expr
from funs.fun_for import fun_for
from funs.fun_print import fun_print
from funs.fun_scan import fun_scan

RULES = {'print': fun_print,
         'scan': fun_scan,
         'for': fun_for,
         'expression': fun_expr,
         'bool_expression': fun_bool_expr}
