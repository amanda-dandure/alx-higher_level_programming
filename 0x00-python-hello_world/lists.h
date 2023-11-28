#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - This is a singly linked list
 * @n: This is the int
 * @next: This points to the next node
 * Decription: This is a singly linked list node structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

#endif /* LISTS_H */
