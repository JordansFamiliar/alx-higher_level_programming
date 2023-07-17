#include "lists.h"
#include <stdlib.h>
#include <string.h>
/**
 * is_palindrome - a function that checks if a singly
 * linked list is a palindrome
 * @head: pointer to the head node
 * Return: 0 if it is not a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head;
	size_t i = 0, size = 0;
	char *num = NULL, *start, *end;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (node != NULL)
	{
		size++;
		node = node->next;
	}
	num = malloc(size * sizeof(char));
	if (num == NULL)
		return (0);
	node = *head;
	while (node != NULL)
	{
		num[i] = node->n + '0';
		node = node->next;
		i++;
	}
	start = num;
	end = num + size - 1;
	while (start < end)
	{
		if (*start != *end)
		{
			free(num);
			return (0);
		}
		start++;
		end--;
	}
	free(num);
	return (1);
}
