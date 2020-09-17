//
// Created by snorcros on 9/10/20.
//
#include "rpn.h"

int check_op(t_operation *a, t_stack_op **stack, char *out, int *j)
{
	t_operation b;
	int i;

	i = *j;
	if (*stack)
	{
		b = (*stack)->op;
		if (a->priority == 0) //if )
		{
			while (b.priority != -1 && *stack) // while not (
			{
				i = op_to_out(b.name, out, i);
				remove_op(stack);
				if (*stack)
					b = (*stack)->op;
			}
			if (b.name != '(')
				ft_exit(NO_OPEN_BRACKET);
			remove_op(stack);
			*j = i;
			return (0);
		}

		while (a->priority != -1 && a->priority <= b.priority && *stack)
		{
			i = op_to_out(b.name, out, i);
			remove_op(stack);
			*j = i;
			if (*stack)
				b = (*stack)->op;
		}
	}
	if (a->priority != 0) // не добавляем )
		push_op(stack, a);
	if (a->priority == 3)
	{
		i = op_to_out(a->name, out, i);
		remove_op(stack);
		*j = i;
		return (1);
	}

	return (0);
}

