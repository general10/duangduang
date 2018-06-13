# coding: utf-8
import urllib2

from bs4 import BeautifulSoup
import re,json,requests


def getJsonText(self, url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print '获取失败'
        return ''


def getgood(url):
    html = urllib2.urlopen(url).read()
    # 用正则表达式拿取

    ma = re.search(r'"productId":"[\d]+"', html)
    productId = eval(ma.group().split(':')[-1])
    ma = re.search(r'"categoryPath":"[\d.]+"', html)
    categoryPath = eval(ma.group().split(':')[-1])
    # print page_url
    ma = re.search(r'"mainProductId":"[\d.]+"', html)
    mainProductId = eval(ma.group().split(':')[-1])
    # 对Ajax的url进行拼接
    json_url = 'http://product.dangdang.com/index.php?r=comment%2Flist&productId={productId}&categoryPath={categoryPath}&mainProductId={mainProductId}&mediumId=0&pageIndex=1&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0'.format(
        productId=productId, categoryPath=categoryPath, mainProductId=mainProductId)
    # 调用方法，下载下来json数据
    json_html = json.loads(getJsonText(json_url))
    summary = json_html['data']['list']['summary']
    data = {}
    data['all_comment_num'] = summary['total_comment_num']              # 总评论数
    data['good_comment_num'] = summary['total_crazy_count']             # 好评数
    data['middle_comment_num'] = summary['total_indifferent_count']     # 中评数
    data['bad_comment_num'] = summary['total_detest_count']             # 差评数
    data['good_rate'] = summary['goodRate']                             # 好评率
    return data



if __name__ == '__main__':
    print(getgood('http://product.dangdang.com/23761145.html'))
