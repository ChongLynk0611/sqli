from urllib.parse import urlparse
import useragents
# hàm để gửi request lên url 
def getHtml(url):
    header = useragents.get()
    print(header)


def scan(url):
    # tách domain ra khỏi url
    domain = url.split("?")[0]
    #tách lấy từng pram trong query và gán vào mảng queries
    queries = urlparse(url).query.split("&")
    # nếu không có query trong url thì không tồn tại sql injecttion
    if len(queries) == 0:
        print("")
        return False
    
    # nếu có query trong url thì check sql injection 
    # các phần inject vào query để check xem url có bị lỗi sqlinjection không
    payloads = ("'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
    for payload in payloads:
        # nối các ký tự check sqli vào query để kiểm tra
        website = domain + "?" + ("&".join([param + payload for param in queries]))
        

getHtml()