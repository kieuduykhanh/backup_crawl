from bs4 import BeautifulSoup
import urllib.request
import json


def getAllLinkBooksOfPage(urlOfPage):
    '''

    :param urlOfPage:
    :return:
    '''
    page = urllib.request.urlopen(urlOfPage)
    soup = BeautifulSoup(page, 'html.parser')
    urls = []
    for i in range(38):
        try:
            url = soup.find('a', id="ContentPlaceHolder1_ucBookSearch1_rptBookList_hplImage_" + str(i))
            urls.append(url['href'])
        except:
            pass
    return urls


def getLinkAudiosOfBook(urlOfBook):
    '''

    :param urlOfBook:
    :return:
    '''

    dic = {}
    page = urllib.request.urlopen(urlOfBook)
    soup = BeautifulSoup(page, 'html.parser')
    data = soup.findAll('script')
    data = str(data[16].contents[0])
    data = data.replace('$(document).ready(function() {var jplaylist = new jPlayerPlaylist({jPlayer: "#jquery_jplayer_1",cssSelectorAncestor: "#jp_container_1"},', '').replace(', {playlistOptions: {autoPlay:true},swfPath: "/App_Themes/themeAudioBook/js",supplied: "mp3",wmode: "window"});jplaylist.select(0);});', '')[1:-1]
    data = data.split('},')
    for i in range(len(data)):
        data[i] = data[i][data[i].index('mp3: ')+5:].replace("\"", "").replace("}","")
    data = list(set(data))
    try:
        data.remove('')
    except: pass

    dic['name'] = soup.find('span', id="ContentPlaceHolder1_ucBookDetail1_rptBookDetail_lbBookName_0").text

    dic['links'] = data

    return dic


def dataToJsonFile(data):
    '''

    :param data:
    :return:
    '''
    with open('data.json', 'w', encoding='utf8') as txt_file:
        json.dump(data, txt_file, ensure_ascii=False)


list_pages = [
    "http://sachnoiviet.com/sach-noi/the-loai/111/giai-tri.html",
    "http://sachnoiviet.com/sach-noi/the-loai/69/ke-sach-lam-giau.html",
    "http://sachnoiviet.com/sach-noi/the-loai/71/ki-nang-quan-trong.html",
    "http://sachnoiviet.com/sach-noi/the-loai/88/kinh-doanh-theo-mang.html",
    "http://sachnoiviet.com/sach-noi/the-loai/68/kien-thuc-kinh-te.html",
    "http://sachnoiviet.com/sach-noi/the-loai/89/giao-duc.html",
    "http://sachnoiviet.com/sach-noi/the-loai/109/giao-duc-som---chan-hung-dan-toc.html",
    "http://sachnoiviet.com/sach-noi/the-loai/74/ren-nghi-luc---nhan-cach.html",
    "http://sachnoiviet.com/sach-noi/the-loai/108/van-hoa.html",
    "http://sachnoiviet.com/sach-noi/the-loai/107/sach-giao-khoa.html",
    "http://sachnoiviet.com/sach-noi/the-loai/92/danh-nhan-viet-nam.html",
    "http://sachnoiviet.com/sach-noi/the-loai/93/danh-nhan-the-gioi.html",
    "http://sachnoiviet.com/sach-noi/the-loai/101/ttvh---viet-nam.html",
    "http://sachnoiviet.com/sach-noi/the-loai/100/ttvh---the-gioi.html",
    "http://sachnoiviet.com/sach-noi/the-loai/105/ngu-ngon---co-tich.html",
    "http://sachnoiviet.com/sach-noi/the-loai/112/tam-ly---xa-hoi.html",
    "http://sachnoiviet.com/sach-noi/the-loai/113/sach-dai-hoc.html",
    "http://sachnoiviet.com/sach-noi/the-loai/77/cao-hoc-kinh-te.html",
    "http://sachnoiviet.com/sach-noi/the-loai/72/phat-giao.html",
    "http://sachnoiviet.com/sach-noi/the-loai/94/tam-thoi-01.html",
    "http://sachnoiviet.com/sach-noi/the-loai/95/tam-thoi-02.html",
    "http://sachnoiviet.com/sach-noi/the-loai/104/tam-thoi-03.html"
]

list_books = []
list_book_and_audio = []

for page in list_pages:
    list_books += getAllLinkBooksOfPage(page)


for book in list_books:
    try:
        list_book_and_audio.append(getLinkAudiosOfBook(book))
    except: pass


dataToJsonFile(list_book_and_audio)
