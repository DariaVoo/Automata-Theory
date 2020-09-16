//
// Created by snorcros on 9/10/20.
//

void		push_op(t_stack_op **begin_list, t_operation data)
{
	t_stack_op	*buff;

	buff = ft_create_stop(data);
	if (*begin_list != 0)
		buff->previous = *begin_list;
	*begin_list = buff;
}

t_stack_op	*create_stop(t_operation data)
{
	t_stack_op	*node;

	node = NULL;
	node = (t_stack_op*)malloc(sizeof(t_stack_op));
	if (node == NULL)
		return (node);
	node->op = data;
	node->previous = NULL;
	return (node);
}

void	remove_op(t_stack_op **op)
{
	t_stack_op *tmp;

	tmp = *op;
	*op = (*op)->previous;
	free(tmp);
}