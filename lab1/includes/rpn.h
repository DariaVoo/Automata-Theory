#ifndef RPN_H
# define RPN_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libft.h"

#include "libftprintf.h"
#include "error_msg.h"

# define USAGE "./rpn '(1 + 2) - 3' -rpn"

typedef struct	s_operation
{
	char		name;
	int			priority;
	double		(*fun)(double, double);
}				t_operation;

typedef struct	s_stack_op
{
	t_operation				op;
	struct s_stack_op		*previous;
}				t_stack_op;

t_operation *is_op(char x);
double		ft_add(double a, double b);
double		ft_sub(double a, double b);
double		ft_mul(double a, double b);
double		ft_mod(double a, double b);
double		ft_div(double a, double b);
double		ft_log(double base, double b);

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


t_stack_op	*create_stop(t_operation data);
void		remove_op(t_stack_op **op);
void		push_op(t_stack_op **begin_list,
									   t_operation *data);
int			check_op(t_operation *a, t_stack_op *stack, char *out, int *i);

void		ft_exit(char *error);
int			is_digit(char x);
//int is_op(char x);



#endif
