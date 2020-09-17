#include "rpn.h"

char *to_rpn(char *str, char *end)
{
	int i;
	char *out;
	t_stack_op *stack;
	t_operation *op;

	i = 0;
	stack = NULL;
	out = ft_strnew(ft_strlen(str));
	while (*str && str != end)
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
				char *index;

				index = ft_strrchr(str, ',');
				if (index == (char*)0)
					ft_exit(INVALID_PARAMS_FUN);
				char *a_out = to_rpn(str, index);
				str = index;

				ft_strcpy(&out[i], a_out);
				i += ft_strlen(a_out);
				out[i] = '_';
				i++;

				index = ft_strrchr(str, ',');
				if (index == (char*)0)
					ft_exit(INVALID_PARAMS_FUN);
				char *b_out = to_rpn(str, index);

				ft_strcpy(&out[i], b_out);
				i += ft_strlen(a_out);
			}
			*str++;
		}
		else
		{
			ft_exit(INVALID_INPUT);
			return (NULL);
		}

	}
	return (out);
}

