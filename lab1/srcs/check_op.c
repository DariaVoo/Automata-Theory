//
// Created by snorcros on 9/10/20.
//
#include "rpn.h"

void check_op(t_operation a, t_stack_op *stack, char *out, int i)
{
	t_operation b;

	b = *stack;
	while (a.priority <= b.priority)
	{
		if (b.name == ')')
		{
			while (b.name != '(')
			{
				out[i] = b.name;
				i++;
				out[i] = ' ';
				i++;
				stack = stack.previous;
			}
		}
		else {
			out[i] = b.name;
			i++;
			out[i] = ' ';
			i++;
			stack = stack.previous;
		}
	}
}

