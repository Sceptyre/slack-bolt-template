from dotenv import load_dotenv
import os

global config

def init_config(env_file):    
    global config

    load_dotenv(env_file)

    config = {
        **os.environ
    }
