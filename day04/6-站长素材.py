# import requests
# import urllib.request
# import urllib
# # 测试一条数据


#
# import os
# from lxml import etree
#
# url = 'http://sc.chinaz.com/tupian/dahaitupian.html'
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
#            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#            }
# response = requests.get(url=url,headers=headers)
# response.encoding = 'utf-8'
# html = response.text
# # with open('./站长.html',mode='w',encoding='utf-8') as fp:
# #     fp.write(html)
#
# tree = etree.HTML(html)

#该数据通过浏览器获取的，js css 动态代码执行出来。

# content = '''
# <div class="box picblock col3 masonry-brick" style="width: 186px; height: 156px; position: absolute; top: 0px; left: 206px;">
# <div>
# <a target="_blank" href="http://sc.chinaz.com/tupian/180619238331.htm" alt="岩石大海风景图片"><img alt="岩石大海风景图片"
#  src="http://pic1.sc.chinaz.com/Files/pic/pic9/201806/zzpic12380_s.jpg"></a>
#
# </div>
# <p><a target="_blank" href="http://sc.chinaz.com/tupian/180619238331.htm" alt="岩石大海风景图片">岩石大海风景图片</a></p>
# </div>
# '''
# tree = etree.HTML(content)
#
# pic_urls = tree.xpath('//div[@class="box picblock col3 masonry-brick"]/div/a/img/@src')
#
# print(pic_urls)


# 测试多条数据-------------------------------
import requests
import urllib.request
import urllib

import os
from lxml import etree

url = 'http://sc.chinaz.com/tupian/dahaitupian.html'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           }
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
html = response.text
# 读取网上的数据。保存到本地
with open('./站长.html',mode='w',encoding='utf-8') as fp:
    fp.write(html)
tree = etree.HTML(html)
# ===========================================
'''
这些代码是网页源代码，不能用。所以用下一种方案。把网页的内容保存到本地
<div class="box picblock col3 masonry-brick" style="width: 186px; height: 156px; position: absolute; top: 0px; left: 206px;">
<div>
<a target="_blank" href="http://sc.chinaz.com/tupian/180619238331.htm" alt="岩石大海风景图片"><img alt="岩石大海风景图片"
 src="http://pic1.sc.chinaz.com/Files/pic/pic9/201806/zzpic12380_s.jpg"></a>

</div>
<p><a target="_blank" href="http://sc.chinaz.com/tupian/180619238331.htm" alt="岩石大海风景图片">岩石大海风景图片</a></p>
</div>
'''
# ============================================
'''
下载网页上的代码。对比对比
<div class="box picblock col3" style="width:186px;height:155px">
<div>
<a target="_blank" href="http://sc.chinaz.com/tupian/180530099854.htm" alt="情定爱琴海唯美图片"><img src2="http://pic1.sc.chinaz.com/Files/pic/pic9/201805/zzpic12119_s.jpg" alt="情定爱琴海唯美图片"></a>
</div>
<p><a target="_blank" href="http://sc.chinaz.com/tupian/180530099854.htm" alt="情定爱琴海唯美图片">情定爱琴海唯美图片</a></p>
</div>
'''
# ============================================
# pic_urls = tree.xpath('//div[@class="box picblock col3 masonry-brick"]/div/a/img/@src')
pic_urls = tree.xpath('//div[@class="box picblock col3"]/div/a/img/@src2')
pic_titles = tree.xpath('//div[@class="box picblock col3"]/div/a/img/@alt')

# print(pic_urls)
# print(len(pic_urls))

# 保存到本地

for i in range(len(pic_urls)):
    # suddix:后缀 截取图片格式
    suddix = os.path.splitext(pic_urls[i])[-1]
    #                                        文件名。不确定是哪个格式。所以截取图片格式
    urllib.request.urlretrieve(url=pic_urls[i],filename='./站长/%s%s'%(pic_titles[i],suddix))































