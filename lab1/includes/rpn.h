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



char		*to_rpn(char *str, char *end);
t_stack_op	*create_stop(t_operation data);
void		remove_op(t_stack_op **op);
void		push_op(t_stack_op **begin_list,
									   t_operation *data);
int			check_op(t_operation *a, t_stack_op **stack, char *out, int *j);
int			op_to_out(char op_name, char *out, int i);
void		add_delim_out(char *out, int *j);
char		*get_arg(char *out, char * str, int *j, char del);


void		ft_exit(char *error);
int			is_digit(char x);
//int is_op(char x);



#endif
