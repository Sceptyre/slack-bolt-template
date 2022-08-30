import views.error as v_error
from datetime import datetime

def error_handler(error, client, context, logger, body):
    logger.error(f"User {body.get('user_name')} caused error: {error}")

    client.chat_postEphemeral(        
        text=v_error.error_response(error),
        channel=context["user_id"],
        user=context["user_id"]
    )