#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *last = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		if (current->next != NULL && current->next->next != NULL)
		{
			current = current->next->next;
			last = last->next;

			if (current == last)
			{
				return (1);
			}
		}
		else
			return (0);
	}
}
