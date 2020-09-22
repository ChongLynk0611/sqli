# -*- coding: utf-8 -*-
import queue
import urllib.parse
import requests
import threading
file_wordlist = "./SVNDigger/all.txt"
url_taget = "http://testphp.vulnweb.com"
""" hàm dùng để tạo queue chứa các từ khóa dir thông dụng
các từ khóa này sẽ dùng để vét cạn dir """
def build_wordlist(file_wordlist):
    #taoj queue chứa các từ khóa và open file 
    words = queue.Queue()
    fb = open(file_wordlist )
    # gán file vào biến file và sau đó duyệt vào queue
    with fb as file:
        for f in file:
            f = f.rstrip()
            words.put(f)
    fb.close()
    return words

""" hàm tạo tất cả các dir có thể có của 1 domain input
gửi reqest lên các url được tạo ra bằng cách thêm các tên thư mục thông dụng của file all.txt
nếu response.status = 200 => url đó có tồn tại, ngược lại url đó k tồn tại"""
def dir_bruter(word_queue , extentions = None):
    while not word_queue.empty():
        attempt = word_queue.get()
       
        # tạo ra mảng để lưu các url có tồn tại
        attempt_list = []

        # nếu là tên thư mục 
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)


            # là tên file
        else:
            attempt_list.append("/%s" %attempt)
        
        # nếu truyền extensions vào
        if extentions:
            for extension in extentions:
                attempt_list.append("/%s%s" % (attempt , extension))

        # duyệt tất cả các phần extension có thể tạo ra được với url_taget 
        for brute in attempt_list:
            url = "%s%s" %(url_taget ,urllib.parse.quote(brute))
            try:
                r = requests.get(url)
                if(r.status_code == 200):
                    print("[200] => %s" %url )
            except:
                pass
        
word_queue = build_wordlist(file_wordlist)
extensions = [".php",".bak",".orig",".inc"]
for i in range(50):
    t = threading.Thread(target=dir_bruter , args=(word_queue , extensions))
    t.start()
