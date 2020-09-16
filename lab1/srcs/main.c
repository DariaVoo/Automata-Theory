//
// Created by snorcros on 9/16/20.
//
#include "rpn.h"

int	main(int ac, char **av)
{
	if (ac != 2 || rpn_calc(av[1]) == -1)
		printf("Error\n");
	return (0);
}