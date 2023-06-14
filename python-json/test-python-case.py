import subprocess

# Define the Postman collection file and environment file paths
collection_file = 'Collections/test-collection.json'
environment_file = 'local_env.json'
global_file = 'global_env.json'

newman_command = f'newman run {collection_file} -e {environment_file} -g {global_file}'

subprocess.run(newman_command, shell=True, check=True)
