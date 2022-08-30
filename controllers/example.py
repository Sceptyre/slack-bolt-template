import models.example as m_example
import views.example as v_example

def cmd_hello_world(say, respond, command, client):
    data = m_example.get_message()

    respond(
        v_example.render_message(data)
    )