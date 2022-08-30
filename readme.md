# Template for basic slack app following MVC architecture


## Utilities

### MVC
Model - Data interactions  
View - Rendering/presentation interactions  
Controller - Interactions between Model and View

#### Controller File:
controller/example.py
```py
import models.example as m_example
import views.example as v_example

def cmd_hello_world(**kwargs):
    # Get Data
    data = m_example.get_data()

    # Return Renderered Data
    return v_example.render_data(data)
```

### routers.BaseSlackRouter
Standardizes routing for events, commands, views etc. Helps simplify creating new ones  
Calling in base app.py is as simple as:
```py
routers.NameOfRouter(app)
```


### lib.config
Centralises config into a single lib to allow adding a config file in the future etc that can be referenced in other locations  
Can be sourced with 
```py
from lib.config import config
```

### Lib
Home for external services or objects that multiple services will need  
ex. Database Objects, Configs, APIs, etc