#ifndef RPN_H
# define RPN_H

#include <stdio.h>
#include <stdlib.h>
#include "libft.h"

typedef struct	s_operation
{
	char		name;
	int			priority;
	double		(*fun)(int, int);
}				t_operation;

typedef struct	s_stack_op
{
	t_operation				op;
	struct s_stack_op		*previous;
}				t_stack_op;

t_operation g_opp[] =
{
		{'(', -1, NULL},
		{')', 0, NULL},
		{'-', 1, ft_sub},
		{'+', 1, ft_add},
		{'*', 2, ft_mul},
		{'/', 2, ft_div},
		{'%', 2, ft_mod},
		{'l', 2, ft_log},
		{'\0', 2, NULL}
};

t_operation is_op(char x)
t_stack_op					*create_stop(t_operation data);
void						remove_op(t_stack_op **op);
void						push_op(t_stack_op **begin_list,
									   t_operation data);

int is_digit(char x);
int is_op(char x);

#endif
