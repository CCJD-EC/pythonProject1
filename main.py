import json
import sys

import requests
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
base_url = "http://api.airvisual.com/v2/city/"
api_key = "e2579de6-9f51-4f4e-a48e-c4e3f9432275"


class COApp(QWidget):
    country = ''
    state = ''
    city = ''

    def __init__(self):
        super().__init__()
        uic.loadUi('gui/page1.ui', self)
        colors = ['#4dab6d', "#72c66e", "#c1da64", "#f6ee54", "#fabd57", "#f36d54", "#ee4d55"]
        self.getcountries(self)

    def getcountries(self, argv):
        url = "http://api.airvisual.com/v2/countries?key=" + api_key
        response = requests.request("GET", url)
        # a = ['Selecciona uno ..']
        a = ['Selecciona uno ..', 'USA']
        x = json.loads(response.text)
        # for y in x['data']:
        #     a.append(y['country'])
        self.comboBox.addItems(a)
        # self.comboBox.setCurrentIndex(1)
        self.comboBox.currentTextChanged.connect(self.text_changed)
        self.comboBox.currentIndexChanged.connect(self.index_changed)

    def text_changed(self, s):
        print("Text changed:", s)
        url = "http://api.airvisual.com/v2/states?country=" + self.comboBox.currentText() + "&key=" + api_key
        response = requests.request("GET", url)
        # a = ['Selecciona uno ..']
        a = ['Selecciona uno ..', 'California']
        x = json.loads(response.text)
        # for y in x['data']:
        #     a.append(y['state'])
        self.comboBox_2.addItems(a)
        # self.comboBox.setCurrentIndex(1)
        self.comboBox_2.currentTextChanged.connect(self.text_change_2)

    def text_change_2(self, s):
        print("Text changed:", s)
        # url = "http://api.airvisual.com/v2/cities?state=" + self.comboBox_2.currentText() + "&country=" \
        #       + self.comboBox.currentText() + "&key=" + api_key
        # response = requests.request("GET", url)
        # a = ['Selecciona uno ..']
        a = ['Selecciona uno ..', 'Los Angeles']
        # x = json.loads(response.text)
        # for y in x['data']:
        #     a.append(y['city'])
        self.comboBox_3.addItems(a)
        # self.comboBox.setCurrentIndex(1)
        self.comboBox_3.currentTextChanged.connect(self.text_change_3)

    def text_change_3(self, s):
        print("Text changed:", s)
        url = "http://api.airvisual.com/v2/city?city=" + self.comboBox_3.currentText() + "&state=" + self.comboBox_2.currentText() + "&country=" \
              + self.comboBox.currentText() + "&key=" + api_key
        response = requests.request("GET", url)
        x = json.loads(response.text)
        self.lcdNumber_2.display(x['data']['current']['weather']['tp'])
        self.lcdNumber_3.display(x['data']['current']['weather']['hu'])
        self.lcdNumber.display(x['data']['current']['pollution']['aqius'])

    def index_changed(self, index):
        print("Index changed", index)


def print_response(response):
    print(response.text)
    print(response.json())
    print(response.status_code)
    print(response.headers)


if __name__ == '__main__':
    url = "http://api.airvisual.com/v2/city?city=Los Angeles&state=California&country=USA&key=" + api_key

    # response = requests.request("GET", url)

    # print_response(response)
    app = QApplication(sys.argv)

    myApp = COApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window....')
