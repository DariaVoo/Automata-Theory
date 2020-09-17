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

int check_op(t_operation *a, t_stack_op **stack, char *out, int *j)
{
	t_operation b;
	int i;

	i = *j;
	if (!*stack)
		return (0);
	b = (*stack)->op;

	if (a->priority == 0) //if )
	{
		while (b.priority != -1 && *stack) // while not (
		{
			i = op_to_out(b.name, out, i);
			remove_op(stack);
			b = (*stack)->op;
		}
		if (b.name != '(')
			ft_exit(NO_OPEN_BRACKET);
		remove_op(stack);
		*j = i;
		return (0);
	}

	while (a->priority != -1&& a->priority <= b.priority && *stack)
	{
		i = op_to_out(b.name, out, i);
		remove_op(stack);
		*j = i;
		if (b.priority == 3)
			return (1);
		if (*stack)
			b = (*stack)->op;
	}

	if (a->priority != 0) // не добавляем )
		push_op(stack, a);

	return (0);
}

