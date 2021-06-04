# -*- coding: utf-8 -*-
import zipfile
import os


def main():
    
    path_raw = './data/raw/'
    zip_raw =  'pulmonary-embolism-in-ct-images.zip'

    try:
        extract_pe_ct(path_raw, zip_raw) 
    except AssertionError as error:
        print(error)
        print ('Error: extract files fail')

def extract_pe_ct(path_raw, zip_raw):

    with zipfile.ZipFile(path_raw+zip_raw,"r") as zipObj:
        
        print('extract zip ', zip_raw)
        zipObj.extractall(path_raw)

        print('extract zip success, removing zip')
        os.remove(path_raw+zip_raw)

if __name__ == '__main__':
    main()