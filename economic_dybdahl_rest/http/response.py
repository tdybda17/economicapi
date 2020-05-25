from collections import namedtuple

HttpResponse = namedtuple(
    "HttpResponse",
    "http_status "
    "message "
    "data "
)

BadRequest = RuntimeError()
