#include "rpn.h"

void	add_delim_out(char *out, int *j)
{
	int i = *j;

	out[i] = '_';
	i++;
	out[i] = ' ';
	i++;
	*j = i;
}

char *to_rpn(char *str, char *end)
{
	int i;
	char *out;
	int	flag;
	t_stack_op *stack;
	t_operation *op;

	i = 0;
	stack = NULL;
	out = ft_strnew(ft_strlen(str));
	while (*str && str != end)
	{
		flag = 0;
		while (*str == ' ')
			str++;
		while (is_digit(*str) || (*str == '-' && is_digit(*(str + 1)))  || (*str == '.' && is_digit(*(str + 1))))
		{
			flag = 1;
			out[i] = *str;
			i++;
			out[i] = ' ';
			i++;
			str++;
		}
		if (str != end && (op = is_op(*str)) != '\0')
		{
			flag = 1;
			if (check_op(op, &stack, out, &i))
			{
				str += 2; // skip l(
				char *index;

				index = ft_strrchr(str, ',');
				if (index == (char*)0)
					ft_exit(INVALID_PARAMS_FUN);
				char *a_out = to_rpn(str, index);
				str = index;

				ft_strcpy(&out[i], a_out);
				i += ft_strlen(a_out);

				add_delim_out(out, &i);

				index = ft_strrchr(str, ')');
				while (*str && (*str == ',' || *str == ' '))
					str++;
				if (index == (char*)0)
					ft_exit(INVALID_PARAMS_FUN);
				char *b_out = to_rpn(str, index);

				ft_strcpy(&out[i], b_out);
				i += ft_strlen(b_out);
				str += ft_strlen(b_out) - 1;

				add_delim_out(out, &i);

			}
			str++;
		}
		if (!flag)
		{
			ft_exit(INVALID_INPUT);
			return (NULL);
		}
	}
	while (stack)
	{
		op_to_out((*stack).op.name, out, i);
		i++;
		remove_op(&stack);
	}
	return (out);
}

