"""PySGI is a simple and fast server library, giving access
to all the necessary HTTP information such as headers,
cookies, requested path and method, and other functionality.

With it, you can easily create complex and fast servers,
see an example:

```python
from pysgi import PySGI

server = PySGI()


@server.route('/')
def index():
     return 'Hello World from PySGI!'

server.run()
```

Access our official repository and get more information.
"""

from .wsgi import PySGI
from .response import Response
from .plugins import *

__version__ = '1.2.2'
