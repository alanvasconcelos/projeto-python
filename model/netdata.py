'''
Created on 9 de mar de 2017

Obtem dados em arquivos da internet

@author: Gilzamir (gilzamir@outlook.com)
'''

#coding: utf-8

import urllib.request as request
import zipfile
import io
import os
import re
import model
import sys
from math import sin,cos,sqrt,asin,pi


BUFF_SIZE = 1024

class NetDataModel():
    def download_length(self, response, output, length):
        times = length/BUFF_SIZE
        if length % BUFF_SIZE > 0:
            times = times + 1
        for time in range(int(times)):
            output.write(response.read(BUFF_SIZE))
            print("Downloaded %d " % (((time * BUFF_SIZE)/100.0) * 100))

    def download(self, response, output):
        total_downloaded = 0
        while True:
            data = response.read(BUFF_SIZE)
            total_downloaded += len(data)
            if not data:
                break
            output.write(data)
            print('Downloaded {bytes}'.format(bytes=total_downloaded))

    def extract_filename(self, filename):
        filename = filename.split('.')
        del filename[len(filename) - 1]
        return '.'.join(filename)

    def read_data(self, path):
        fdata = open(path, 'rt', encoding="utf8")
        data = []
        for line in fdata:
            ld = line.split(',')
            
            ender = model.Endereco(ld[5], ld[6], ld[7], ld[8])
            unit_health = model.UnidadeDeSaude(ld[0], ld[1], ld[2], ld[3], ld[4], ender, ld[9], ld[10], ld[11], ld[12])
            
            data.append(unit_health)
        fdata.close()
        return data

    def loadlistfromcsv(self, URL, OUTPUT_PATH="dt.zip", EXTRACTION_PATH="./"):
        if (os.path.exists(OUTPUT_PATH) == 0):
            response = request.urlopen(URL)
            out_file = io.FileIO(OUTPUT_PATH, mode="w")
            content_length = response.getheader('Content-Length')
            if content_length:
                length = int(content_length)
                self.download_length(response, out_file, length)
            else:
                self.download(response, out_file)
            response.close()
            out_file.close()
        
        zfile = zipfile.ZipFile(OUTPUT_PATH)
        zfile.extractall(EXTRACTION_PATH)
        filename = [name for name in os.listdir(EXTRACTION_PATH) if '.csv' in name]
        dt = self.read_data(EXTRACTION_PATH+filename[0])
        return dt

    def create_cidcnes_index(self, list):
        db = {}
        for obj in list:
            cidval = obj.magicGet('codCid')
            cnesval = obj.magicGet('codCnes')
            db[cidval+cnesval] = obj
        return db;

    def syncdata(self):
        RESOURCE_URL = "http://repositorio.dados.gov.br/saude/unidades-saude/unidade-basica-saude/ubs.csv.zip"
        
        if os == "Windows":
            OUTPUT_PATH = os.path.expanduser("saida.zip")
            EXTRACTED_PATH = os.path.expanduser("~\\")
        else:
            OUTPUT_PATH = os.path.expanduser("saida.zip")
            EXTRACTED_PATH = os.path.expanduser("~/")

        if len(sys.argv) > 1:
            RESOURCE_URL = sys.argv[1] 
        if len(sys.argv) > 2:
            OUTPUT_PATH = sys.argv[2]
        if len(sys.argv) > 3:
            EXTRACTION_PATH = sys.argv[3]
        
        self.repository = self.loadlistfromcsv(RESOURCE_URL, OUTPUT_PATH, EXTRACTED_PATH)

    def searchNearUnitHealth(self, longitude, latitude):
        self.syncdata()
        dados = self.repository
        #dados = self.read_data('/home/user/Documentos/lp3/pythoncourse/pythoncourse/src/ubs.csv')
        r = 6371000
        c = pi/180
        db = {}
        for d in dados[1:]:
            dist = 2 * r * asin(sqrt(sin(c * (float(d._get_latitude()) - float(latitude)) / 2) ** 2 + cos(c * float(latitude)) * cos(c * float(d._get_latitude())) * sin(c * (float(d._get_longitude()) - float(longitude)) / 2) ** 2))
            db[dist] = d

        for d in db:
            return db[d]

    def searchAllUnitHealth(self):
        self.syncdata()
        return self.repository
        #return self.read_data('/home/user/Documentos/lp3/pythoncourse/pythoncourse/src/ubs.csv')

    def __init__(self):
        self.repository = []
