# PySGI Library - Fast and simple ⚡️

PySGI is a WSGI library that allows you to receive and handle `HTTP requests`, giving access to various features, such as:

- Handle all response and request headers;
- Get or set all cookies coming from the browser;
- Add or get the body of an HTTP response or request;
- Can get parameters from URL;
- Get values ​​from a dynamic route.

## Example of use

Here's a brief demonstration of using the PySGI library to create a simple web server:

```python
from pysgi import PySGI

server = PySGI()


@server.route('/')
def index():
    return 'Hello World from PySGI!'


if __name__ == '__main__':
    server.run()

```

> You can find this usage example in `./examples/simple_server.py`

When creating a route, you can define the methods that are accepted by the route, being able to know which method was requested by the **request object**, which is passed as an argument to the function that was called (in this case, the `index()`)