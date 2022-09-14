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

## **1.2.1**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.1)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.1/)

### Fix

- [`3c1cad2`](https://github.com/jaedsonpys/pysgi/commit/3c1cad227e1015993f3e5b2568cd137543c767ad) Creating MANIFEST.in to include DESCRIPTION.md file;

## **1.2.2**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.2)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.2/)

### Fix

- [`cf042a0`](https://github.com/jaedsonpys/pysgi/commit/cf042a0): Improving condition structure in _request.py;
- [`4e9bf1c`](https://github.com/jaedsonpys/pysgi/commit/4e9bf1c): Renaming "wrapper" function to "decorator";
- [`5e5241c`](https://github.com/jaedsonpys/pysgi/commit/5e5241c): Using parentheses to format the return string from ClientRequest's `repr` method.

## **1.2.3**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.3)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.3/)

### Fix

- [`80d77e0`](https://github.com/jaedsonpys/pysgi/commit/80d77e0): Fix argument name in decorator.

## **1.2.4**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.4)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.4/)

### Fix

- [`5fa8b6a`](https://github.com/jaedsonpys/pysgi/commit/5fa8b6a): Using **HTTPPyParser** to get request data.

## **1.2.5**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.5)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.5/)

### Fix

- [`889f26d`](https://github.com/jaedsonpys/pysgi/commit/889f26d): Updating version from HTTPPyParser;
- [`8558055`](https://github.com/jaedsonpys/pysgi/commit/8558055): Print full requested path in request log.

## **1.2.6**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.6)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.6/)

### Fix

- [`8da5670`](https://github.com/jaedsonpys/pysgi/commit/8da5670): Fix `import error` adding version in setup.py.

## **1.2.7**

- [GitHub Release](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.7)
- [PyPI Release](https://pypi.org/project/PySGI/1.2.7)

### Fix

- [`f36386a`](https://github.com/jaedsonpys/pysgi/commit/f36386a): Handle `InvalidHTTPMessageError` and returning bad request error.