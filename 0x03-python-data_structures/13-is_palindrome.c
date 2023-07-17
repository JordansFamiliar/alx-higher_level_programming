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
	size_t i;
	char *num = NULL, temp[2];

	if (*head == NULL)
		return (1);
	while (node != NULL)
	{
		temp[0] = node->n + '0';
		temp[1] = '\0';
		if (num == NULL)
		{
			num = malloc(2 * sizeof(char));
			strcpy(num, temp);
		}
		else
		{
			num = realloc(num, (strlen(num) + 2) * sizeof(char));
			strcat(num, temp);
		}
		node = node->next;
	}
	for (i = 0; i <= strlen(num) - i - 1; i++)
	{
		if (num[i] != num[strlen(num) - i - 1])
		{
			free(num);
			return (0);
		}
	}
	free(num);
	return (1);
}
