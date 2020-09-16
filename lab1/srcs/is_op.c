//
// Created by snorcros on 9/10/20.
//
#include "rpn.h"

t_operation *is_op(char x)
{
	int i;

	i = 0;
	while (g_opp[i].name != '\0')
	{
		if (x == g_opp[i].name)
			return (g_opp[i]);
		i++;
	}
	return (NULL);
}