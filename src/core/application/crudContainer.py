from src.infrastructure.container.docker_sdk import create as createDocker, delete as deleteDocker

def create(**kwargs):
    return createDocker(**kwargs)

def delete(id_or_name):
    return deleteDocker(id_or_name)