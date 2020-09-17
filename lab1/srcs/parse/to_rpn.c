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

char	*get_arg(char *out, char * str, int *j, char del)
{
	char *index;
	char *b_out;
	int i;

	i = *j;
	index = ft_strrchr(str, del);
	if (index == (char*)0)
		ft_exit(INVALID_PARAMS_FUN);
	b_out = to_rpn(str, index);
	ft_strcpy(&out[i], b_out);
	i += ft_strlen(b_out);
	add_delim_out(out, &i);
	*j = i;
	return (index);
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
			str++;
		}
		if (flag)
		{
			out[i] = ' ';
			i++;
		}
		if (str != end && (op = is_op(*str)) != '\0')
		{
			flag = 1;
			if (check_op(op, &stack, out, &i))
			{
				str += 2; // skip l(
				str = get_arg(out, str, &i, ',') + 1;
				while (*str && (*str == ',' || *str == ' '))
					str++;
				str = get_arg(out, str, &i, ')') + 1;
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

