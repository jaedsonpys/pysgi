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

## **1.2.0**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.0)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.0/)

### Aditions

- Adding method name verification when registering a route;
- Adding functionality to get parameters of dynamic routes;
- Adding functionality to add dynamic routes;
- Plugin functionality for the application;
- Adding IPFilter plugin.

### Fix

- [`ab06916`](https://github.com/jaedsonpys/pysgi/commit/ab06916fa6a01da13b3b85cb0feece69a352ea34) Moving routes variable to PySGI class;
- [`7c7d6a1`](https://github.com/jaedsonpys/pysgi/commit/7c7d6a1ccfffc11eb4e14ab24480dc3b056c9479) Displaying query string in request log.
- [`ef2d24b`](https://github.com/jaedsonpys/pysgi/commit/ef2d24ba990dc486ee97891e2ea998922697ed50) Decoding the route path;
- [`8652aeb`](https://github.com/jaedsonpys/pysgi/commit/8652aeb37d4699fce95852128bf0db9e14b6cf29) Fixed data duplication errors.