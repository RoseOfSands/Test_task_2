
def load_file(path: str) -> dict:
    """load json file"""
    with open(path, 'r') as file:
        text = file.read().replace(",", "").replace("}", "").replace("{", "").replace(":", "").replace('"', "").split()
    keys = []
    values = []
    for k in range(len(text)):
        if k == 0 or k % 2 == 0:
            keys.append(text[k])
        else:
            values.append(float(text[k]))
    return dict(zip(keys, values))


a = load_file('/home/natalia/Рабочий стол/new/test_task/data.json')
print(a)
