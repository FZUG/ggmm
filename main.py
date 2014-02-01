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

import re, email

def get_user_input(gui=False):
    '''获取用户的输入，未来可能支持 gui
    返回一个 tuple，里面有三个不带换行符的字符串
    '''
    pass

def get_url(s):
    '''把形如 "<xxxbot>:abc http://server.org/log.html" 的字符串处理成
    ("abc", "http://server.org/log.html") 的 tuple
    '''
    pass

def fetch_data(url):
    '''该函数内不做多线程，就是用对应的库抓取信息
    '''

def make_eml(to, cc, subject, welcome_message, log):
    '''to: string
    cc: list/tuple of strings
    subject: string (without date)
    welcome_message: string
    log: FIXME I'm not sure yet
    '''
    pass

if __name__ == '__main__':
    pass
