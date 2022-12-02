import inspect
import os.path
import re

import requests

from utils import secrets


def _extract_path_day_part(calling_frame):
    module = inspect.getmodule(calling_frame[0])
    module_name = os.path.basename(module.__file__)
    module_path = os.path.dirname(module.__file__)
    matches = re.match(r'd(\d{1,2})p([12])\.py', module_name)
    return module_path, int(matches.group(1)), int(matches.group(2))


def fetch_input():
    calling_frame = inspect.stack()[1]
    day_path, day, part = _extract_path_day_part(calling_frame)
    input_file = os.path.join(day_path, 'input.txt')
    if os.path.exists(input_file):
        print(f'## [INFO] reading cached input from {input_file}')
        with open(input_file, 'r') as f:
            text = f.read()
    else:
        url = f'https://adventofcode.com/2022/day/{day}/input'
        cookies = {
            "session": secrets.SESSION,
        }
        print(f'## [WARN] fetching input from {url}')
        response = requests.get(url, cookies=cookies)
        text = response.text
        print(f'## [INFO] caching input into {input_file}')
        with open(input_file, 'w') as f:
            f.write(text)
    return text
