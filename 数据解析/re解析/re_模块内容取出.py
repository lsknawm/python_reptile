import re
s = '''
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='三国演义'><span id='10000'>中国电信</span></div>
<div class='红楼梦'><span id='10001'>中国移动</span></div>
<div class='水浒传'><span id='10022'>中国广电</span></div>
'''
obj = re.compile(r"<div class='(?P<book>.*?)'><span id='(?P<ID>\d{5})'>(?P<yyin>.*?)</span></div>",re.S)    #让.可以匹配换行符
result = obj.finditer(s)
my_list = []
for i in result:
    print(i.group('book','ID','yyin'))
    my_list.append(i.group('book'))
print(my_list)