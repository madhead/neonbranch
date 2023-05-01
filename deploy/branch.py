#!/usr/bin/env python3
import os
import time

import requests

base_url = 'https://console.neon.tech/api/v2'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {os.environ["NEON_TOKEN"]}'
}


def find_project(project_name: str) -> dict:
    projects = requests.get(
        url=f"{base_url}/projects",
        headers=headers,
    ).json()['projects']

    return next(project for project in projects if project['name'] == project_name)


def find_branches(project: dict, name: str) -> (dict, dict):
    branches = requests.get(
        url=f"{base_url}/projects/{project['id']}/branches",
        headers=headers,
    ).json()['branches']

    primary_branch = next(branch for branch in branches if branch['primary'])
    if name:
        branch = next((branch for branch in branches if branch['name'] == name), None)
    else:
        branch = primary_branch

    return primary_branch, branch


def get_operation_details(project: dict, operation_id: str) -> dict:
    return requests.get(
        url=f"{base_url}/projects/{project['id']}/operations/{operation_id}",
        headers=headers,
    ).json()['operation']


def create_branch(project: dict, parent: dict, name: str) -> dict:
    result = requests.post(
        url=f"{base_url}/projects/{project['id']}/branches",
        headers=headers,
        json={
            'endpoints': [
                {
                    'type': 'read_write'
                }
            ],
            'branch': {
                'parent_id': parent['id'],
                'name': name,
            }
        },
    ).json()
    operations = result['operations']

    for operation in operations:
        while True:
            operation_details = get_operation_details(project, operation['id'])
            if operation_details['status'] == 'finished':
                break
            else:
                time.sleep(5)

    return result['branch']


def find_endpoint(project: dict, branch: dict) -> dict:
    endpoints = requests.get(
        url=f"{base_url}/projects/{project['id']}/endpoints",
        headers=headers,
    ).json()['endpoints']

    return next(endpoint for endpoint in endpoints if endpoint['branch_id'] == branch['id'])


def find_role(project: dict, branch: dict) -> dict:
    roles = requests.get(
        url=f"{base_url}/projects/{project['id']}/branches/{branch['id']}/roles",
        headers=headers,
    ).json()['roles']

    return next(role for role in roles if not role['protected'])


def get_password(project: dict, branch: dict, role: dict) -> str:
    return requests.get(
        url=f"{base_url}/projects/{project['id']}/branches/{branch['id']}/roles/{role['name']}/reveal_password",
        headers=headers,
    ).json()['password']


def mask(value: str):
    print(f"::add-mask::{value}")


def set_output(name: str, value: str):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as github_output:
        print(f'{name}={value}', file=github_output)


if __name__ == '__main__':
    project = find_project(os.environ['NEON_PROJECT'])
    primary_branch, branch = find_branches(project, os.environ.get('NEON_BRANCH'))

    if not branch:
        branch = create_branch(project, primary_branch, os.environ.get('NEON_BRANCH'))

    endpoint = find_endpoint(project, branch)
    role = find_role(project, branch)
    password = get_password(project, branch, role)

    mask(endpoint['host'])
    mask(role['name'])
    mask(password)

    set_output('db_host', endpoint['host'])
    set_output('db_user', role['name'])
    set_output('db_password', password)
