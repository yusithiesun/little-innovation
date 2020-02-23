'''
项目介绍：爬取华南理工大学所有讲座预告的链接，存在SCUT.xlsx中
说明：
1.起始网页：https://www.scut.edu.cn/new/9010/list.htm
2.使用正则表达式匹配内链
（杀鸡不用scrapy）
'''
import requests
import lxml
import re
import time
from openpyxl import Workbook
from bs4 import BeautifulSoup

path="https://www.scut.edu.cn"  #前缀网址
#原本打算用集合，考虑到无序，而列表即使文章重复也会因重名而覆盖，所以仍用列表
url_list=[] 

if __name__=="__main__":
    for i in range(1,83):
        #构造翻页页面，按基本流程煮一碗美丽汤
        Page=path+"/new/9010/list"+str(i)+".htm"
        html=requests.get(Page)
        html.encoding='utf-8'
        bs=BeautifulSoup(html.text,'lxml')
        #使用正则表达式匹配需要的内链
        for link in bs.findAll('a',href=re.compile('^(/new/20.*)')):
            url_list.append(path+link["href"])
        #为了降低对SCUT官网的服务器可能存在的影响，假装暂停一下
        time.sleep(1)
    #for i in url_list:print(i)
    wb=Workbook()
    sheet=wb.active
    for link,index in zip(url_list,range(1,len(url_list)+1)):
        sheet.cell(index,1).value=link
    wb.save("***/SCUT.xlsx")

    
