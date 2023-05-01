import os


def mask(value: str):
    print(f"::add-mask::{value}")


def set_output(name: str, value: str):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as github_output:
        print(f'{name}={value}', file=github_output)
