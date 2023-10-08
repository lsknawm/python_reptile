from lxml import etree
tree = etree.parse('b.html')
# print(tree.xpath('/html/body//li[1]/a/text()'))       #xpath顺序从1开始数，中括号为索引
# print(tree.xpath('/html/body//li[1]/a/text()'))     #此处匹配第一个的li标签
# print(tree.xpath('/html/body//ul/li/a[@href="bing"]/text()'))   #此处匹配href为bing的内容
ol_li_list = tree.xpath('/html/body/div/div/ol/li')
for l_i in ol_li_list:
    result = (l_i.xpath('./a/text()'))     #继续寻找，从li接着找
    print(result)
    res = l_i.xpath('./a[@href="ftp"]/text()')  #相对路径继续查找
    href = l_i.xpath('./a/@href')   #拿到属性值
    print(href)
print(tree.xpath('/html/body/div/ul/li/a/@href'))   #拿到链接