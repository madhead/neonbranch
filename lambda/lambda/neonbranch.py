from . import env


def handle(event: dict, context):
    return event | {'env': env}
