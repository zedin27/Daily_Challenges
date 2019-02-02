/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   daily_36.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ztisnes <ztisnes@student.42.us.org>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/02 17:18:35 by ztisnes           #+#    #+#             */
/*   Updated: 2019/02/02 15:16:58 by ztisnes          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

typedef struct		s_tree
{
	void			*data; //FIXME
	int				val;
	struct s_tree	*left;
	struct s_tree	*right;
}					t_tree;

t_tree				*create_tree(int value)
{
	t_tree *root;

	root = malloc(sizeof(t_tree));
	root->val = value;
	root->left = NULL;
	root->right = NULL;
	return (root);
}

t_tree		*insert(t_tree *node, int key)
{
	if (node == NULL)
		return (create_tree(key));
	if (key < node->val)
		node->left = insert(node->left, key);
	else if (key > node->val)
		node->right = insert(node->right, key);
	return (node);
}

// void	inorder(t_tree *root) //left root right
// {
// 	if (!root)
// 		return ;
// 	inorder(root->left);
// 	printf("%d ", root->val);
// 	inorder(root->right);
// }
//
// void	postorder(t_tree *root) //left right root
// {
// 	if (!root)
// 		return ;
// 	postorder(root->left);
// 	postorder(root->right);
// 	printf("%d ", root->val);
// }
//
//
void	preorder(t_tree *root) //root left right
{
	if (!root)
		return ;
	printf("%d ", root->val);
	preorder(root->left);
	preorder(root->right);

}

int		second_largest(t_tree *node)
{
	int temp_1 = INT_MIN; //1st largest
	int temp_2 = INT_MIN; //2nd largest

	while (node != NULL)
	{
		if (temp_1 < node->val)
		{
			temp_2 = temp_1;
			temp_1 = node->val;
		}
		if ((node->val > temp_2) && (temp_1 != node->val))
			temp_2 = node->val;
		node = node->right ? node->right : node->left;
	}
	return (temp_2);
}

int		main(void)
{
	t_tree *node = NULL;
	node = insert(node, 30);
	node = insert(node, 10);
	node = insert(node, 3);
	node = insert(node, 1);
	node = insert(node, 50);
	node = insert(node, 49);
	preorder(node);
	printf("\n");
	printf("Second largest value is: %d\n", second_largest(node));
	return (0);

}
