#include "lists.h"

/**
 * check_cycle - a function that checks for a cycle in a linked list
 * @list: a pointer to a node on a linked list
 * Return: 0 if no cycle is found, 1 if a cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
