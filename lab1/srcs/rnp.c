#include "rpn.h"

int is_digit(char x)
{
	return (x >= '0' && x <= '9' || x == '.');
}

int is_op_(char x)
{
	return (x == '+' || x == '-' || x == '*' || x == '/' || x == '%' || x == 'l');
}

double	do_op(double *cur, char op)
{
	double a = *cur;
	double b = *(cur + 1);

	if (op == '+')
		*cur = a + b;
	else if (op == '-')
		*cur = a - b;
	else if (op == '*')
		*cur = a * b;
	else if (b == 0)
		return (-1);
	else if (op == '/')
		*cur = a / b;
	else if (op == '%')
		*cur = (int)a % (int)b;
	return (0);
}

int	rpn_calc(char *str)
{
	double num[4096];
	int i = -1;

	while (*str)
	{
		if (is_digit(*str) || (*str == '-' && is_digit(*(str + 1))))
		{
			num[++i] = atof(str);
			if (*str == '-')
				++str;
			while (*str != ' ' && *str)
				++str;
		}
		else if (is_op_(*str) && i > 0)
		{
			--i;
			if (do_op(num + i, *str) == -1)
				return (-1);
			++str;
		}
		if (*str != '\0' && *str != ' ')
			return (-1);
		while (*str != '\0' && *str == ' ')
			++str;
	}

	if (i != 0)
		return (-1);
	printf("%f\n", num[i]);
	return (0);
}

int	main(int ac, char **av)
{
	if (ac != 2 || rpn_calc(av[1]) == -1)
		printf("Error\n");
	return (0);
}



