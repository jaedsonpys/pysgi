# Version 1

## **1.0.0**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.0.0)
- [PyPI Release](https://pypi.org/project/PySGI/1.0.0/)

### Additions

- Handle all response and request headers;
- Get or set all cookies coming from the browser;
- Add or get the body of an HTTP response or request;
- Can get parameters from URL.

## **1.1.0**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.1.0)
- [PyPI Release](https://pypi.org/project/PySGI/1.1.0/)

### Aditions

- Adding `Response` class to create responses;
- Removing direct use of the "make_response" function;
- New docstring added to methods and functions;
- Formatting URL arguments.

### Corrections

- [`6ca2ed7`](https://github.com/jaedsonpys/pysgi/commit/6ca2ed75bc16d359f4ccff821f385b26b43d04ed) Assigning empty dictionary to "cookies" and "headers" attributes;
- [`906bb0e`](https://github.com/jaedsonpys/pysgi/commit/906bb0e2b4cb2f224afd294ea0515ee3d7667b79) Removing TABS and fixing conditions in _print.py;
- [`379df60`](https://github.com/jaedsonpys/pysgi/commit/379df6008970548ab6c8d4ed33441a66cbc53da4) Changing response log style.