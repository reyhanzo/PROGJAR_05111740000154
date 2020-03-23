import shelve
import uuid
from datetime import datetime
import os

class File:
    def __init__(self):
        #  self.data = shelve.open('mydata.dat')
        if not os.path.exists("Server"):
            os.makedirs("Server")

    def put_data(self, namafile=None, data=None):
        f = open("Server/" + namafile, "wb")
        f.write(data)
        f.close()
        return True

    def get_data(self, namafile=None):
        if os.path.isfile("Server/" + namafile):
            myfile = open("Server/" + namafile, "rb")
            data = myfile.read()
            myfile.close()
        else:
            data = b'File not Exist'
        return data

    def list_data(self):
        list = os.listdir("Server")
        f = []
        for filename in list:
            f.append(filename)
        return f


if __name__ == '__main__':
    p = File()
    # data=open("File Client/171076.jpg", 'rb')
    # p.Upload("171076.jpg",data.read())
    # print(p.List())
    print(p.get_data("2.png"))