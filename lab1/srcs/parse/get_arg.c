//
// Created by snorcros on 9/16/20.
//
#include "rpn.h"

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
