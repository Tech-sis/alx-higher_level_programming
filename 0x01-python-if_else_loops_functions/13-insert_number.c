#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inset a number into a sorted linked list 
 * 
 * @head: pointer to node
 * @number: number to inset 
 * Return: listint_t* 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
			return (NULL);
	
	new->n = number;

	if (*head == NULL)
			*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
					break;

			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}