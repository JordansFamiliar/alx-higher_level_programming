#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - a function that inserts a number into a sorted singly linked
 * list
 * @head: a pointer to the head node
 * @number: the number to be added
 * Return: a pointer to the new node, otherwise NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new_node, *temp;

	if (head == NULL || *head == NULL)
		return (NULL);
	node = *head;
	while (node != NULL)
	{
		if (number >= node->n && (node->next == NULL ||
					 number <= node->next->n))
		{
			new_node = malloc(sizeof(listint_t));
			if (new_node == NULL)
				return (NULL);
			temp = node->next;
			node->next = new_node;
			new_node->n = number;
			new_node->next = temp;
			return (new_node);
		}
		node = node->next;
	}
	return (NULL);
}
