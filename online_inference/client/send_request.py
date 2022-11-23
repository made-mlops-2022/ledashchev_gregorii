import requests
import json
import pandas as pd
import click


@click.command(name="send_request_to_api")
@click.argument('endpoint', default='health')
@click.argument('path_to_data', default='')
@click.argument('output', default='std')
def send_request_to_api(endpoint, path_to_data, output):
    url = f'http://127.0.0.1:80/{endpoint}'
    if endpoint == 'predict':
        data = pd.read_csv(rf'{path_to_data}').iloc[:3, :]
        sending_data = {"dataframe": data.to_json()}
        print(json.dumps(sending_data))
        post_request = requests.post(url, data=json.dumps(sending_data))
        data_to_print = str(post_request.text)[1: -1]
    elif endpoint == 'health':
        post_request = requests.post(url)
        data_to_print = post_request.text
    else:
        data_to_print = 'No such endpoint'

    if output == 'std':
        print(data_to_print)
    else:
        with open(output, 'w') as output_file:
            print(data_to_print, file=output_file)


if __name__ == '__main__':
    send_request_to_api()
