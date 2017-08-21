import requests
from lxml import etree

from model.RequestModel import RequestModel

'''
@Desc
    测试各个功能的脚本

@Author monkey
@Date 2017-08-08
'''

# 测试案例1
# url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_2.html'
# html = requests.get(url, headers=RequestModel.getHeaders(), proxies=RequestModel.getProxies())
# print(html.status_code)

#测试案例2
# temp1 = {'director': 'S·S·拉贾穆里 S.S. Rajamouli', 'language': '泰卢固语/泰米尔语/印地语/马拉雅拉姆语', 'resolution': '1280 x 720', 'type': '[巴霍巴利王(下)：终结][BD-mkv.720p.中英双字][2017年动作战争]', 'trans_name': '巴霍巴利王(下)：终结/巴霍巴利王：磅礴终章(台)/巴霍巴利王(下)/巴霍巴利王2/巴霍巴利王：结局', 'publish': '2017-04-28(印度)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '167分钟', 'level': '剧情/动作/战争/奇幻/冒险', 'size': '1CD', 'screenshot': 'https://public.lightpic.info/image/8274_59872EB90.jpg', 'format': 'x264 + AAC', 'douban_score': '7.1/10 from 2,496 users', 'name': 'Baahubali: The Conclusion', 'actors': '\u3000帕拉巴斯 Prabhas\n拉纳·达格巴提 Rana Daggubati\n安努舒卡·谢蒂 Anushka Shetty\n特曼娜·芭蒂亚 Tamannaah Bhatia\n萨伯拉杰 Subbaraju\n拉姆亚·克里希南 Ramya Krishnan\n纳赛尔 Nasser\n挲塞亚拉杰 Satyaraj', 'subtitles': '中英双字幕', 'IMDB_socre': '8.7/10 from 45,729 users', 'conutry': '印度', 'placard': 'https://public.lightpic.info/image/AEC1_597FDBD70.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp2 = {'director': '迈克尔·法斯宾德 Michael Fassbender', 'language': '英语', 'resolution': '1CD', 'type': '[异形：契约][BD-mkv.720p.中英双字][2017年科幻惊悚恐怖]', 'trans_name': '异形：契约/异形：圣约(港/台)/神奇异形在哪里(豆友译名)/已开：大勺(豆友译名)/异形：失乐园/普罗米修斯2', 'publish': '2017-05-10(法国)/2017-05-19(美国)/2017-06-16(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '雷德利·斯科特 Ridley Scott', 'level': '科幻/惊悚/恐怖', 'size': '122分钟', 'screenshot': 'https://public.lightpic.info/image/0E0B_5981E9240.jpg', 'format': '1280 x 720', 'douban_score': 'x264 + AAC', 'name': 'Alien: Covenant', 'actors': '\u3000凯瑟琳·沃特斯顿 Katherine Waterston\n凯瑟琳·沃特斯顿 Katherine Waterston\n比利·克鲁德普 Billy Crudup\n丹尼·麦克布耐德 Danny McBride\n德米安·比齐尔 Demián Bichir\n卡门·艾乔戈 Carmen Ejogo\n朱西·斯莫利特 Jussie Smollett\n考莉·赫尔南德斯 Callie Hernandez\n艾米·西米茨 Amy Seimetz\n纳撒尼尔·迪安 Nathaniel Dean\n亚历山大·英格兰 Alexander England\n本杰明·里格比 Benjamin Rigby\n乌利·拉图基孚 Uli Latukefu\n泰丝·哈乌布里奇 Tess Haubrich\n罗蕾莱·金 Lorelei King\n哈维尔·博特 Javier Botet\n詹姆斯·弗兰科 James Franco\n盖·皮尔斯 Guy Pearce\n劳米·拉佩斯 Noomi Rapace', 'subtitles': '中英双字幕', 'IMDB_socre': '6.7/10 from 91,839 users', 'conutry': '美国', 'placard': 'https://public.lightpic.info/image/D48F_595B69A80.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp3 = {'director': '尼古拉·科斯特-瓦尔道 Nikolaj Coster-Waldau', 'language': '英语', 'resolution': '1CD', 'type': '[一锤定音][BD-mkv.720p.中英双字][2017年惊悚动作]', 'trans_name': '一锤定音', 'publish': '2017-06-17(洛杉矶电影节)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2016', 'duration': '里克·罗曼·沃夫 Ric Roman Waugh', 'level': '剧情/动作/犯罪/惊悚', 'size': '121分钟', 'screenshot': 'https://public.lightpic.info/image/E9DA_597FDBD70.jpg', 'format': '1280 x 720', 'douban_score': 'x264 + AAC', 'name': 'Shot Caller', 'actors': '\u3000乔·博恩瑟 Jon Bernthal\n乔·博恩瑟 Jon Bernthal\n蕾克·贝尔 Lake Bell\n欧玛瑞·哈德威克 Omari Hardwick\n杰弗里·多诺万 Jeffrey Donovan\n洁西·斯克拉姆 Jessy Schram\n本杰明·布拉特 Benjamin Bratt\n伊万·琼斯 Evan Jones\n马特·杰拉德 Matt Gerald\n迈克尔·兰德斯 Michael Landes\n艾莫里·科恩 Emory Cohen\nChris Browning\n基思·雅各 Keith Jardine', 'subtitles': '中英双字幕', 'IMDB_socre': '7.5/10 from 4,418 users', 'conutry': '美国', 'placard': 'https://public.lightpic.info/image/5D0C_597FDBD70.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp4 = {'director': 'Raul Merida ....Teniente Conte', 'language': '西班牙语', 'resolution': '93分钟', 'type': '[敌对区域][BD-mkv.720p.中英双字][2017年剧情战争] ', 'trans_name': '敌对区域', 'publish': '分\xa0 6.8/10 from 289 users', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': 'Ariadna Gil ....Capitan Varela', 'level': '剧情/战争', 'size': 'Adolfo Martinez Perez', 'screenshot': 'https://public.lightpic.info/image/65CC_598093670.jpg', 'format': '1CD', 'douban_score': '1280 x 720', 'name': 'Zona hostil / rescue under fire', 'actors': '\u3000Roberto alamo ....Capitan Torres\nRaul Merida ....Teniente Conte\nRoberto alamo ....Capitan Torres\nAntonio Garrido ....Comandante Ledesma\nIngrid Garcia Jonsson ....Cabo Sanchez\nJacobo Dicenta ....Sargento 1o Aguilar\nIsmael Martinez ....Cabo 1o Carranza\nNasser Saleh ....Alferez Abda\nMariam Hernandez ....Sargento Castro\nRuth Gabriel ....Brigada Alvite\nYounes Bachir ....Soldado Rashid\nDavid de la Torre ....Soldado Vazquez\nJavier Bodalo ....Cabo Angulo\nBerta Hernandez ....Cabo Sobrino\nSergio Momo ....Soldado Hunt\nLeander Vyvey ....Soldado Norris\nAdolfo Martin Vela ....Teniente Vilches\nRichard Calderon ....Soldado Pe?a\nJose Luis Casado ....Brigada Rodriguez\nAntonio Cifo ....General Zarate\nVicente Ayala ....Coronel Bermudez\nAngelo Olivier ....Teniente Coronel Bravo\nJorge Fuentes ....Capitan Machado\nMaykol Hernandez ....Soldado Operador Control\nPedro Vassallo ....Capitan Lazaro\nLeo Rivera ....Capitan Legion', 'subtitles': '中英双字幕', 'IMDB_socre': '4 + AAC', 'conutry': '西班牙', 'placard': 'https://public.lightpic.info/image/7B2E_598093660.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp5 = {'director': '庄鹃瑛 Ball Chuang', 'language': '普通话', 'resolution': '1CD', 'type': '[52赫兹，我爱你][BD-mkv.720p.国语中字][2017年爱情音乐]', 'trans_name': '52 Hz, I Love You', 'publish': '2017-01-26(台湾)/2017-06-16(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '魏德圣 Te-Sheng Wei', 'level': '爱情/音乐', 'size': '109分钟', 'screenshot': 'https://public.lightpic.info/image/1D43_5981E9240.jpg', 'format': '1280 x 720', 'douban_score': 'x264 + AAC', 'name': '52赫兹，我爱你/52Hz我爱你/52赫茲，我愛你', 'actors': '\u3000林忠谕 Lin Chungyu\n林忠谕 Lin Chungyu\n姜圣民 Shengmin Jiang\n陈玫希 Mify Chen\n赵咏华 Cyndi Chaw\n林庆台 Ching-tai Lin\n张榕容 Sandrine Pinna\n李千娜 Gina Li\n马如龙 Ju-Lung Ma\n沛小岚 Hsiao-Lan Pei\n范逸臣 Van Fan\n田中千绘 Chie Tanaka\n马念先 Nien-Hsien Ma\n应蔚民 Wei-min Ying\n民雄 Min-Hsiung\n林晓培 Shino Lin\n安乙荞 Joanne Yang', 'subtitles': '中文', 'IMDB_socre': '6.8/10 from 190 users', 'conutry': '中国台湾', 'placard': 'https://public.lightpic.info/image/4353_5981E9240.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp6 = {'director': '杨幂 Mi Yang', 'language': '普通话', 'resolution': '1CD', 'type': '[逆时营救][HD-mkv.720p.国语中字][2017年杨幂霍建华动作科幻]', 'trans_name': 'Fatal Countdown: Reset / Reset', 'publish': '2017-06-19(上海电影节)/2017-06-29(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '尹鸿承 Chang', 'level': '动作/科幻', 'size': '106分钟', 'screenshot': 'https://public.lightpic.info/image/A8FF_597F29320.jpg', 'format': '1280 x 720', 'douban_score': 'x264 + AAC', 'name': '逆时营救/致命倒数', 'actors': '\u3000霍建华 Wallace Huo\n霍建华 Wallace Huo\n金士杰 King Shih-Chieh\n刘畅 Chang Liu\n张艺瀚\xa0 Hummer\n王俐丹 Lidan Wang', 'subtitles': '中文', 'IMDB_socre': '6.1/10 from 76 users', 'conutry': '中国', 'placard': 'https://public.lightpic.info/image/B3CC_597F29310.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp7 = {'director': '程伟豪 Wei-hao Cheng', 'language': '普通话', 'resolution': '1280 x 720', 'type': '[目击者之追凶][HD-mkv.720p.国语中字][2017年悬疑惊悚]', 'trans_name': '目击者之追凶/目擊者', 'publish': '2017-03-31(中国台湾)/2017-06-21(上海电影节)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '113分钟', 'level': '犯罪/悬疑/惊悚', 'size': '1CD', 'screenshot': 'https://public.lightpic.info/image/E256_597B4D060.jpg', 'format': 'x264 + AAC', 'douban_score': '7.4/10 from 228 users', 'name': 'Who Killed Cock Robin', 'actors': '\u3000许玮甯 Tiffany Hsu\n柯佳嬿 Alice Ko\n庄凯勋 Cash Chuang\n李铭顺 Christopher Lee Ming Shun\n李淳 Mason Lee\nIan Chen\n郑志伟 Chih-Wei Cheng\n汤志伟 Chih Wei Tang\nMario Pu', 'subtitles': '中文', 'IMDB_socre': '7.5/10 from 217 users', 'conutry': '中国台湾', 'placard': 'https://public.lightpic.info/image/82EB_597B4D060.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp8 = {'director': '徐浩峰 Haofeng Xu', 'language': '普通话', 'resolution': '1280 x 720', 'type': '[师父/师傅][BD-mkv.720p.国语中字][2015年高分获奖动作]', 'trans_name': '师父/师傅', 'publish': '2015-11-11(台北金马影展)/2015-12-10(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2015', 'duration': '109分钟', 'level': '剧情/动作/武侠', 'size': '1CD', 'screenshot': 'https://public.lightpic.info/image/4AA4_597D9E790.jpg', 'format': 'x264 + AAC', 'douban_score': '8.1/10 from 138,157 users', 'name': 'The Final Master / The Master', 'actors': '\u3000廖凡 Fan Liao\n宋佳 Jia Song\n蒋雯丽 Wenli Jiang\n金士杰 Shi-Jye Jin\n宋洋 Yang Song\n黄觉 Jue Huang\n麦迪娜 Vicky\n张傲月 Aoyue Zhang\n马君 Jun Ma\n陈观泰 Kuan Tai Chen\n熊欣欣 Xinxin Xiong\n戴立忍 Leon Dai\n裘继戎 Jirong Qiu\n李博 Bo Li', 'subtitles': '中文', 'IMDB_socre': '7.2/10 from 1,035 users', 'conutry': '中国', 'placard': 'https://public.lightpic.info/image/6C79_597D9FFC0.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp9 = {'director': '刘紫微 Ziwei Liu', 'language': '剧情', 'resolution': '1280 x 720', 'type': '[我心雀跃][HD-mkv.720p.国语中字][2017年获奖剧情]', 'trans_name': '', 'publish': '中文', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '我心雀跃', 'duration': '95分钟', 'level': '中国', 'size': '1CD', 'screenshot': 'https://public.lightpic.info/image/15AB_597B4D060.jpg', 'format': 'x264 + AAC', 'douban_score': '6.7/10 from 1,811 users', 'name': 'My Heart Leaps Up', 'actors': '\u3000孙伊涵 Yihan Sun\n宋宁 Ning Song\n周楚楚 Chu-chu Zhou\n杜双宇 Shuangyu Du\n刘锐 Kobe Liu\n池韵 Yun Chi\n刘北妍 Beiyan Liu\n任运杰 Yunjie Ren\n修健 Jian Xiu', 'subtitles': '普通话', 'IMDB_socre': '6-06-14(上海国际电影节)/2017-06-09(中国)', 'conutry': '2016', 'placard': 'https://public.lightpic.info/image/C24D_597B4D060.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp10 = {'director': '查理·汉纳姆 Charlie Hunnam ', 'language': '动作/奇幻/冒险 ', 'resolution': '1CD', 'type': '[亚瑟王：斗兽争霸][BD-mkv.720p.中英双字][2017年奇幻动作] ', 'trans_name': '', 'publish': '中英双字幕 ', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': 'King Arthur: Legend of the Sword ', 'duration': '盖·里奇 Guy Ritchie ', 'level': '美国 ', 'size': '126分钟 ', 'screenshot': 'https://public.lightpic.info/image/68F0_5979DCC50.jpg', 'format': '1280 x 720', 'douban_score': 'x264 + AAC', 'name': '亚瑟王：斗兽争霸/亚瑟王：圣剑传奇/亚瑟：王者之剑(台)/神剑亚瑟王(港)/亚瑟王：圆桌骑士/亚瑟王：剑之传奇/亚瑟王：石中剑传说/新亚瑟王/圆桌骑士 ', 'actors': '\u3000裘德·洛 Jude Law \n裘德·洛 Jude Law \n阿斯特丽德·伯格斯-弗瑞斯贝 àstrid Bergès-Frisbey \n米卡埃尔·佩斯布兰特 Mikael Persbrandt \n杰曼·翰苏 Djimon Hounsou \n安娜贝拉·沃丽丝 Annabelle Wallis \n艾瑞克·巴纳 Eric Bana \n艾丹·吉伦 Aidan Gillen \n尼尔·马斯克尔 Neil Maskell \n赫敏·科菲尔德 Hermione Corfield \n凯蒂·麦克格拉思 Katie McGrath \n杰奎·安斯蕾 Jacqui Ainsley \n弗莱迪·福克斯 Freddie Fox \n波比·迪瓦伊 Poppy Delevingne \n朱利安·西格尔 Julian Seager \n大卫·贝克汉姆 David Beckham \n杰夫·贝尔 Geoff Bell \n米莉·布拉迪 Millie Brady \n乔治娜·坎贝尔 Georgina Campbell \n丹尼尔·斯蒂森 Daniel Stisen \n伊琳·珀威尔 Eline Powell \n迈克尔·麦克埃尔哈顿 Michael McElhatton \n阿德里安·布薛特 Adrian Bouchet \n彼得·费迪南多 Peter Ferdinando \n汤姆·吴 Tom Wu \n金斯利·本-阿德 Kingsley Ben-Adir \n盖·里奇 Guy Ritchie ', 'subtitles': '英语 ', 'IMDB_socre': '.2/10 from 50,624 users ', 'conutry': '2017 ', 'placard': 'https://public.lightpic.info/image/FA4F_595920430.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp11 = {'director': '张孝全 Hsiao-chuan Chang', 'language': '普通话', 'resolution': '100分钟', 'type': '[指甲刀人魔][BD-mkv.720p.国语中字][2017年周冬雨张孝全爱情喜剧]', 'trans_name': '指甲刀人魔', 'publish': '2017-04-11(北京电影节)/2017-04-14(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '周冬雨 Dongyu Zhou', 'level': '喜剧/爱情', 'size': '关智耀 Jason Kwan Chi-Yiu', 'screenshot': 'https://public.lightpic.info/image/B137_596B4F690.jpg', 'format': '1CD', 'douban_score': '1280 x 720', 'name': 'A Nail Clipper Romance', 'actors': '\u3000纳豆 Na Dow\n张孝全 Hsiao-chuan Chang\n纳豆 Na Dow\n林辰唏 Zaizai Lin\n蔡洁 Jacky Cai\n盛朗熙 Joy Sheng\n郑伊健 Ekin Cheng\n谢依霖 Yilin Sie\n许玮甯 Tiffany Hsu', 'subtitles': '中文', 'IMDB_socre': '4 + aac', 'conutry': '中国/中国香港', 'placard': 'https://public.lightpic.info/image/8E19_590060000.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp12 = {'director': '新海诚 Makoto Shinkai', 'language': '日语', 'resolution': '1280 x 720', 'type': '[你的名字。][HD-mkv.720p.日语中字][2016年高分获奖动画]', 'trans_name': '你的名字。/你的名字/君之名', 'publish': '2016-08-26(日本)/2016-12-02(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2016', 'duration': '106分钟', 'level': '剧情/爱情/动画', 'size': '1CD', 'screenshot': 'https://public.lightpic.info/image/9035_5977ECF20.jpg', 'format': 'x264 + AAC', 'douban_score': '8.5/10 from 367,630 users', 'name': '君の名は。/Your Name', 'actors': '\u3000神木隆之介 Ry?nosuke Kamiki\n上白石萌音 Mone Kamishiraishi\n长泽雅美 Masami Nagasawa\n市原悦子 Etsuko Ichihara\n成田凌 Ryo Narita\n悠木碧 Aoi Yuki\n岛崎信长 Nobunaga Shimazaki\n石川界人 Kaito Ishikawa\n谷花音 Tani Kanon', 'subtitles': '中文', 'IMDB_socre': '8.5/10 from 41,821 users', 'conutry': '日本', 'placard': 'https://public.lightpic.info/image/3277_5977ECF10.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp13 = {'director': '乔什·哈奈特 Josh Hartnett', 'language': '英语', 'resolution': '1CD', 'type': '[奥斯曼中尉][BD-mkv.720p.中英双字][2017年高分剧情战争]', 'trans_name': '奥斯曼中尉', 'publish': '2017-03-10(美国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '约瑟夫·鲁本 Joseph Ruben', 'level': '剧情/战争', 'size': '106分钟', 'screenshot': 'https://public.lightpic.info/image/0C30_5977ECF20.jpg', 'format': '1280 x 720', 'douban_score': 'x264 + AAC', 'name': 'The Ottoman Lieutenant', 'actors': '\u3000米契尔·哈思曼 Michiel Huisman\n米契尔·哈思曼 Michiel Huisman\n哈鲁克·比尔根纳尔 Haluk Bilginer\n塞尔柱克.约奈坛 Selcuk Yontem\n海拉·西尔玛 Hera Hilmar', 'subtitles': '中英双字幕', 'IMDB_socre': '8.4/10 from 13,045 users', 'conutry': '土耳其/美国', 'placard': 'https://public.lightpic.info/image/B4D3_59769F3D0.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp14 = {'director': '王泊文 Bowen Wang', 'language': '普通话', 'resolution': '1CD', 'type': '[无罪之城][HD-mkv.720p.国语中字][2017年动作]', 'trans_name': '无罪之城', 'publish': '2017-07-22(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '尹晨阳', 'level': '动作/犯罪', 'size': '70分钟', 'screenshot': 'https://public.lightpic.info/image/A739_59774A5B0.jpg', 'format': '1280 x 720', 'douban_score': 'x264 + AAC', 'name': 'The Innocent City', 'actors': '\u3000谭盐盐\n谭盐盐\n赵怀良\n郭震 Zhen Guo', 'subtitles': '中文', 'IMDB_socre': '/10 from 178 users', 'conutry': '中国', 'placard': 'https://public.lightpic.info/image/77F9_59774B090.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
# temp15 = {'director': '陈正道 Leste Chen', 'language': '普通话', 'resolution': '1280 x 720', 'type': '[记忆大师][HD-mkv.720p.国语中字][2017年黄渤徐静蕾悬疑惊悚]', 'trans_name': '记忆大师/记忆战/催眠大师2', 'publish': '2017-04-23(北京电影节)/2017-04-28(中国)', 'ftpurl': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8035/[阳光电影www.ygdy8.com].英雄联盟.HD.720p.英语中字.mkv', 'decade': '2017', 'duration': '119分钟', 'level': '剧情/犯罪/悬疑/惊悚', 'size': '1CD', 'screenshot': 'https://public.lightpic.info/image/9FC6_59774A5B0.jpg', 'format': 'x264 + AAC', 'douban_score': '7.3/10 from 89,671 users', 'name': 'Battle of Memories', 'actors': '\u3000黄渤 Bo Huang\n徐静蕾 Jinglei Xu\n段奕宏 Yihong Duan\n杨子姗 Zishan Yang\n许玮宁 Tiffany Hsu\n梁杰理\n王真儿 Zhen Wang\n杜函梦 Hanmeng Du', 'subtitles': '中文', 'IMDB_socre': '6.9/10 from 206 users', 'conutry': '中国', 'placard': 'https://public.lightpic.info/image/C8C0_59774B090.jpg', 'dytt8_url':'http://www.dytt8.net/html/gndy/dyzz/20170223/53313.html'}
#
#
#
# TaskQueue.getContentQueue().put(temp1)
# TaskQueue.getContentQueue().put(temp2)
# TaskQueue.getContentQueue().put(temp3)
# TaskQueue.getContentQueue().put(temp4)
# TaskQueue.getContentQueue().put(temp5)
# TaskQueue.getContentQueue().put(temp6)
# TaskQueue.getContentQueue().put(temp7)
# TaskQueue.getContentQueue().put(temp8)
# TaskQueue.getContentQueue().put(temp9)
# TaskQueue.getContentQueue().put(temp10)
# TaskQueue.getContentQueue().put(temp11)
# TaskQueue.getContentQueue().put(temp12)
# TaskQueue.getContentQueue().put(temp13)
# TaskQueue.getContentQueue().put(temp14)
# TaskQueue.getContentQueue().put(temp15)
#
# DBName = 'dytt.db'
# db = sqlite3.connect('./'+DBName, 10)
# conn = db.cursor()
#
# SelectSql = 'Select * from sqlite_master where type = "table" and name="lastest_moive";'
# CreateTableSql = '''
#     Create Table lastest_moive (
#         'm_id' INTEGER PRIMARY KEY,
#         'm_type' varchar(100),
#         'm_trans_name' varchar(200),
#         'm_name' varchar(100),
#         'm_decade' varchar(30),
#         'm_conutry' varchar(30),
#         'm_level' varchar(100),
#         'm_language' varchar(30),
#         'm_subtitles' varchar(100),
#         'm_publish' varchar(30),
#         'm_IMDB_socre' varchar(50),
#         'm_douban_score' varchar(50),
#         'm_format' varchar(20),
#         'm_resolution' varchar(20),
#         'm_size' varchar(10),
#         'm_duration' varchar(10),
#         'm_director' varchar(50),
#         'm_actors' varchar(1000),
#         'm_placard' varchar(200),
#         'm_screenshot' varchar(200),
#         'm_ftpurl' varchar(200),
#         'm_dytt8_url' varchar(200)
#     );
# '''
#
# InsertSql = '''
#     Insert into lastest_moive(m_type, m_trans_name, m_name, m_decade, m_conutry, m_level, m_language, m_subtitles, m_publish, m_IMDB_socre,
#     m_douban_score, m_format, m_resolution, m_size, m_duration, m_director, m_actors, m_placard, m_screenshot, m_ftpurl,
#     m_dytt8_url)
#     values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
# '''
# #            'm_id' int auto_increment,
# if not conn.execute(SelectSql).fetchone():
#     conn.execute(CreateTableSql)
#     db.commit()
#     print('====  创建表成功  ====')
# else :
#     print('====  创建表失败, 表已经存在  ====')
#
# count = 1
#
# while not TaskQueue.isContentQueueEmpty():
#     item = TaskQueue.getContentQueue().get()
#     conn.execute(InsertSql, Utils.dirToList(item))
#     db.commit()
#     print('插入第 ' + str(count) + ' 条数据成功')
#     count = count + 1
#
# db.commit()
# db.close()


# #测试案例3
# DBName = 'dytt.db'
# db = sqlite3.connect('./'+DBName, 10)
# conn = db.cursor()
#
# curser = conn.execute("SELECT m_actors FROM lastest_moive WHERE m_name = 'Baahubali: The Conclusion';")
# print(curser.fetchone())


# 测试案例4
# '''
# 有点,  解析失败
# Top 子线程 0 请求【 http://www.dytt8.net/html/gndy/dyzz/20170713/54501.html 】的结果： 200
# Top 子线程 0 请求【 http://www.dytt8.net/html/gndy/dyzz/20170514/53986.html 】的结果： 200
# Top 子线程 0 请求【 http://www.dytt8.net/html/gndy/dyzz/20170413/53726.html 】的结果： 200
# Top 子线程 4 请求【 http://www.dytt8.net/html/gndy/dyzz/20170327/53562.html 】的结果： 200
# Top 子线程 0 请求【 http://www.dytt8.net/html/gndy/dyzz/20170310/53447.html 】的结果： 200
# Top 子线程 0 请求【 http://www.dytt8.net/html/gndy/dyzz/20170310/53446.html 】的结果： 200
#
# Top 子线程 0 请求【 http://www.dytt8.net/html/gndy/dyzz/20170414/53727.html 】的结果： 200
# Top 子线程 2 请求【 http://www.dytt8.net/html/gndy/dyzz/20170318/53507.html 】的结果： 200
# '''
url = 'http://www.dytt8.net/html/gndy/dyzz/20170713/54501.html'
response = requests.get(url, headers=RequestModel.getHeaders(), proxies=RequestModel.getProxies(), timeout=3)
print(' 请求【 ' + url + ' 】的结果： ' + str(response.status_code))
response.encoding = 'GBK'
selector = etree.HTML(response.text)
# print(response.text)
content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/div/text()")
# 匹配出来有两张图片, 第一张是海报, 第二张是电影画面截图
imgs = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/p/img/@src")
print(content)
