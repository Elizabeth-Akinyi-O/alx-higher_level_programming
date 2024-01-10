#include "lists.h"
#include <stdio.h>

/*rev - reverse && comp - compare*/
void rev(listint_t **head);
int comp_lists(listint_t *head, listint_t *mid, int len);
/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: pointer to pointer of the first node
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *temp, *mid;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	mid = *head;

	for (len = 0; temp != NULL; len++)
		temp = temp->next;

	len = len / 2;

	for (i = 1; i < len; i++)
		mid = mid->next;
	if (len % 2 != 0 && len != 1)
	{
		mid = mid->next;
		len = len - 1;
	}
	rev(&mid);
	i = comp_lists(*head, mid, len);
	return (i);
}

/**
 * comp_lists - compares 2 lists
 * @head: pointer to the head node
 * @mid: pointer to the middle node
 * @len: length of the list 
 *
 *Return: 1 if same, 0 if not
 */
int comp_lists(listint_t *head, listint_t *mid, int len)
{
	int a;

	if (head == NULL || mid == NULL)
		return (1);
	for (a = 0; a < len; a++)
	{
		if (head->n != mid->n)
			return (0);
		head = head->next;
		mid = mid->next;
	}
	return (1);
}

/**
 * rev - reverses a list
 * @head: pointer to the head to reverse
 */
void rev(listint_t **head)
{
	listint_t *curr, *next, *prev;/*curr - current, prev - previous*/

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	curr = *head;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
}
