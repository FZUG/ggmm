#功能：自动生成每周的 IRC 会议记录邮件
#
#输入：结束会议时 bot 的提示
# 示例：
'''
<zodbot> Minutes: http://meetbot.fedoraproject.org/fedora-zh/2014-01-31/fedora-zh.2014-01-31-13.02.html
<zodbot> Minutes (text): http://meetbot.fedoraproject.org/fedora-zh/2014-01-31/fedora-zh.2014-01-31-13.02.txt
<zodbot> Log: http://meetbot.fedoraproject.org/fedora-zh/2014-01-31/fedora-zh.2014-01-31-13.02.log.html
'''
#
#输出：.eml 文件
#
#程序结构：
# 1. 匹配 （获取用户输入，得到链接）
# 2. 抓取
# 3. 输出 （按照 .eml 文件的格式）
#
# 注意：
#  1. 所有编码都是 UTF-8
#  2. 仅保证 python3 能运行该程序

#config
TO="chinese@lists.fedoraproject.org"
CC=("meetingminutes@lists.fedoraproject.org", )
SUBJECT="Fedora Chinese Meeting Minutes"
GREETING="""Hi all,

The IRC meeting minutes yesterday are available at the links below. Thanks
everyone for attending the meeting."""

import re
import email
import sys
import urllib.request

#debug config
ENABLE_TRACE = True

def trace(s):
    if ENABLE_TRACE:
        print(s)

def get_user_input(gui=False):
    '''获取用户的输入，未来可能支持 gui
    返回一个 tuple，里面有三个不带换行符的字符串
    '''
#Dirty test
    print("get_user_input STUB!")
    return ("<zodbot> Minutes: http://meetbot.fedoraproject.org/fedora-zh/2014-01-31/fedora-zh.2014-01-31-13.02.html",\
            "<zodbot> Minutes (text): http://meetbot.fedoraproject.org/fedora-zh/2014-01-31/fedora-zh.2014-01-31-13.02.txt", \
            "<zodbot> Log: http://meetbot.fedoraproject.org/fedora-zh/2014-01-31/fedora-zh.2014-01-31-13.02.log.html")


def get_url(s):
    '''把形如 "<xxxbot>:abc http://server.org/log.html" 的字符串处理成
    ("abc", "http://server.org/log.html") 的 tuple
    '''
    trace("get_url() from : " + s)
    bot_pattern = re.compile('^<\w+bot>')

    #answer from http://stackoverflow.com/a/6883094
    link_pattern = re.compile(\
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    match = re.search(link_pattern, s)
    if not match:
        sys.exit("Url Match Error!")

    url = match.group(0)
    trace(url)
    s = s.replace(url, "")

    match = re.search(bot_pattern, s)
    if not match:
        sys.exit("Url Match Error!")

    bot = match.group(0)
    trace("bot name: " + bot)
    s = s.replace(bot, "")

    s = s.strip()
    s = s.rstrip(':')
    s = s.strip()
    
    trace("Description: " + s)
    return (s, url)



def fetch_data(url):
    '''该函数内不做多线程，就是用对应的库抓取信息
    返回一个列表，是解码后的字符串
    '''
    trace("Fetching "+url)
    req = urllib.request.urlopen(url)
    lines = req.readlines()
    strs = [line.decode('utf-8').rstrip('\n') for line in lines]
    trace(strs)
    return strs

def make_eml(to, cc, subject, message, log):
    '''to: string
    cc: list/tuple of strings
    subject: string (without date)
    message: string
    log: list of strings
    return: list of strings
    '''
    pass

if __name__ == '__main__':
    user_input = get_user_input()
    #urls: description -> url
    urls = dict()
    for uinpt in user_input:
        url = get_url(uinpt)
        urls[ url[0] ] = url[1]

    print("Fetching data from server......")
    log = fetch_data(urls['Minutes (text)'])

    eml = make_eml(TO, CC, SUBJECT, GREETING, log)

