#include "lists.h"

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_list - Function to Reverse a singly-linked list
 * @head: A pointer to the starting node
 *
 * Return:Pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - funtion to Check if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 *
 * Return: If the linked list is not a palindrome - 0
 *         If the linked list is a palindrome - 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *revised, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	revised = reverse_list(&tmp);
	middle = revised;

	tmp = *head;
	while (revised)
	{
		if (tmp->n != revised->n)
			return (0);
		tmp = tmp->next;
		revised = revised->next;
	}
	reverse_list(&middle);

	return (1);
}
