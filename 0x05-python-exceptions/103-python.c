#include <stdio.h>
#include <Python.h>
#include <time.h>
/**
 * print_python_float - prints some basic info about Python float objects
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double float_value = 0;
	char *float_str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [Error] Invalid Float Object\n");
		return;
	}
	float_value = ((PyFloatObject *)p)->ob_fval;
	float_str = PyOS_double_to_string(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", float_str);
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, a = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [Error] Invalid Bytes Codes\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (a < size + 1 && a < 10)
	{
		printf(" %02hhx", string[a]);
		a++;
	}
	printf("\n");
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	/* A Py_ssize_t variable to store the size of the Python list*/
	/* A PyObject pointer used to iterate over the elements of the list */
	Py_ssize_t list_size = 0;
	PyObject *list_element;
	int a = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		list_size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", list_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (a < list_size)
		{
			list_element = PyList_GET_ITEM(p, a);
			printf("Element %d: %s\n", a, list_element->ob_type->tp_name);
			if (PyBytes_Check(list_element))
				print_python_bytes(list_element);
			else if (PyFloat_Check(list_element))
				print_python_float(list_element);
			a++;
		}
	}
	else
		printf("  [Error] InvalidList Object\n");
}
