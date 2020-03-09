import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':
    url_gambar = []
    url_gambar.append('https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg')
    url_gambar.append('https://maimai.sega.com/storage/root/dxkuma.png')
    url_gambar.append('https://maimai.sega.com/storage/root/laun.png')
    url_gambar.append('https://maimai.sega.com/storage/root/dry.png')
    url_gambar.append('https://maimai-club.bingoworlds.com/icon/2010117.PNG')

threads = []
for i in range(5):
    t = threading.Thread(target=download_gambar, args=(url_gambar[i],))
    threads.append(t)

for thr in threads:
    thr.start()
