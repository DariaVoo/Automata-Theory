/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snorcros <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/09/17 12:25:50 by snorcros          #+#    #+#             */
/*   Updated: 2020/09/17 13:54:53 by snorcros         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_strirchr(const char *s, int c)
{
	int	occur;
	int	i;

	i = 0;
	occur = -1;
	while (*s != '\0')
	{
		if (*s == (char)c)
			occur = i;
		s++;
		i++;
	}
	if (!c && !*s)
		return (-1);
	return (occur);
}