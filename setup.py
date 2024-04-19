import subprocess
from src.utils import load_config

#################################################################
    # Go and configure your config/llm.config.json file first.
#################################################################

config=load_config("config/project.config.json",verbose = True)
print("Loaded config/project.config.json file.")
env_lines = [f"{key}={value}" for key, value in config.items()]
with open(".env","w") as e:
    
    e.writelines(env_lines)

CMD="sudo export $(cat .env| xargs); env"

subprocess.call(CMD)
