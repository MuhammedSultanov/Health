import json

def read_json_file(file_path):

    with open(file_path, 'r') as file:
        return json.load(file)

def format_health_data(content):
    raw_text = content['parts'][0]['text']


    return raw_text

def main():

    json_file_path = 'response.json'


    data = read_json_file(json_file_path)

    formatted_report = format_health_data(data['text'])

    print(formatted_report)

    with open('formatted_report.txt', 'w') as report_file:
        report_file.write(formatted_report)

if __name__ == "__main__":
    main()
