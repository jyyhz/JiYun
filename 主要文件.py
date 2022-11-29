import requests as re
from time import *
from random import *
import json as j
from PIL import Image, ImageFont, ImageDraw
import string
d1ct = {'圣剑': 300, '魔刀': 310, '天地斧': 325, '雷神锤': 300, '加特林': 260, '巴雷特': 390,'无':0}
f = ''
fblb = ['圣剑之堡','火上郊游','水上乐园','孤狼沙漠','高风险地区','柠檬圣地','芒果小岛','宝藏龙窟','魔法神镇','孤狼沙漠']
jysdwp = {'体力药':110,'生命药':90,'武力药水':70}
shijian = strftime('%Y-%m-%d %H:%M:%S')
qqgid = '323667525'
botqq = 647013710
gly = [1497703235, 3409374044, 2504735026]
bj2 = ''
ddts = 0
cs = 0
ddsj = 0
xxi = re.post(
    'http://127.0.0.1:5700/get_group_msg_history?group_id={}'.format(qqgid)).json()
zh = [
    'sb', 'SB', '傻逼', '尼玛', '你妈', '泥马', '卧槽', '我操', '握草', '我草', '草人', '日人', 'woc', 'wc', 'fuck', 'fxxk', 'f**k', 'sabi', 'NB', 'nb', 'tm', 'TM', '他妈', '踏马', '艹']
p123 = 1

def js():
    global xxi
    xxi["data"]["messages"][-1]["post_type"] = 'message_sent'


def fs(msg, at=False):
    if at == False:
        re.post(
            'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(qqgid, msg)).json()
    else:
        re.post(
            'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(qqgid, '[CQ:at,qq='+str(xxi["data"]["messages"][-1]["sender"]["user_id"])+']'+msg)).json()
    print("[{0}] [send msg info] 发送群{2}消息：{1}".format(shijian, msg, qqgid))
    js()
fs('极韵AI已经开启')
while True:
    try:
        while True:
            f = ''
            shijian = strftime('%Y-%m-%d %H:%M:%S')
            try:
                r = open('D:/qqbot_image/自定义.txt', 'r+', encoding='ANSI')
                rfd = eval(r.readlines()[-1])
            except:
                rfd = {'测试':'测试'}
            xxi = re.post(
                'http://127.0.0.1:5700/get_group_msg_history?group_id={}'.format(qqgid)).json()
            for i in xxi["data"]["messages"]:
                bj1 = xxi["data"]["messages"][-1]["message"]
                if bj1 == bj2:
                    pass
                elif bj1 != bj2 and xxi["data"]["messages"][-1]["post_type"] == "message":
                    bj2 = xxi["data"]["messages"][-1]["message"]
                    print('[{0}] [get msg info] 收到群{4}中的成员{1}(Q号{2})的消息：{3}'.format(shijian, xxi["data"]["messages"][-1]["sender"]["nickname"],xxi["data"]["messages"][-1]["sender"]["user_id"], xxi["data"]["messages"][-1]["message"],qqgid))
                if '你好' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs('你好')
                if '极韵系统' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    lb = [
                        '版本信息--------------查看版本信息',
                        '极韵系统--------------打开这张图片',
                        '你好------------------回复“你好”',
                        '脏话--------回复“禁止说脏话”加禁言',
                        '@机器人-----------回复“叫我干嘛”',
                        '禁言@人*分钟--------------禁言某人',
                        '禁言@人*0分钟-------------解禁某人',
                        '说*内容------------------发送语音',
                        '管理员列表-----------获取管理员列表',
                        '获取*http://网站-------获取网站长图',
                        '新增回复+指令+内容---自定义机器人回复',
                        '踢出@人-----------------踢出某人',
                        '当前时间--------------获取当前时间'
                    ]
                    im = Image.new('RGB', (1350, (len(lb)+1)*70), (255, 255, 255))
                    jp = ImageDraw.Draw(im)
                    fo = ImageFont.truetype(
                        font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                    jp.text((0, 0), '机器人指令:', (68, 204, 255), font=fo)
                    for i in range(1, len(lb)+1):
                        jp.text((0, i*70), lb[i-1], (68, 204, 255), font=fo)
                    im.save(
                        'C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                    fs('[CQ:image,file=gx.png]')
                if '版本信息' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs('版本：2.98')
                if '[CQ:at,qq=647013710]' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs('叫我干嘛')
                if '禁言[CQ:at,qq=' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    try:
                        jyqq = xxi["data"]["messages"][-1]["message"].split('qq=')[-1].split('] ')[0]
                        jyfz = xxi["data"]["messages"][-1]["message"].split('*')[1].split('分钟')[0]
                    except:
                        fs('禁言失败',at=True)
                    else:
                        if xxi["data"]["messages"][-1]["sender"]["user_id"] in gly:
                            fd12 = re.get(
                                'http://127.0.0.1:5700/set_group_ban?group_id={0}&user_id={1}&duration={2}'.format(qqgid,str(jyqq), str(int(jyfz)*60))).json()
                            if fd12["status"] == "ok":
                                if jyfz == '0':
                                    fs('解禁成功',at=True)
                                else:
                                    fs('禁言成功',at=True)
                            if fd12.get("wording") != None:
                                if fd12["wording"] == "机器人权限不足":
                                    fs('无法禁言群主或其他管理员',at=True)
                                else:
                                    fs('禁言失败',at=True)
                        else:
                            fs('您的权限不足',at=True)
                if '说*' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs('[CQ:tts,text={}]'.format(
                        xxi["data"]["messages"][-1]["message"].split('*')[-1]))
                for ve in zh:
                    if ve in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                        re.get(
                            'http://127.0.0.1:5700/set_group_ban?group_id={0}&user_id={1}&duration={2}'.format(qqgid,str(xxi["data"]["messages"][-1]["sender"]["user_id"]),p123*5*12*5))
                        re.get('http://127.0.0.1:5700/delete_msg?message_id={}'.format(str(xxi["data"]["messages"][-1]["message_id"])))
                        fs('禁止说脏话',at=True)
                        p123 += 1
                if '管理员列表' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs(str(gly).split('[')[1].split(']')[0])
                if '获取*' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    try:
                        msg = xxi["data"]["messages"][-1]["message"].split(
                            '*')[-1]
                    except:
                        fs('获取失败，可能是格式错误',at=True)
                    else:
                        fs('[CQ:image,file={0}.image,url=http://image.thum.io/get/fullpage/{1}]'.format(msg.split('http://')[0],msg))
                if '踢出[CQ:at,qq=' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    try:
                        try:
                            tcqq = xxi["data"]["messages"][-1]["message"].split('踢出[CQ:at,qq=')[1].split(']')[0]
                        except:
                            fs('踢群失败，可能是格式错误',at=True)
                        else:
                            trxx = re.post('http://127.0.0.1:5700/set_group_kick?group_id={0}&user_id={1}'.format(qqgid,tcqq))
                            if trxx["wording"] == "机器人权限不足":
                                fs('无法踢出群主或其他管理员',at=True)
                            if trxx["status"] == "ok":
                                fs('踢群成功！',at=True)
                    except:
                        fs('踢群失败',at=True)
                if '新增回复+' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    try:
                        zl = xxi["data"]["messages"][-1]["message"].split('+')[1]
                        hf = xxi["data"]["messages"][-1]["message"].split('+')[2]
                    except:
                        fs('增添失败，可能是格式错误',at=True)
                    else:
                        with open('D:/qqbot_image/自定义.txt','r+') as f:
                            try:
                                dq = eval(f.readlines()[-1])
                                f.close()
                            except Exception as exe:
                                dq = {}
                        with open('D:/qqbot_image/自定义.txt', 'w+') as f:
                            dq[zl] = hf
                            f.write(str(dq))
                            f.close()
                        fs('增添成功',at=True)
                if xxi["data"]["messages"][-1]["message"] in rfd.keys() and xxi["data"]["messages"][-1]["post_type"] == "message":
                    index = eval(str(rfd.keys()).split('(')[1].split(')')[0]).index(xxi["data"]["messages"][-1]["message"])
                    fs(eval(str(rfd.values()).split('(')[1].split(')')[0])[index])
                if '当前时间' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs(shijian, at=True)
                if '我的小兵' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fd3 = xxi["data"]["messages"][-1]["sender"]["user_id"]
                    fdfdfd3 = {'good':'正常','die':'死亡'}
                    fdfdfd = open(
                        'D:/qqbot_image/{}游戏数据.json'.format(qqgid))
                    dict = eval(fdfdfd.read())
                    lb = ['您的小兵等级:'+str(dict[str(fd3)]['tity']) +'级',
                          '武力值:'+str(dict[str(fd3)]["force"]),
                          '体力:'+str(dict[str(fd3)]["phystr"])+'/100',
                          '状态:'+fdfdfd3[str(dict[str(fd3)]["state"])],
                          '神器:'+dict[str(fd3)]["artt"],
                          '神力:'+dict[str(fd3)]["supow"],
                          '血量:'+str(dict[str(fd3)]["blov"]) ]
                    im = Image.new(
                        'RGB', (800, (len(lb)+1)*71), (255, 255, 255))
                    jp = ImageDraw.Draw(im)
                    fo = ImageFont.truetype(
                        font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                    jp.text((0, 0), '您的小兵:', (68, 204, 255), font=fo)
                    for i in range(1, len(lb)+1):
                        jp.text((0, i*70), lb[i-1], (68, 204, 255), font=fo)
                    im.save('C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                    fs('[CQ:image,file=gx.png]', at=True)
                if '小兵系统' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    lb = [
                        '极韵商店---------------查看商店内容',
                        '我的资产----------产看自己的金币',
                        '打工-------------获得20-30金币',
                        '升级小兵----------------',
                        '花费100金币买一个小兵,同时武力也会增加',
                        '使用xx ------------使用一个xx物品',
                        '购买xx*x------------购买xx物品x个',
                        '充值--------------在小兵系统里充值',
                        '进入副本----------------进入某个副本',
                        '副本列表----------------获取副本列表'
                        ]
                    im = Image.new('RGB', (1350, (len(lb)+1)*71), (68, 204, 255))
                    jp = ImageDraw.Draw(im)
                    fo = ImageFont.truetype(
                        font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                    jp.text((0, 0), '小兵系统:', (255, 255, 255), font=fo)
                    for i in range(1, len(lb)+1):
                        jp.text((0, i*70), lb[i-1], (255, 255, 255), font=fo)
                    im.save('C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                    fs('[CQ:image,file=gx.png]', at=True)
                if '我的资产' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fdfdfd = open(
                        'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                    fd123 = fdfdfd.read()
                    fd123 = eval(fd123)
                    lb = [
                        '您有' +
                        str(fd123[str(xxi["data"]["messages"][-1]
                            ["sender"]["user_id"])]['coin'])+'个极韵币'
                    ]
                    im = Image.new(
                        'RGB', (800, (len(lb)+1)*71), (255, 255, 255))
                    jp = ImageDraw.Draw(im)
                    fo = ImageFont.truetype(
                        font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                    jp.text((0, 0), '您的资产:', (68, 204, 255), font=fo)
                    for i in range(1, len(lb)+1):
                        jp.text((0, i*70), lb[i-1], (68, 204, 255), font=fo)
                    im.save(
                        'C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                    fs('[CQ:image,file=gx.png]', at=True)
                if '打工' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fdfdfd = open('D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                    fd123 = eval(fdfdfd.read())
                    if fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["phystr"] >= 5:
                        hdjb = randint(
                            round(fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["force"]*0.5), round(fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["force"]*0.5+20))
                        fs('的小兵出去打工啦\n获得了'+str(hdjb)+'个极韵币\n但是耗费了5点体力', at=True)
                        fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["coin"] += hdjb
                        fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["phystr"] -= 5
                        fdfdfd1 = open('D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                        fdfdfd1.write(str(fd123))
                        fdfdfd1.close()
                    elif fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["phystr"] <= 0:
                        fs('体力不足，请补充体力',at=True)
                if '升级小兵' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fdfdfd = open(
                        'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                    fd123 = eval(fdfdfd.read())
                    fdfdfd.close()
                    if fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["coin"] < fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["tity"]*50:
                        fs('金币不足，无法升级', at=True)
                    elif fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["coin"] >= 100:
                        hdjb = 1
                        fs('成功花费'+str(fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["tity"]*50)+'个极韵币购买了一个小兵', at=True)
                        fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["tity"] += hdjb
                        fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["force"] += randint(10,15)
                        fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["coin"] -= fd123[str(
                            xxi["data"]["messages"][-1]["sender"]["user_id"])]["tity"]*50
                        fdfdfd1 = open(
                            'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                        fdfdfd1.write(str(fd123))
                        fdfdfd1.close()
                if '购买' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    try:
                        wp = xxi["data"]["messages"][-1]["message"].split('购买')[1].split('*')[0]
                        wpsl = xxi["data"]["messages"][-1]["message"].split('购买')[1].split('*')[1]
                        wpsl = int(wpsl)
                    except:
                        fs('购买失败，可能是格式错误',at=True)
                    else:
                        if wp not in jysdwp:
                            fs('物品不存在', at=True)
                        else:
                            fdfdfd = open(
                                'D:/qqbot_image/{}游戏背包数据.json'.format(qqgid), 'r')
                            fdfdfd3 = open(
                                'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                            fd123 = eval(fdfdfd.read())
                            fd1234 = eval(fdfdfd3.read())
                            fdfdfd.close()
                            if fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["coin"] < jysdwp[wp]:
                                fs('极韵币不足，无法购买',at=True)
                            else:
                                hdjb = 1
                                fs('成功购买了{}'.format(wp), at=True)
                                try:
                                    fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])][wp] += wpsl
                                except KeyError:
                                    fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])][wp] = wpsl
                                finally:
                                    fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['coin'] -= jysdwp[wp]
                                fdfdfd1 = open(
                                    'D:/qqbot_image/{}游戏背包数据.json'.format(qqgid), 'w')
                                fdfdfd1.write(str(fd123))
                                fdfdfd1.close()
                                fdfdfd1 = open(
                                    'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                                fdfdfd1.write(str(fd1234))
                                fdfdfd1.close()
                if '使用' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    wp = xxi["data"]["messages"][-1]["message"].split('使用')[-1]
                    fdfdfd = open(
                        'D:/qqbot_image/{}游戏背包数据.json'.format(qqgid), 'r')
                    fdfdfd2 = open(
                        'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                    fd123 = eval(fdfdfd.read())
                    fd1234 = eval(fdfdfd2.read())
                    fdfdfd.close()
                    fdfdfd2.close()
                    wow = fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]
                    if wow == {}:
                        fs('您的背包空空如也哦',at=True)
                    elif wow != {} and fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])].get(wp) == None or fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])].get(wp) <= 0:
                        fs('您的背包里没有这件物品', at=True)
                        print(wow)
                        print(fd123[str(xxi["data"]["messages"]
                              [-1]["sender"]["user_id"])].get(wp))
                        print(fd123[str(xxi["data"]["messages"]
                              [-1]["sender"]["user_id"])].get(wp))
                    elif wow != {} and fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])].get(wp) != None:
                        if wp == '体力药' and fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["phystr"] <= 50:
                            fdfdfd1 = open(
                                'D:/qqbot_image/{}游戏背包数据.json'.format(qqgid), 'w')
                            fdfdfd = open(
                                'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                            fd123[str(xxi["data"]["messages"][-1]
                                      ["sender"]["user_id"])][wp] -= 1
                            fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['phystr'] += 50
                            fdfdfd1.write(str(fd123))
                            fdfdfd.write(str(fd1234))
                            fs('使用成功，已恢复50%体力',at=True)
                            fdfdfd.close()
                            fdfdfd1.close()
                        elif wp == '体力药' and fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["phystr"] > 50:
                            fs('您的小兵无需恢复体力',at=True)
                        if wp == '生命药':
                            fdfdfd1 = open(
                                'D:/qqbot_image/{}游戏背包数据.json'.format(qqgid), 'w')
                            fdfdfd = open(
                                'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                            fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])][wp] -= 1
                            fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov'] += 75
                            fdfdfd1.write(str(fd123))
                            fdfdfd.write(str(fd1234))
                            fs('使用成功，已恢复75点血量', at=True)
                            fdfdfd.close()
                            fdfdfd1.close()
                        elif wp == '生命药' and fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]["phystr"] >= 100:
                            fs('您的小兵无需恢复血量', at=True)
                        if wp == '武力药水':
                            fdfdfd1 = open(
                                'D:/qqbot_image/{}游戏背包数据.json'.format(qqgid), 'w')
                            fdfdfd = open(
                                'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                            fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])][wp] -= 1
                            if fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])][wp] == 0:
                                del fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])][wp]
                            fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['force'] += 25
                            fdfdfd1.write(str(fd123))
                            fdfdfd.write(str(fd1234))
                            fs('使用成功，已增加25点武力', at=True)
                            fdfdfd.close()
                            fdfdfd1.close()
                if '极韵商店' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    lb=[
                      '体力药------------------110极韵币',
                      '(物品说明:恢复50%体力)',
                      '生命药------------------90极韵币',
                      '(物品说明:恢复75点血量)',
                      '武力药水----------------70极韵币',
                      '(物品说明:提升25点武力值)'
                        ]
                    im=Image.new('RGB', (1350, (len(lb)+2)*70), (255, 255, 255))
                    jp=ImageDraw.Draw(im)
                    fo=ImageFont.truetype(font = 'C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size = 70)
                    jp.text((0, 0), '极韵商店:', (68, 204, 255), font = fo)
                    for i in range(1, len(lb)+1):
                        jp.text((0, i*70), lb[i-1], (68, 204, 255), font=fo)
                    jp.text((0, i*70+70), '需要购买说:购买物品*数量', (68, 204, 255), font = fo)
                    im.save('C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                    fs('[CQ:image,file=gx.png]', at=True)
                if '背包' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fdfdfd = open(
                        'D:/qqbot_image/{}游戏背包数据.json'.format(qqgid), 'r')
                    fd123 = eval(fdfdfd.read())
                    lb = ['您的背包:']
                    for woww in fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])].items():
                        lb.append(woww[0] + '*' + str(woww[1]))
                    im = Image.new(
                        'RGB', (800, (len(lb)+2)*71), (255, 255, 255))
                    jp = ImageDraw.Draw(im)
                    fo = ImageFont.truetype(
                                            font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                    jp.text((0, 0), '您的背包:', (68, 204, 255), font=fo)
                    jp.text((0, 70), '==============================', (68, 204, 255), font=fo)
                    for i in range(2, len(lb)+1):
                        jp.text((0, i*70), lb[i-1], (68, 204, 255), font=fo)
                    jp.text((0, i*70+70), '==============================',
                            (68, 204, 255), font=fo)
                    im.save(
                        'C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                    fs('[CQ:image,file=gx.png]', at=True)
                if '奖励极韵币*' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    if xxi["data"]["messages"][-1]["sender"]["user_id"] == 1497703235 or xxi["data"]["messages"][-1]["sender"]["user_id"] == 3409374044:
                        sm = xxi["data"]["messages"][-1]["message"]
                        sl = sm.split('*')[1].split('至')[0]
                        sl = int(sl)
                        fdfdfd = open(
                            'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                        fd1234 = eval(fdfdfd.read())
                        fd123 = open(
                            'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                        fdfdfd.close()
                        qq2 = sm.split('至')[1]
                        if qq2 == 'all':
                            for wowwo in fd1234.keys():
                                fd1234[wowwo]['coin'] += sl
                            fd123.write(str(fd1234))
                            fd123.close()
                            fs('成功奖励给全体成员', at=True)
                        else:
                            qq = sm.split('至[CQ:at,qq=')[1].split(']')[0]
                            fd1234[qq]["coin"] += sl
                            fd123.write(str(fd1234))
                            fd123.close()
                            fs('奖励成功',at=True)
                    else:
                        fs('权限不足',at=True)
                if '出售' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs('敬请期待')
                fdfdfd2 = open('D:/qqbot_image/{}游戏数据.json'.format(qqgid),'r+')
                fd1234 = eval(fdfdfd2.read())
                fdfdfd1 = open('D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                for wowwow in fd1234.keys():
                    if fd1234[wowwow]['blov'] <= 0:
                        if fd1234[wowwow]['blov'] == 0:
                            fd1234[wowwow]['state'] = 'die'
                        else:
                            fd1234[wowwow]['blov'] = 0
                            fd1234[wowwow]['state'] = 'die'
                    if fd1234[wowwow]['blov'] > 100:
                        fd1234[wowwow]['blov'] = 100
                    if fd1234[wowwow]['blov'] >= 0:
                        fd1234[wowwow]['state'] = 'good'
                    fd1234[wowwow]['coin'] = round(fd1234[wowwow]['coin'])
                fdfdfd1.write(str(fd1234))
                if '充值' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fs('请向[CQ:at,qq=1497703235]索要微信群二维码')
                if '进入副本' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fdfdfd = open(
                        'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                    fd123 = eval(fdfdfd.read())
                    fdfdfd1 = open(
                        'D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'w')
                    force = fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['force']
                    dict = {'圣剑之堡': {'m': '圣剑守护者', 'b': 100, 'f': 500}, '宝藏龙窟': {'m': '霸王龙', 'b': 500, 'f': 1000}, '火上郊游': {'m': '火怪', 'b': 60, 'f': 100},
                            '水上乐园': {'m': '水怪', 'b': 75, 'f': 125}, '魔法神镇': {'m': '麻瓜', 'b': 130, 'f': 250}, '高风险地区': {'m': '新冠病毒', 'b': 100000, 'f': 254000},
                            '柠檬圣地': {'m': '檬檬哒', 'b': 50, 'f': 50}, '芒果小岛':{'m': '芒人', 'b':75, 'f': 100}, '孤狼沙漠':{'m': '沙漠孤狼', 'b': 100,'f':100}}
                    jrfb = xxi["data"]["messages"][-1]["message"].split(
                        '进入副本')[-1]
                    if '*' in jrfb:
                        jrfb = jrfb.split('*')
                        cs = jrfb[-1]
                        jrfb = jrfb[0]
                        cs = int(cs)
                    else:
                        cs = 1
                    if jrfb in dict.keys():
                        if dict[jrfb]['f']*cs < force and fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov'] >= dict[jrfb]['b'] and fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['phystr'] >= 5:
                            lb = [
                                '['+str(xxi["data"]["messages"][-1]["sender"]["user_id"])+'的小兵'+'  VS  '+dict[jrfb]['m']+']',
                                '*胜败情况:胜利     *获得极韵币:'+str(round(fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov']*2)*cs),
                                '*消耗体力:5点      *消耗血量:' + str(dict[jrfb]['b'])
                                ]
                            im = Image.new(
                                'RGB', (1350, (len(lb)+1)*70), (255, 255, 255))
                            jp = ImageDraw.Draw(im)
                            fo = ImageFont.truetype(font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                            jp.text((0, 0), '结果:', (68, 204, 255), font=fo)
                            for i in range(1, len(lb)+1):
                                jp.text((0, i*70), lb[i-1], (68, 204, 255), font=fo)
                            im.save('C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                            fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['coin'] += dict[jrfb]['b'] / \
                                1.5 - \
                                fd1234[str(xxi["data"]["messages"][-1]
                                           ["sender"]["user_id"])]['blov']/1.5
                            fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['phystr'] -= 5
                            fd123[str(xxi["data"]["messages"][-1]["sender"]
                                      ["user_id"])]['blov'] -= dict[jrfb]['b']
                        elif fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov'] <= dict[jrfb]['b'] and fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['force'] >= dict[jrfb]['f'] and fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['phystr'] >= 5:
                            if randint(1, 2) == 1:
                                lb = [
                                    '['+str(xxi["data"]["messages"][-1]["sender"]
                                            ["user_id"])+'的小兵'+'  VS  '+dict[jrfb]['m']+']',
                                    '*胜败情况:失败     *失败原因:血量不足',
                                    '*消耗体力:5点      *消耗血量:' + str(dict[jrfb]['b'])
                                ]
                                im = Image.new(
                                    'RGB', (1350, (len(lb)+1)*70), (255, 255, 255))
                                jp = ImageDraw.Draw(im)
                                fo = ImageFont.truetype(
                                                        font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                                jp.text((0, 0), '结果:', (68, 204, 255), font=fo)
                                for i in range(1, len(lb)+1):
                                    jp.text((0, i*70), lb[i-1],
                                            (68, 204, 255), font=fo)
                                im.save(
                                    'C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                                fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['coin'] += dict[jrfb]['b'] / \
                                    1.5 - \
                                    fd1234[str(xxi["data"]["messages"][-1]
                                            ["sender"]["user_id"])]['blov']/1.5
                                fd123[str(xxi["data"]["messages"][-1]
                                        ["sender"]["user_id"])]['phystr'] -= 5
                                fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov'] -= dict[jrfb]['b']-(
                                    dict[jrfb]['b']-fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov'])
                            else:
                                lb = [
                                    '['+str(xxi["data"]["messages"][-1]["sender"]
                                            ["user_id"])+'的小兵'+'  VS  '+dict[jrfb]['m']+']',
                                    '*胜败情况:胜利     *获得极韵币:' +
                                    str(round(
                                        fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov']*2)*cs),
                                    '*消耗体力:5点      *消耗血量:' +
                                    str(dict[jrfb]['b'])
                                    ]
                                im = Image.new(
                                    'RGB', (1350, (len(lb)+1)*70), (255, 255, 255))
                                jp = ImageDraw.Draw(im)
                                fo = ImageFont.truetype(
                                    font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                                jp.text((0, 0), '结果:', (68, 204, 255), font=fo)
                                for i in range(1, len(lb)+1):
                                    jp.text((0, i*70), lb[i-1],
                                            (68, 204, 255), font=fo)
                                im.save(
                                    'C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                                fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['coin'] += dict[jrfb]['b'] / \
                                    1.5 - \
                                    fd1234[str(xxi["data"]["messages"][-1]
                                            ["sender"]["user_id"])]['blov']/1.5
                                fd123[str(xxi["data"]["messages"][-1]
                                        ["sender"]["user_id"])]['phystr'] -= 5
                                fd123[str(xxi["data"]["messages"][-1]["sender"]
                                          ["user_id"])]['blov'] -= dict[jrfb]['b']
                        else:
                            lb = [
                                '['+str(xxi["data"]["messages"][-1]["sender"]
                                        ["user_id"])+'的小兵'+'  VS  '+dict[jrfb]['m']+']',
                                '*胜败情况:失败     *失败原因:武力/血量/精力不足',
                                '*消耗体力:5点      *消耗血量:' +str(dict[jrfb]['b'])
                                ]
                            im = Image.new('RGB', (1350, (len(lb)+1)*70), (255, 255, 255))
                            jp = ImageDraw.Draw(im)
                            fo = ImageFont.truetype(font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                            jp.text((0, 0), '结果:', (68, 204, 255), font=fo)
                            for i in range(1, len(lb)+1):
                                jp.text((0, i*70), lb[i-1],(68, 204, 255), font=fo)
                            im.save('C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                            fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['coin'] += dict[jrfb]['b'] / 1.5 - fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov']/1.5
                            fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['phystr'] -= 5
                            fd123[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['blov'] -= dict[jrfb]['b']
                        fdfdfd1.write(str(fd123))
                        fs('[CQ:image,file=gx.png]')
                if '副本列表' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    lb = ['孤狼沙漠--一只狼在沙漠游荡',
                    '圣剑之堡--圣剑在此堡内 有怪物在守护圣剑',
                    '火上郊游--跟火怪碰碰胆量',
                    '水上乐园--水怪埋伏在内 可以跟它碰碰胆量',
                    '宝藏龙窟--霸王龙在守护它的家',
                    '魔法神镇--相传 此城中有牢不可破的力量',
                    '高风险地区--谁都不敢去',
                    '柠檬圣地--这个地方高产柠檬',
                    '芒果小岛--这个地方高产芒果']
                    im = Image.new(
                        'RGB', (1365, (len(lb)+2)*71), (255, 255, 255))
                    jp = ImageDraw.Draw(im)
                    fo = ImageFont.truetype(
                        font='C:/Users/Administrator/AppData/Local/Microsoft/Windows/Fonts/也字工厂弗吉亚体.ttf', size=70)
                    jp.text((0, 0), '副本列表:', (68, 204, 255), font=fo)
                    jp.text((0, 70), '==============================',
                            (68, 204, 255), font=fo)
                    for i in range(2, len(lb)+1):
                        jp.text((0, i*70), lb[i-1], (68, 204, 255), font=fo)
                    jp.text((0, i*70+70), '==============================',
                            (68, 204, 255), font=fo)
                    im.save(
                        'C:/Users/Administrator/Desktop/极韵AI总文件/data/images/gx.png')
                    jp.text((0, 0), '进入副本xx*x即可进入副本', (68, 204, 255), font=fo)
                    fs('[CQ:image,file=gx.png]')
                if '穿戴' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    sq = xxi["data"]["messages"][-1]["message"].split('穿戴')[-1]
                    if sq not in dict.keys():
                        fs('神器“'+sq+'”不存在',at=True)
                    else:
                        fdfdfd1 = open('D:/qqbot_image/{}游戏数据.json'.format(qqgid), 'r')
                        fd1234 = fdfdfd1.read()
                        fdfdfd2 = open('D:/qqbot_image/{}游戏数据.json'.format(qqgid),'w')
                        fd1234[str(xxi["data"]["messages"][-1]["sender"]["user_id"])]['force'] += dict[sq]
                if '查看副本' in xxi["data"]["messages"][-1]["message"] and xxi["data"]["messages"][-1]["post_type"] == "message":
                    fb = xxi["data"]["messages"][-1]["message"].split('查看副本')[-1]
    except Exception as ex:
        ex = str(ex)
        if ex == "'NoneType' object is not subscriptable":
            continue
        else:
            print('\033[1;31;31m[{0}] [error] 报错：{1} \033[0m'.format(shijian, ex))
            fs('[CQ:at,qq=1497703235]AI发生了错误，报错信息{}'.format(ex))
            print(报错啦)
