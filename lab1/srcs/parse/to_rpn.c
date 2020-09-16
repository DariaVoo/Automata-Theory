#include "rpn.h"

char *to_rpn(char *str)
{
	int i;
	char *out;
	t_stack_op *stack;
	t_operation *op;

	i = 0;
	stack = NULL;
	out = ft_strnew(ft_strlen(str));
	while (*str)
	{
		if (is_digit(*str) || (*str == '-' && is_digit(*(str + 1))  || (*str == '.' && is_digit(*(str + 1)))))
		{
			while (*str != ' ' && *str)
			{
				out[i] = *str;
				i++;
				str++;
			}
		}
		else if ((op = is_op(*str)) != '\0')
		{
			if (!stack)
				push_op(&stack, op);
			if (check_op(op, stack, out, &i))
			{
				*str += 2; // skip l(
				char *a_out = to_rpn(ft_strcat(*str, ','));
				char *b_out = to_rpn(ft_strcat(*str, ')'));
				//Записываем две эти строки в out разделяя _ и заканчивая op.name

			}
			*str++;
		}
		else
		{
			ft_exit(INVALID_INPUT);
			return (NULL);
		}

	}

}

