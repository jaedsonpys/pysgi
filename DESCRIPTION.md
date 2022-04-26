# PySGI Library, fast and simple

PySGI is a WSGI library that allows you to receive and handle `HTTP requests`, giving access to various features, such as:

- Handle all response and request headers;
- Get or set all cookies coming from the browser;
- Add or get the body of an HTTP response or request;
- Can get parameters from URL;
- Get values ​​from a dynamic route.

# How to use

This is the official documentation for using the `PySGI` library, here you will have the **first steps** to create a server using our library.

See [CHANGELOG.md](https://github.com/jaedsonpys/pysgi/blob/master/CHANGELOG.md) on GitHub for changes made to each release.

## Links

- [PySGI Library, fast and simple](#pysgi-library-fast-and-simple)
- [How to use](#how-to-use)
  - [Links](#links)
  - [Creating a server](#creating-a-server)
    - [class `PySGI()`](#class-pysgi)
    - [method `server.route()`](#method-serverroute)
    - [argument `index(request)`](#argument-indexrequest)
  - [Creating dynamic routes](#creating-dynamic-routes)
  - [Returns a response](#returns-a-response)
    - [Returning only the body](#returning-only-the-body)
    - [Returning the body and status of the request](#returning-the-body-and-status-of-the-request)
    - [Using `Response` class](#using-response-class)

## Creating a server

To create a server, you need to import the `PySGI` class and the `Response` class (if you need to define content type, cookies, or headers):

```python
from pysgi import PySGI
from pysgi import Response

server = PySGI()


@server.route('/', methods=['GET', 'POST'])
def index(request):
    return 'Hello World!'


server.run()
```

We just created a web server. Let's see the functionality of some functions and arguments:

### class `PySGI()`

The PySGI class has the necessary methods to create your application, being only two: `route()` and `run()`.

There, the routes created by you will also be registered.

### method `server.route()`

This method is responsible for registering new routes. A route name must always start with *"/"*, followed by the route name (eg `/about`).

The method has only two arguments, the first is `route`, which requires the name of the route, and the second is `methods`, which requires a list of methods accepted by this route. The default accepted method is **GET**, but you can define them in a list.

Method names must be defined in uppercase, for example: **GET**, **POST**, **PUT**, **DELETE** and others.

```python
@server.route('/user', methods=['DELETE', 'POST'])
```

### argument `index(request)`

The `request` argument has information about the client's request, such as headers, cookies, requested method and route, and URL arguments (or parameters).

This argument is `optional`, you can put it or not, if you need it, it will be available.

> A question... How does PySGI know if the request argument is there? Simple, with one exception, if the `TypeError` exception is thrown, we will try again to call the function, but without passing the argument.

You can access the data as you access an attribute (eg request.method). Cookies and headers are like dictionaries.

```python
request.body  # request body
request.path  # request path
request.parameters  # request parameters (to dynamic routes)
request.args  # request args
request.method  # request method
request.cookies  # request cookies
request.headers  # request headers
```

## Creating dynamic routes

To create a dynamic route, just inform the parameter name and its type (optional). This information must be enclosed in braces (<>).

```python
from pysgi import PySGI
from pysgi import Response

server = PySGI()


@server.route('/user/<str: username>', methods=['GET', 'POST'])
def index(request):
    return f'Hello, {request.parameters.get("username")}'


server.run()
```

If the defined parameter is not available, status code 404 will be returned.

## Returns a response

There are two three ways to return a response to the client, let's see some:

### Returning only the body

Use this only for simpler requests, the default HTTP status code will be 200.

```python
@server.route('/', methods=['GET', 'POST'])
def index(request):
    return 'Hello World'  # returning only the body
```

### Returning the body and status of the request
   
That way you can return the body and status of the request:

```python
@server.route('/', methods=['GET', 'POST'])
def index(request):
    return 'Hello World', 200  # returning the body and status
```

### Using `Response` class

Using this class you can have a much more detailed answer by setting body, cookies, headers, content type and status.

```python
@server.route('/', methods=['GET', 'POST'])
def index(request):
    return Response('Hello World', content_type='text/plain')
```

To set cookies and headers (setting their name and value):

```python
@server.route('/', methods=['GET', 'POST'])
def index(request):
    response = Response('Hello World', content_type='text/plain')

    # cookies
    response.set_cookie('Auth', 'utokenAuth123')

    # headers
    response.set_header('Authorization', 'utokenAuth123')

```