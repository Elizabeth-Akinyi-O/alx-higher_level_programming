#include "lists.h"
/*
 *check_cycle - checks if a singly linked list has a cycle in it
 *@list: linked list
 *
 *Return: 1 if there is a cycle and 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *is_fast, *is_slow;

	if (!list || !list->next)
		return (0);
	is_fast = list;
	is_slow = list;

	while (is_slow != NULL && is_fast != NULL && is_fast->next != NULL)
	{
		is_slow = is_slow->next;
		is_fast = is_fast->next->next;
		if (is_slow == is_fast)
		{
			return(1);
		}
	}
	return (0);
}
