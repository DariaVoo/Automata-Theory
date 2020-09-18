//
// Created by snorcros on 9/16/20.
//
#include "rpn.h"

int	main(int argc, char **argv)
{
	char *out;
	char *end;

	if (argc != 2)
		ft_printf("Usage:%s\n", USAGE);
	out = to_rpn(argv[1], NULL);
	ft_printf("%s\n", out);
//	rpn_calc(out);
	return (0);
}