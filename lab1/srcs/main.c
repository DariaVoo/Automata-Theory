//
// Created by snorcros on 9/16/20.
//
#include "rpn.h"

int	main(int argc, char **argv)
{
	char *out;
	double ans;

	if (argc != 2)
		ft_printf("Usage:%s\n", USAGE);
	out = to_rpn(argv[1], NULL);
	ft_printf("%s\n", out);
	ans = rpn_calc(out, NULL);
	printf("%f\n", ans);
	free(out);
	return (0);
}