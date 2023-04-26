import os

import neon

if __name__ == '__main__':
    neon.delete_branch(
        neon.find_project(os.environ['NEON_PROJECT']),
        os.environ['NEON_BRANCH'],
    )
