#include "lists.h"
/**
* check_cycle - checks for acycle in a linked list.
*
* @list: The head pointer to be checked.
*
*Return: if cycle present 1 else 0.
*/

int check_cycle(listint_t *list)
{
listint_t *hare, *turtle;

if (list == NULL || list->next == NULL)

return (0);
turtle = list->next;
hare = list->next->next;

while (turtle && hare && hare->next)
{
if (turtle == hare)
return (1);

turtle = turtle->next;
hare = hare->next->next;
}
return (0);
}
