//
// Created by snorcros on 9/10/20.
//
#include "rpn.h"

int check_op(t_operation *a, t_stack_op *stack, char *out, int *j)
{
	t_operation b;
	int i;

	i = *j;
	while (a->priority <= b.priority && stack)
	{
		b = stack->op;
		if (b.priority == 0) //if )
		{
			while (b.priority != -1 && stack) // while not (
			{
				stack = stack->previous;
				b = stack->op;

				out[i] = b.name;
				i++;
				out[i] = ' ';
				i++;
			}
			if (b.name != '(')
				ft_exit(NO_OPEN_BRACKET);
			stack = stack->previous;
			*j = i;
			return (0);
		}
		else {
			out[i] = b.name;
			i++;
			out[i] = ' ';
			i++;
			stack = stack->previous;
			*j = i;
			if (b.priority == 3)
				return (1);
		}
	}
	return (0);
}

