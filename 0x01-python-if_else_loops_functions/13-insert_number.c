#include "lists.h"
#include <stdlib.h>

/**
 * new_node - a function that creates a new node
 * @node: pointer to the current node
 * @number: number to be set
 * Return: a pointer to the new node
 */
listint_t *new_node(listint_t **node, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *temp;
	if (new == NULL)
		return (NULL);
	if (*node == NULL)
		new->next = NULL;
	else
	{
		temp = (*node)->next;
		(*node)->next = new;
		new->next = temp;
	}
	new->n = number;
	return (new);
}
/**
 * insert_node - a function that inserts a number into a sorted singly linked
 * list
 * @head: a pointer to the head node
 * @number: the number to be added
 * Return: a pointer to the new node, otherwise NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	if (head == NULL || *head == NULL)
	{
		*head = new_node(head, number);
		return (*head);
	}
	node = *head;
	if (number < node->n)
	{
		temp = (*head)->next;
		*head = new_node(&temp, number);
		return (*head);
	}
	while (node != NULL)
	{
		if ((number >= node->n && number <= node->next->n) ||
		    (node->next == NULL))
		{
			return (new_node(&node, number));
		}
		node = node->next;
	}
	return (NULL);
}
