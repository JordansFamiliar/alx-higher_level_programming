#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * rev_list - a helper function that reverses a linked list.
 * @node: a pointer to the starting node.
 * Return: a pointer to the new linked list.
 */
listint_t *rev_list(listint_t *node)
{
	listint_t *temp = NULL, *prev = NULL,
		*new_node = NULL;

	while (node != NULL)
	{
		temp = node->next;
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
		{
			while (prev != NULL)
			{
				temp = prev->next;
				free(prev);
				prev = temp;
			}
			return (NULL);
		}
		new_node->n = node->n;
		new_node->next = prev;
		prev = new_node;
		node = temp;
	}
	return (new_node);
}
/**
 * _free_list - a helper function to free a linked list.
 * @head: pointer to the head node.
 * Return: void
 */
void _free_list(listint_t *head)
{
	listint_t *temp = NULL;

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}
/**
 * is_palindrome - a function that checks if a singly
 * linked list is a palindrome
 * @head: pointer to the head node
 * Return: 0 if it is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *new = NULL, *temp = NULL;
	int i = 1, size = 1, mid = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (node->next != NULL)
	{
		size++;
		node = node->next;
	}
	if (size % 2 != 0)
		mid = ((size + 1) / 2) + 1;
	else
		mid = (size / 2) + 1;
	node = *head;
	for (; i < mid; i++)
		node = node->next;
	temp = new = rev_list(node);
	node = *head;
	while (new != NULL)
	{
		if (new->n != node->n)
		{
			_free_list(temp);
			return (0);
		}
		node = node->next;
		new = new->next;
	}
	_free_list(temp);
	return (1);
}
