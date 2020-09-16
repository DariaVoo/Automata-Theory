#include rpn.h

char *to_rpn(char *str)
{
	int i;
	char out[ft_strlen(str)];
	t_stack_op *stack;
	t_operation op;

	i = 0;
	stack = NULL;
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
		else if ((op = is_op(*str)) != NULL)
		{
			if (!stack)
				push_op(&stack, op);
			check_op(op, *stack);
			*str++;
		}

	}

}

int	main(int ac, char **av)
{
	if (ac != 2 || rpn_calc(av[1]) == -1)
		printf("Error\n");
	return (0);
}