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
    branch = next((branch for branch in branches if branch['name'] == name), None)

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


if __name__ == '__main__':
    print("NEON_BRANCH:")
    print(os.environ['NEON_BRANCH'])

    project = find_project(os.environ['NEON_PROJECT'])
    primary_branch, branch = find_branches(project,
                                           os.environ['NEON_BRANCH'])  # TODO: What id it's main branch? Non PR?

    if not branch:
        branch = create_branch(project, primary_branch, os.environ['NEON_BRANCH'])

    print(branch)
