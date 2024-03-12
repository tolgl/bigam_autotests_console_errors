import os
import requests
import json


def send_message_telegram():
    try:
        name_failed_tests = []
        status_test = []
        allure_reports = []
        folder = 'allure_results/'
        files = os.listdir(folder)
        for file in files:
            if 'result.json' in file:
                with open(folder + file) as f:
                    data = json.load(f)
                    allure_reports.append(data)
        for i in allure_reports:
            status_test.append(i['status'])
            if i['status'] == 'failed':
                name_failed_tests.append(i['name'])

        token = '6836860421:AAHgjmjF0MBH8Xvfb8yWkH2dQHE7P7GZynk'
        chat_id = '-1002120752814'
        message = f'Кол-во выполненных тестов: {status_test.count("passed")} \n' \
                  f'Кол-во не выполненных тестов: {status_test.count("failed")} \n' \
                  f'Тесты с ошибкой: {name_failed_tests}'

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

        print(requests.get(url=url).json())

    except FileNotFoundError:
        token = '6836860421:AAHgjmjF0MBH8Xvfb8yWkH2dQHE7P7GZynk'
        chat_id = '-1002120752814'
        message = 'No such file or directory: "allure_report"'
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url=url).json())


if __name__ == '__main__':
    send_message_telegram()
