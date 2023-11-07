#include <stdlib.h>
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info -  function to print  basic info about Python lists
 *
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *item;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
	item = PyList_GetItem(p, i);
	printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
