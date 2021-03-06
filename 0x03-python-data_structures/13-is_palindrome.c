#include "lists.h"

/**
 * is_palindrome checks if a singly linked list is a palindrome or not.
 * @head: pointer to beginning of linked lists.
 * Returns: 0 if not, 1 if is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t  *reversed_list, *stepper = *head, *skipper = *head;

	if (!head)
		return (0);

	if (!*head || !(*head)->next)
		return (1);


	while(skipper->next && skipper->next->next)
	{
		stepper = stepper->next;
		skipper = skipper->next->next;
	}

	reversed_list = reverse(&stepper);

	while (*head && reversed_list)
	{
		if((*head)->n != reversed_list->n)
			return (0);

		*head = (*head)->next;
		reversed_list = reversed_list->next;
	}

	return (1);
}




listint_t *reverse(listint_t **head)
{
	listint_t *next, *prevnode = NULL;



	while (*head)
	{
		next = (*head)->next;

		(*head)->next = prevnode;

		prevnode = *head;

		*head = next;

	}

	*head = prevnode;

	return (*head);

}
