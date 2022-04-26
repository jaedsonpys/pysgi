# PySGI Library - Fast and simple ⚡️

![PySGI logo](https://github.com/jaedsonpys/pysgi/blob/master/docs/assets/img/logo.png)

PySGI is a WSGI library that allows you to receive and handle `HTTP requests`, giving access to various features, such as:

- Handle all response and request headers;
- Get or set all cookies coming from the browser;
- Add or get the body of an HTTP response or request;
- Can get parameters from URL;
- Get values ​​from a dynamic route.

## Links

- [PyPI Project](https://pypi.org/project/PySGI)
- [PySGI Docs](https://jaedsonpys.github.io/pysgi)

## Initializing

The PySGI library is available for installation on PyPI. Use this command to install the latest version:

```
pip install PySGI 
```

If you prefer, you can install manually by cloning the repository and running the following commands:

```
git clone git@github.com:jaedsonpys/pysgi.git
python3 setup.py sdist
pip install dist/PySGI-{last version}.tar.gz
```

Remember to replace "{last version}" with the current version of the project.

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

# Documentation

Access the full documentation:

- [PySGI use docs](https://jaedsonpys.github.io/pysgi/use)