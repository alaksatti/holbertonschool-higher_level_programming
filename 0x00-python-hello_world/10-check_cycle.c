#include "lists.h"


int check_cycle(listint_t *list)
{

	listint_t *stepper = list, *skipper = list;

	while (stepper && skipper && skipper->next)
	{
		stepper = stepper->next;
		skipper = skipper->next->next;


		if (stepper == skipper)
			return (1);


	}

	return (0);
}
