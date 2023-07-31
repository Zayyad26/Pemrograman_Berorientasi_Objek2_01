# Script Generated Using PyAthlon
# Created By: Freddy Wicaksono, M.Kom
# ===================================
# filename : Matakuliah.py
import requests
import json
class Matakuliah:
    def __init__(self):
        self.__id=None
        self.__kodemk = None
        self.__namamk = None
        self.__sks = None
        self.__prodi = None
        self.__url = "http://localhost/appakademik/matakuliah_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodemk(self):
        return self.__kodemk
        
    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value
    @property
    def namamk(self):
        return self.__namamk
        
    @namamk.setter
    def namamk(self, value):
        self.__namamk = value
    @property
    def sks(self):
        return self.__sks
        
    @sks.setter
    def sks(self, value):
        self.__sks = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodemk(self, kodemk):
        url = self.__url+"?kodemk="+kodemk
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idmk']
            self.__kodemk = item['kodemk']
            self.__namamk = item['namamk']
            self.__sks = item['sks']
            self.__prodi = item['prodi']
        return data
    def simpan(self):
        payload = {
            "kodemk":self.__kodemk,
            "namamk":self.__namamk,
            "sks":self.__sks,
            "prodi":self.__prodi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodemk(self, kodemk):
        url = self.__url+"?kodemk="+kodemk
        payload = {
            "kodemk":self.__kodemk,
            "namamk":self.__namamk,
            "sks":self.__sks,
            "prodi":self.__prodi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodemk(self,kodemk):
        url = self.__url+"?kodemk="+kodemk
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
