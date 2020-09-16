//
// Created by snorcros on 9/10/20.
//
#include "rpn.h"

int check_op(t_operation *a, t_stack_op *stack, char *out, int *j)
{
	t_operation b;
	int i;

	i = *j;
	b = stack->op;
	while (a->priority <= b.priority)
	{
		if (b.name == ')')
		{
			while (b.name != '(')
			{
				out[i] = b.name;
				i++;
				out[i] = ' ';
				i++;
				stack = stack->previous;
			}
		}
		else {
			out[i] = b.name;
			i++;
			out[i] = ' ';
			i++;
			stack = stack->previous;
			if (b.priority == 3)
				return (1);
		}
	}
	*j = i;
	return (0);
}

