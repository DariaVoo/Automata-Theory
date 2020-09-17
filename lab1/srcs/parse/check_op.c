//
// Created by snorcros on 9/10/20.
//
#include "rpn.h"

int op_to_out(char op_name, char *out, int i)
{
	out[i] = op_name;
	i++;
	out[i] = ' ';
	i++;
	return i;
}

int check_op(t_operation *a, t_stack_op *stack, char *out, int *j)
{
	t_operation b;
	int i;

	i = *j;
	if (!stack)
		return (0);
	b = stack->op;
	while (a->priority <= b.priority && stack)
	{
		b = stack->op;
		if (b.priority == 0) //if )
		{
			while (b.priority != -1 && stack) // while not (
			{
				stack = stack->previous;
				b = stack->op;

				i = op_to_out(b.name, out, i);
			}
			if (b.name != '(')
				ft_exit(NO_OPEN_BRACKET);
			stack = stack->previous;
			*j = i;
			return (0);
		}
		else {
			i = op_to_out(b.name, out, i);

			stack = stack->previous;
			*j = i;
			if (b.priority == 3)
				return (1);
		}
	}
	return (0);
}

