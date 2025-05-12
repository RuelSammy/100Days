#include <Python.h>

// Function to add two numbers
static PyObject* my_add(PyObject* self, PyObject* args) {
    int a, b;
    
    // Parse the input tuple
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }

    // Return the sum as a Python integer
    return PyLong_FromLong(a + b);
}

// Method definitions
static PyMethodDef MyMethods[] = {
    {"add", my_add, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "my_module",   // Module name
    NULL,          // Module documentation
    -1,            // Size of per-interpreter state of the module
    MyMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_my_module(void) {
    return PyModule_Create(&mymodule);
}
