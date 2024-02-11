import csv


def read_csv_without_header(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)
        data = list(reader)
    return data


def get_positive_datas(file_path):
    datas = read_csv_without_header(file_path)
    return list(filter(lambda x: "positive" in x, datas))


def get_negative_datas(file_path):
    datas = read_csv_without_header(file_path)
    return list(filter(lambda x: "negative" in x, datas))


if __name__ == "__main__":
    path = "./testdatas/search_datas.csv"
    print(get_positive_datas(path))
    print(get_negative_datas(path))
