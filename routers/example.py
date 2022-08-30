from routers import BaseSlackRouter

from controllers import example

class ExampleRouter(BaseSlackRouter):
    CMD_BASE = "/hello"

    ROUTES={
        "world": example.cmd_hello_world
    }