*** Setting ***
Library  SeleniumLibrary
Library  courseAPI.py

*** Variables ***
${basicurl}    http://localhost:8066/
@{info}        auto    sdfsdfsdf

*** Keywords ***
Setupk
    open browser    ${basicurl}    chrome
    set selenium implicit wait  10

Teardownk
    close browser

logink
    log to console       \n----开始登录----\n
    go to           ${basicurl}mgr/login/login.html
    input text      id=username            @{info}[0]
    input text      id=password            @{info}[1]
    click element      css=[type="button"]
    sleep           0.5
    log many     ${basicurl}    @{info}[0]    @{info}[1]

addcoursek
    log to console       \n----开始添加数据----\n
    [Arguments]    ${name}    ${desc}    ${num}
    click element  css=*[ng-click^=showAddOne]
    input text     css=*[ng-model="addData.name"]            ${name}
    input text     css=*[ng-model="addData.desc"]            ${desc}
    input text     css=*[ng-model="addData.display_idx"]     ${num}
    click element  css=*[ng-click="addOne()"]
    sleep          1
    [Return]       ${name}

assertk_pass
    [Arguments]    ${name}
                   log to console       \n----开始验证相等----\n
    ${eles}        get webelements      css=tbody>tr>td:nth-child(2)
    :for           ${ele}               IN                   @{eles}
      \            log to console       current:${ele.text}
      \            log to console       getvalus:${name}
      \            run keyword if       $ele.text==$name          log to console       u"--验证成功--"\n
      ...          ELSE                 log to console            u"--验证失败--"\n
      \            ${len}=              lenth                     ${eles}
      \            log to console       u"当前数量: "${len}

assertk_fail
    [Arguments]    ${name}
                   log to console       \n----开始验证不相等----\n
    ${eles}        get webelements      css=tbody>tr>td:nth-child(2)
    :for           ${ele}               IN                   @{eles}
      \            run keyword if       $ele.text!=$name          log to console       u"--验证成功--"\n
      ...          ELSE                 log to console            u"--验证失败--"\n
      \            log to console       current:${ele.text}
      \            log to console       getvalus:${name}
      \            ${len}=              lenth                     ${eles}
      \            log to console       u"当前数量: "${len}



DeleteAllCourse1
    log to console       \n----开始删除所有数据----\n
    Set Selenium Implicit Wait   2
    :For   ${one}  IN RANGE  99
       \   sleep  1
       \   ${html}=  Get Webelement  tag=html
       \   ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")
       \   Exit For Loop If   $eles==[]
       \   Click Element   @{eles}[1]
       \   Click Element   css=button.btn-primary
    Set Selenium Implicit Wait   10             1

deleteallcourse2
    log to console       \n----开始删除所有数据----\n
    set selenium implicit wait  2
    :for           ${ele}               IN RANGE    100
      \            ${eles}              get webelements       css=*[ng-click="delOne(one)"]
      \            ${len}=              lenth    ${eles}
#      \            log to console       ${len}
      \            exit for loop if     $len==1
      \            click element        @{eles}[1]
      \            click element        css=*[class="btn btn-primary"]
      \            sleep                3
      set selenium implicit wait  10




















