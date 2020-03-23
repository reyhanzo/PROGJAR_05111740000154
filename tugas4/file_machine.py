from file import File
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get 
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = File()

class FileMachine:
    def proses(self,string_to_process, data):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'): #Upload file
                logging.warning("upload")
                namafile = cstring[1].strip()
                p.put_data(namafile,data)
                return "OK"
            elif (command=='list'): #List file
                logging.warning("list")
                hasil = p.list_data()
                hasil = {"file":hasil}
                return json.dumps(hasil)
            elif (command=='download'):
                logging.warning("download")
                namafile = cstring[1].strip()
                hasil = p.get_data(namafile)
                return hasil
                #return json.dumps(hasil)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = FileMachine()
#    hasil = pm.proses("list")
#    print(hasil)
    hasil = pm.proses("download pesan.txt", "null")
    print(hasil)