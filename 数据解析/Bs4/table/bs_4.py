import requests
from bs4 import BeautifulSoup
import csv
#拿到页面源码
#数据分析拿到想要的内容
url = 'https://nba.hupu.com/stats/players'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
resp = requests.get(url=url,headers=headers,verify=False)
resp.encoding='utf-8'
#先添加一个标题，以写入覆盖模式，覆盖以前的内容
f = open('vegetable_price.csv', mode='w', encoding='utf-8')
f.write("排名,球员,球队,得分,命中-出手,命中率,命中-三分,三分命中率,命中-罚球,罚球命中率,场次,上场时间\n")
f.close()   #关闭文件，以两次打开文件操作，如果都是读写或者追加都不太妥当
#以追加形式写入，以免覆盖以前的内容
f = open('vegetable_price.csv', mode='a', encoding='utf-8', newline='')
csvwrite = csv.writer(f)
# with open('test.html',mode='w',encoding='utf-8') as f:
#     f.write(resp.text)
page = BeautifulSoup(resp.text,"html.parser")
#将table提取
table_surface = page.find('table',attrs={"class": 'players_table'})
#将标签栏去除
trs = table_surface.find_all("tr")[1:]
# csvwrite.writerow([])
for tr in trs:
    tds = tr.find_all('td')
    ranking = tds[0].text
    player = tds[1].text
    team = tds[2].text
    score = tds[3].text
    hit = tds[4].text
    hit_rate = tds[5].text
    hit_three_points = tds[6].text
    three_point_shooting_percentage = tds[7].text
    serve = tds[8].text
    free_throw_percentage = tds[9].text
    number_of_sessions = tds[10].text
    playing_time = tds[11].text
    print(ranking,player,team,score,hit,hit_rate,hit_three_points,three_point_shooting_percentage,serve,free_throw_percentage,number_of_sessions,playing_time,sep='::')
    csvwrite.writerow([ranking,player,team,score,hit,hit_rate,hit_three_points,three_point_shooting_percentage,serve,free_throw_percentage,number_of_sessions,playing_time])
f.close()