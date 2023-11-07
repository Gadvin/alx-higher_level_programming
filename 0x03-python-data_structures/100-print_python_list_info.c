#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#include <time.h>

/**
 * print_python_list_info -  function to print  basic info about Python lists
 *
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, i;

	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < list_size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
}
