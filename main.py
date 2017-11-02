# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url_js='http://www.jshrss.gov.cn/rsrcfww/xwdt/tzgg/sydwzp/index_{page}.html'

res=requests.get(url_js.format(page=1))
res_bs=BeautifulSoup(res.text,"html5lib")
res_bs_l=res_bs.select(".z_mainbox > .files_left_box > .files_left_box_border > .xwdt_list > ul > li")
#res_bs_l=res_bs.select('a[href]')
print res_bs_l
