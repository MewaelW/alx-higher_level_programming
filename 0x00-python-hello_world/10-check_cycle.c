#include "lists.h"
/**
 * check_cycle - This function checks if a singly linked list has
 * a cycle in it
 * @list: pointer
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *p;
	listint_t *prev;

	p = list;
	prev = list;
	while (list && p && p->next)
	{
		list = list->next;
		p = p->next->next;

		if (list == p)
		{
			list = prev;
			prev =  p;
			while (1)
			{
				p = prev;
				while (p->next != list && p->next != prev)
				{
					p = p->next;
				}
				if (p->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
