#include "lists.h"

/**
 * insert_mode - insters a node in a linked list.
 * @head: beginning of linked list.
 * @number: value associatedwith node.
 * Return: address of new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t  *prevnode, *node, *nextnode = *head;


	node = malloc(sizeof(listint_t));

	if (node)
	{
		node->n = number;
		node->next = *head;

		if (!*head || number <= (*head)->n)
		{
			*head = node;
			return (node);
		}

		while (nextnode && nextnode->n < node->n)
		{
			prevnode = nextnode;
			nextnode = prevnode->next;
		}

		prevnode->next = node;
		node->next = nextnode;
	}

	return (node);


}
