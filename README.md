# PySGI Library

PySGI is a WSGI library that allows you to receive and handle `HTTP requests`, giving access to various features, such as:

- Handle all response and request headers;
- Get or set all cookies coming from the browser;
- Add or get the body of an HTTP response or request;
- Can get parameters from URL;
- Get values ​​from a dynamic route;
- Returning JSON and other data types.

You can learn how to use `PySGI` in the project's [official documentation](https://jaedsonpys.github.io/pysgi/). See [CHANGELOG.md](https://github.com/jaedsonpys/pysgi/blob/master/CHANGELOG.md) on GitHub for changes made to each release.

The PySGI library is available for installation on PyPI. Use this command to install the latest version:

```
pip install PySGI 
```

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

You can find this and other examples in the [example usage files](https://github.com/jaedsonpys/pysgi/tree/master/examples).

# License

```text
MIT License
Copyright (c) 2022 Jaedson Silva
```

See [LICENSE](https://github.com/jaedsonpys/pysgi/blob/master/LICENSE) file to learn more about the license.