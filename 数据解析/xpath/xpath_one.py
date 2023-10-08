from lxml import etree
xml = '''
<bookstore>
  <book>
    <title lang="en">Learning XML</title>
    <author>John Doe</author>
    <year>2003</year>
    <price>34.95</price>
    <price>64.95</price>
    <price>45.95</price>
    <price>467.95</price>
    <div>
        <price>645.95</price>
        <div>
            <price>**date</price>
        </div>
    </div>
  </book>
  <book>
    <nick>
        <price>645.95</price>
        <author>
            <price>***date</price>
        </author>
    </nick>
    <title lang="en">XML for Dummies</title>
    <author>Jane Doe</author>
    <year>2005</year>
    <price>45.95</price>
    <price>34.95</price>
    <price>234.95</price>
    <price>645.95</price>
    <div>
        <price>645.95</price>
    </div>
  </book>
  <book>
    <title lang="zh">XML入门</title>
    <author>张三</author>
    <year>2010</year>
    <price>49.95</price>
    <price>43.95</price>
    <price>345.95</price>
    <div>
        <price>654635464536543.95</price>
    </div>
    <price>54.95</price>
  </book>
</bookstore>
'''
tree = etree.XML(xml)
print(tree.xpath('/bookstore/book/author/text()'))  #绝对路径
print(tree.xpath('/bookstore/book//price/text()'))  #双下划线表示多层级
print(tree.xpath('/bookstore/book/*/*/price/text()'))  #*表示为任意节点
print(tree.xpath('/bookstore//year/text()'))    #拿到bookstore里面所有的year