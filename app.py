#!/usr/bin/env python
# Init Configuration Must be before remaining imports in case they utilize the config
import os
from lib.config import init_config
init_config(".env")

# Import necessary modules/resources
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import routers
import middleware
from lib import db

# Initialize app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"), )

# Map routes
routers.ExampleRouter(app)

# Error & Log Handler
app.use(middleware.log_handler)
app.error(middleware.error_handler)

# Init External/Integrations/Databases
db.init_database()

# Start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
