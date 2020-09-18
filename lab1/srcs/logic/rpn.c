#include "rpn.h"

int is_digit(char x)
{
	return (x >= '0' && x <= '9' || x == '.');
}

double	doo_op(double *cur, t_operation *op)
{
	double a = *cur;
	double b = *(cur + 1);

	if (op->priority != 3)
	{
		*cur = op->fun(a, b);
		return (*cur);
	}
}

double rpn_calc(char *str, char *end)
{
	double num[4096];
	t_operation *op;
	int i = -1;

	while (str && *str && str != end)
	{
		if (is_digit(*str) || (*str == '-' && is_digit(*(str + 1))))
		{
			num[++i] = atof(str);
			if (num[i] == 0 && *str != '0')
				ft_exit(INVALID_OPERAND);
			if (*str == '-')
				str++;
			while (*str != ' ' && *str)
				str++;
		}
		else if ((op = is_op(*str)) && (i > 0 || op->priority == 3))
		{
			i--;
			if (op->priority == 3)
			{
				str++;
				int a, b;

				if (i < 0)
					i = 0;
				a = get_arg(&str);
				b = get_arg(&str);
				num[i] = op->fun(a, b);
			}
			else
			{
				doo_op(num + i, op);
				str++;
			}
		}
		if (*str != '\0' && *str != ' ' && *str != '_')
			ft_exit(INVALID_INPUT);
		while (*str != '\0' && str != end && (*str == ' ' || *str == '_'))
			str++;
	}

	if (i != 0)
		ft_exit(MANY_OPERANDS);
	return (num[i]);
}