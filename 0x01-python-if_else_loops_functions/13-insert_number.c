#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"
/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: linked list
 *@number: to be inserted
 *
 *Return: pointer to the new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (curr && curr->n < number)
		{
			tmp = curr;
			curr = curr->next;
		}
		tmp->next = new;
		new->next = curr;
	}
	return (new);
}
