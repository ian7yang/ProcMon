import click
import requests
import json
import datetime

DEBUG = True
configs = json.loads(open('./config.json').read())

config = configs['development'] if DEBUG else configs['production']

headers = {'Authorization': f"Token {config['token']}"}


@click.command()
@click.option('--url', required=True, type=str, help='http(s)://example.com')
@click.option('--crawler', required=True, type=str,
              help='name of the crawler, e.g. theia-1')
@click.option('--user', required=True, type=str,
              help='current user, e.g. user-1')
def start(url, crawler, user):
    endpoint = config['host'] + config['progressAPI']
    data = {
        "user": user,
        "website": url,
        "created_by": crawler
    }
    r = requests.post(endpoint, json=data, headers=headers)
    if r.status_code == 201:
        ret = json.loads(r.text)
        # return the id of created record
        print(ret['id'])
    else:
        # -1 means error
        print(r.content)
        print(-1)


@click.command()
@click.option('--pk', required=True, type=str, help='e.g. 1')
@click.option('--is-successful', type=bool, help='e.g. 1 or 0')
@click.option('--is-complete', type=bool, help='e.g. 1 or 0')
@click.option('--file-path', type=str, help='e.g. /path/to/file')
def end(pk, is_successful, is_complete, file_path):
    endpoint = config['host'] + config['progressAPI']
    data = {
        "is_successful": is_successful,
        "is_complete": is_complete,
        "file_path": file_path,
        "complete_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    }
    r = requests.patch(f'{endpoint}{pk}/', json=data, headers=headers)
    if r.status_code == 200:
        ret = json.loads(r.text)
        # return the id of created record
        print(ret['id'])
    else:
        print(r.content)
        print(-1)


@click.group()
def cli():
    pass


if __name__ == '__main__':
    cli.add_command(start)
    cli.add_command(end)
    cli()