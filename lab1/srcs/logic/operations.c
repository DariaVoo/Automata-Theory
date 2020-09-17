//
// Created by snorcros on 9/16/20.
//
#include "rpn.h"

double		ft_add(double a, double b)
{
	return (a + b);
}

double		ft_sub(double a, double b)
{
	return (a - b);
}

double		ft_mul(double a, double b)
{
	return (a * b);
}

double		ft_mod(double a, double b)
{
	int a_ = (int)a;
	int b_ = (int)b;

	if (b == 0)
	{
		ft_exit(ZERO_DIVISION);
		return (0);
	}
	else
		return (double )(a_ % b_);
}

double		ft_div(double a, double b)
{
	if (b == 0)
	{
		ft_exit(ZERO_DIVISION);
		return (0);
	}
	else
		return (a / b);
}

double		ft_log(double base, double b)
{
	double log_base;

	log_base = log(base);
	if (log_base == 0)
	{
		ft_exit(ZERO_DIVISION);
		return (0);
	}
	else
		return log(b) / log(base);
}