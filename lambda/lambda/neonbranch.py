import json
import os
import re

import psycopg

path_regex = re.compile("^/(?P<player_1>[^/]+)/(?P<player_2>[^/]+)/?$")


def handle(event: dict, context):
    match = path_regex.match(event["requestContext"]["http"]["path"])

    if not match:
        return {
            "statusCode": 404,
        }

    player_1 = match.group("player_1")
    player_2 = match.group("player_2")
    # It's not recommended to cache Neon connections, as they may be closed.
    connection = psycopg.connect(
        host=os.environ["DATABASE_HOST"],
        dbname=os.environ["DATABASE_DATABASE"],
        user=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
    )
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM rules WHERE player1=%s AND player2=%s;', (player_1, player_2))

    row = cursor.fetchone()

    if not row:
        return {
            "statusCode": 404,
        }

    winner = row[2]
    description = row[3]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({
            "player_1": player_1,
            "player_2": player_2,
            "winner": winner,
            "description": description,
        }),
    }
