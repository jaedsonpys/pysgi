from .response import Response


class DefaultResponses:
    bad_request = Response(
        body='<h1>Bad request<h1>',
        status=400
    )

    not_found = Response(
        body='<h1>Not found<h1>',
        status=404
    )

    method_not_allowed = Response(
        body='<h1>Method not allowed<h1>',
        status=405
    )
