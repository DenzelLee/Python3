import requests,time
from pprint import  pprint

# 测试环境Host（ip等铭感信息建议放在单独的py文件中）
testHost = "127.0.0.1:8066"
# 获取当前时间戳
nowTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


def login(username, password):
    # 尽可能少用globa全局变量
    # global cookies
    print("\n----登录账户----\n")
    url = f"http://{testHost}/api/mgr/loginReq"
    payload = {"username": username, "password": password}
    response = requests.post(url, data=payload)
    loginres = dict(response.json())
    global cookies
    cookies = dict(response.cookies)
    # sessionid = response.cookies['sessionid']
    # print(f"登录成功：{loginres}...{cookies}")
    if loginres["retcode"] == 0:
        print(f"登录成功：{loginres}，获取cookeis：{cookies}")
    else:
        print(f"登录失败，账号或密码错误!错误信息：{cookies}")
    return loginres

# 列出课程
def list_course(pagenum=1, pagesize=20):
    # get请求(参数用params，不用data）
    print("\n----列出课程----\n")
    url = f"http://{testHost}/api/mgr/sq_mgr/"
    payload = {'action': 'list_course', 'pagenum': pagenum, 'pagesize': pagesize}
    # params可以避免参数中包含&等特殊字符
    listHttp = requests.get(url=url, params=payload, cookies=cookies)
    listret = listHttp.json()
    # print(type(getret))
    print(str(listret) + "，列出课程信息！")
    # return [i["name"] for i in listret["retlist"]]
    return listret
def add_course(name,desc,cdis):
    print("\n----添加课程----\n")
    url = f"http://{testHost}/api/mgr/sq_mgr/"
    payload = {'action': 'add_course', 'data': f'{{"name":"{name}","desc":"{desc}","display_idx":"{cdis}"}}'}
    response = requests.post(url=url, data=payload, cookies=cookies)
    addres = response.json()
    print(str(addres)+"，添加成功！")
    return addres

def delete_course(cid):
    print("\n---- 删除课程 ----\n")
    url = f"http://{testHost}/api/mgr/sq_mgr/"
    payload = {'action':'delete_course', 'id':cid}
    response = requests.delete(url=url, data=payload, cookies=cookies)
    deleteallret = response.json()
    print(str(deleteallret)+"，删除课程成功！")

def deleteall_course():
    print("\n---- 批量删除课程 ----\n")
    clist = list_course(1, 20)
    print("当前课程数量：", clist['total'])
    for i in [id['id'] for id in clist['retlist'][1:]]:
        delete_course(i)
    clist = list_course(1, 20)
    print("\n当前课程数量：", clist['total'])

if __name__=='__main__':
    login('auto', 'sdfsdfsdf')
    deleteall_course()