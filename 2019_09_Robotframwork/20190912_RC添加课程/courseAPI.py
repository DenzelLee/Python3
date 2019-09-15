from selenium import webdriver
from pprint import pprint
from time import sleep
import datetime, time,requests
from random import randint

# 测试环境Host（ip等铭感信息建议放在单独的py文件中）
testHost = "127.0.0.1:8066"
# 获取当前时间戳
nowTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# ------------------UIapi

def lenth(alist):
    return len(list(alist))

def uilogin(username="auto", password="sdfsdfsdf"):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = r"http://localhost:8066/mgr/login/login.html"
    driver.get(url)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_css_selector('*[type="button"]').click()

def uiadd_course(cname, cdesc, cnum):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('*[ng-click="showAddOne=true"]').click()
    driver.find_element_by_css_selector('*[ng-model="addData.name"]').send_keys(f"{cname}{nowTime}")
    driver.find_element_by_css_selector('*[ng-model="addData.desc"]').send_keys(f"{cdesc}{nowTime}")
    driver.find_element_by_css_selector('*[ng-model="addData.display_idx"]').clear()
    driver.find_element_by_css_selector('*[ng-model="addData.display_idx"]').send_keys(cnum)
    driver.find_element_by_css_selector('*[ng-click="addOne()"]').click()
    driver.find_element_by_css_selector('[ng-click="$parent.showAddOne=false"]').click()
    print(f"\n----添加成功，课程名称：{cname}{nowTime}")
    return f"{cname}{nowTime}"


def uilist_course():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    count = 0
    eles = driver.find_elements_by_css_selector('*[ng-repeat="one in theList| itemsPerPage: pageSize"]')
    for course in eles:
        count += 1
        print(f"\n{count}.课程信息：{course.text}\n")


def uidelete_course(getname):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    eles = driver.find_elements_by_css_selector('*[ng-repeat="one in theList| itemsPerPage: pageSize"]')
    for course in eles:
        cid = course.find_element_by_css_selector("td:nth-child(1)").text
        cname = course.find_element_by_css_selector("td:nth-child(2)").text
        if str(cname) == str(getname):
            course.find_element_by_css_selector('button[ng-click="delOne(one)"]').click()
            sleep(1)
            driver.find_element_by_css_selector('*[class="btn btn-primary"]').click()
            sleep(1)
            break
    print(f"\n----课程删除成功,课程名称：{cname}{nowTime}----")

def uideleteall_course():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    count = 0
    while True:
        eles = driver.find_elements_by_css_selector('[ng-if="theList.length>0"] tbody>tr [ng-click="delOne(one)"]')
        if len(eles) == 1:
            break
        eles[1].click()
        sleep(1)
        driver.find_element_by_css_selector('*[class="btn btn-primary"]').click()
        count += 1
        print(f"\n----{count}.课程删除成功----")
        sleep(1)

# ----------------接口API
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
    # login('auto', 'sdfsdfsdf')
    # deleteall_course()
    print(lenth([1,2,3]))