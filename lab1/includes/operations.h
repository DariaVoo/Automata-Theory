//
// Created by snorcros on 9/17/20.
//

#ifndef OPERATIONS_H
# define OPERATIONS_H
#include "rpn.h"

t_operation g_opp[] =
		{
				{'(', -1, NULL},
				{')', 0, NULL},
				{'-', 1, ft_sub},
				{'+', 1, ft_add},
				{'*', 2, ft_mul},
				{'/', 2, ft_div},
				{'%', 2, ft_mod},
				{'l', 3, ft_log},
				{'\0', 2, NULL}
		};

#endif
