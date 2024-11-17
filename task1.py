# TODO решите задачу
import json


def task() -> float:
    file_path = 'input.json'

    with open(file_path, 'r') as file:
        data = json.load(file)

    total_sum = sum(item['score'] * item['weight'] for item in data)

    return round(total_sum, 3)


print(task())
