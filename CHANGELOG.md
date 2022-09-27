# 1.0.0

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.0.0/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.0.0).

## Additions

- Handle all response and request headers;
- Get or set all cookies coming from the browser;
- Add or get the body of an HTTP response or request;
- Can get parameters from URL.

# 1.1.0

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.1.0/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.1.0).

## Aditions

- Adding `Response` class to create responses;
- Removing direct use of the "make_response" function;
- New docstring added to methods and functions;
- Formatting URL arguments.

## Corrections

- [6ca2ed7](https://github.com/jaedsonpys/pysgi/commit/6ca2ed75bc16d359f4ccff821f385b26b43d04ed) Assigning empty dictionary to "cookies" and "headers" attributes;
- [906bb0e](https://github.com/jaedsonpys/pysgi/commit/906bb0e2b4cb2f224afd294ea0515ee3d7667b79) Removing TABS and fixing conditions in _print.py;
- [379df60](https://github.com/jaedsonpys/pysgi/commit/379df6008970548ab6c8d4ed33441a66cbc53da4) Changing response log style.

# 1.2.0

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.0/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.0).

## Aditions

- Adding method name verification when registering a route;
- Adding functionality to get parameters of dynamic routes;
- Adding functionality to add dynamic routes;
- Plugin functionality for the application;
- Adding IPFilter plugin.

## Fix

- [ab0691`](https://github.com/jaedsonpys/pysgi/commit/ab06916fa6a01da13b3b85cb0feece69a352ea34) Moving routes variable to PySGI class;
- [7c7d6a1](https://github.com/jaedsonpys/pysgi/commit/7c7d6a1ccfffc11eb4e14ab24480dc3b056c9479) Displaying query string in request log.
- [ef2d24b](https://github.com/jaedsonpys/pysgi/commit/ef2d24ba990dc486ee97891e2ea998922697ed50) Decoding the route path;
- [8652aeb](https://github.com/jaedsonpys/pysgi/commit/8652aeb37d4699fce95852128bf0db9e14b6cf29) Fixed data duplication errors.

# 1.2.1

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.1/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.1).

## Fix

- [3c1cad2](https://github.com/jaedsonpys/pysgi/commit/3c1cad227e1015993f3e5b2568cd137543c767ad) Creating MANIFEST.in to include DESCRIPTION.md file;

# 1.2.2

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.2/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.2).

## Fix

- [cf042a0](https://github.com/jaedsonpys/pysgi/commit/cf042a0): Improving condition structure in _request.py;
- [4e9bf1c](https://github.com/jaedsonpys/pysgi/commit/4e9bf1c): Renaming "wrapper" function to "decorator";
- [5e5241c](https://github.com/jaedsonpys/pysgi/commit/5e5241c): Using parentheses to format the return string from ClientRequest's `repr` method.

# 1.2.3

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.3/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.3).

## Fix

- [80d77e0](https://github.com/jaedsonpys/pysgi/commit/80d77e0): Fix argument name in decorator.

# 1.2.4

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.4/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.4).

## Fix

- [5fa8b6a](https://github.com/jaedsonpys/pysgi/commit/5fa8b6a): Using **HTTPPyParser** to get request data.

# 1.2.5

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.5/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.5).

## Fix

- [889f26d](https://github.com/jaedsonpys/pysgi/commit/889f26d): Updating version from HTTPPyParser;
- [8558055](https://github.com/jaedsonpys/pysgi/commit/8558055): Print full requested path in request log.

# 1.2.6

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.6/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.6).

## Fix

- [8da5670](https://github.com/jaedsonpys/pysgi/commit/8da5670): Fix `import error` adding version in setup.py.

# 1.2.7

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.7/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.7).

## Fix

- [f36386a](https://github.com/jaedsonpys/pysgi/commit/f36386a): Handle `InvalidHTTPMessageError` and returning bad request error.

# 1.2.8

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.8/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.8).

## Fix

- [d9b026d](https://github.com/jaedsonpys/pysgi/commit/d9b026d): Fixing `request.args` attribute to `request.query` in documentation;
- [077887b](https://github.com/jaedsonpys/pysgi/commit/077887b): Updating `http-pyparser` requirement version;
- [c9bda32](https://github.com/jaedsonpys/pysgi/commit/c9bda32): Changing `CHANGELOG.md` design.

# 1.2.9

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.9/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.9).

## Additions

- [9964efc](https://github.com/jaedsonpys/pysgi/commit/9964efc): Adding default error messages in **HTML**;
- [e8fdac4](https://github.com/jaedsonpys/pysgi/commit/e8fdac4): Changing start and response log message.

# 1.2.10

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.2.10/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.2.10).

## Improvements

- [533349b](https://github.com/jaedsonpys/pysgi/commit/533349b): Using `SocketHandler` instance as `PySGI` attribute;
- [65d8c37](https://github.com/jaedsonpys/pysgi/commit/65d8c37): Adding `client_host` attribute to request object;
- [739769f](https://github.com/jaedsonpys/pysgi/commit/739769f): Getting `client_host` in IPFilter plugin;
- [f865e03](https://github.com/jaedsonpys/pysgi/commit/f865e03): Removing accepted methods list;
- [18ebbe7](https://github.com/jaedsonpys/pysgi/commit/18ebbe7): Creating `_routes` dict inside of instance;
- [a956f1c](https://github.com/jaedsonpys/pysgi/commit/a956f1c): Removing `use_environ` from `SocketHandler`;
- [31b4623](https://github.com/jaedsonpys/pysgi/commit/31b4623): Restructuring thread creating to handle requests;
- [ed8c1bc](https://github.com/jaedsonpys/pysgi/commit/ed8c1bc): End line with "\r\n" in HTTP message.

# 1.3.0

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.3.0/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.3.0).

## Features

- [087b7ef](https://github.com/jaedsonpys/pysgi/commit/087b7ef): Adding `RequestData` class to store request data;
- [b11b80a](https://github.com/jaedsonpys/pysgi/commit/b11b80a): Setting content type if the body is a dictionary or list;
- [bb90817](https://github.com/jaedsonpys/pysgi/commit/bb90817): Getting IP machine if host is `0.0.0.0`;
- [46a236e](https://github.com/jaedsonpys/pysgi/commit/46a236e): Adding error message if server cannot be started;

## Improvements

- [521343a](https://github.com/jaedsonpys/pysgi/commit/521343a): Adding `_get_route_response` method in Request;
- [f9e3a5e](https://github.com/jaedsonpys/pysgi/commit/f9e3a5e): Removing `send_response` method from `SocketHandler`;
- [1bf496b](https://github.com/jaedsonpys/pysgi/commit/1bf496b): Creating daemon threads to manage requests;
- [0683d35](https://github.com/jaedsonpys/pysgi/commit/0683d35): Removing `plugins` import.

# 1.3.1

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.3.1/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.3.1).

## Fixes

- [64ac964](https://github.com/jaedsonpys/pysgi/commit/64ac964): Adding `pysgi/utils` to packages in setup script.

# 1.3.2

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.3.2/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.3.2).

## Fixes

- [90fb4d1](https://github.com/jaedsonpys/pysgi/commit/90fb4d1): Fix None value to query, headers and cookies in `ResponseData`

# 1.3.3

Find this version on [**PyPI**](https://pypi.org/project/PySGI/1.3.3/) or in the releases on [**GitHub**](https://github.com/jaedsonpys/pysgi/releases/tag/1.3.3).

## Fixes

- [9b4bf50](https://github.com/jaedsonpys/pysgi/commit/9b4bf50): Fix `TypeError` in argument type.