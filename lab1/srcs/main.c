//
// Created by snorcros on 9/16/20.
//
#include "rpn.h"

int	main(int argc, char **argv)
{
	char *out;
	char *end;


//	ft_printf("argc %d", argc);
	if (argc != 2)
		ft_printf("Usage:%s\n", USAGE);

//	end = argv[0] + ft_strlen(argv);
	out = to_rpn(argv[1], NULL);
	ft_printf("%s\n", out);
	return (0);
}