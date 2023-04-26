import os

import github
import neon

if __name__ == '__main__':
    project = neon.find_project(os.environ['NEON_PROJECT'])
    primary_branch, branch = neon.find_branches(project, os.environ.get('NEON_BRANCH'))

    if not branch:
        branch = neon.create_branch(project, primary_branch, os.environ.get('NEON_BRANCH'))

    endpoint = neon.find_endpoint(project, branch)
    role = neon.find_role(project, branch)
    password = neon.get_password(project, branch, role)

    github.mask(endpoint['host'])
    github.mask(role['name'])
    github.mask(password)

    github.set_output('db_host', endpoint['host'])
    github.set_output('db_user', role['name'])
    github.set_output('db_password', password)
