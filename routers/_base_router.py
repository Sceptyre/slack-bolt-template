import slack_bolt

class BaseSlackRouter:
    ROUTES = {}
    ACTIONS = {}
    EVENTS = {}
    CMD_BASE = None
    MIDDLEWARES = []

    def __init__(self, app :slack_bolt.App) -> None:
        # Map data
        self.app = app

        # Define command routing
        if self.CMD_BASE:
            self.app.command(command=self.CMD_BASE, middleware=self.MIDDLEWARES)(self._route)

        # Define action and view routing
        self._map_actions()
        self._map_events()

    def _route(self, ack, say, respond, command, client) -> None:
        # Acknowledge
        ack()

        # Grab a "default" value to run function
        func = self.ROUTES.get("")

        # Route based on first segment of command or if no route found fail to default
        for route in self.ROUTES.keys():
            if command['text'].startswith(route):
                func = self.ROUTES[route]

        # Error if func is null
        if not func:
            raise ValueError(f"No Route Found For Requested Command: {command['command']} {command['text']}")
        else:
            func(
                say=say,
                respond=respond,
                command=command,
                client=client
            )

    def _map_actions(self) -> None:
        # For each defined view
        for action in self.ACTIONS.keys():

            # Route to defined view function
            self.app.view(action)(self.ACTIONS[action])

    def _map_events(self) -> None:
        # For each defined view
        for event in self.EVENTS.keys():
            # Route to defined view function
            self.app.event(event)(self.EVENTS[event])
