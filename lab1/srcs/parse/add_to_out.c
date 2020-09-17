//
// Created by snorcros on 9/17/20.
//
#include "rpn.h"

int op_to_out(char op_name, char *out, int i)
{
	out[i] = op_name;
	i++;
	out[i] = ' ';
	i++;
	return i;
}

void	add_delim_out(char *out, int *j)
{
	int i = *j;

	out[i] = '_';
	i++;
	out[i] = ' ';
	i++;
	*j = i;
}
