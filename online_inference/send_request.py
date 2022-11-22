import requests
import json
import pandas as pd
import click


@click.command(name="send_request_to_api")
@click.argument('path_to_data')
@click.argument('output', default='std')
def send_request_to_api(path_to_data, output='std'):
    url = 'http://127.0.0.1:8000/predict'
    data = pd.read_csv(rf'{path_to_data}')
    sending_data = {"dataframe": data.to_json()}
    post_request = requests.post(url, data=json.dumps(sending_data))
    if output == 'std':
        print(str(post_request.text)[1: -1])
    else:
        with open(output, 'w') as output_file:
            print(str(post_request.text[1: -1]), file=output_file)


if __name__ == '__main__':
    send_request_to_api()
