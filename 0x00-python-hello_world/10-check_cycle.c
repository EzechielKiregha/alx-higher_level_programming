#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *actual_node, *node_check;

	if (list == NULL || list->next == NULL)
		return (0);
	actual_node = list;
	node_check = actual_node->next;

	while (actual_node != NULL && node_check->next != NULL
			&& node_check->next->next != NULL)
	{
		if (actual_node == node_check)
			return (1);
		actual_node = actual_node->next;
		node_check = node_check->next->next;
	}
	return (0);
}
