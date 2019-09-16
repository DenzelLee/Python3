*** Setting ***
Library          SeleniumLibrary
Library          teacherAPI.py

*** Variables ***
${basicurl}    http://localhost:8066/
@{info}        auto    sdfsdfsdf

*** Keywords ***
Setupt
    log to console  \nu"----开始初始化----"\n
    open browser    ${basicurl}    chrome
    DeleteAllCourset2
    set selenium implicit wait  10
    log to console  \nu"----结束初始化----"\n

Teardownt
    log to console  \nu"----开始清理数据----"\n
    DeleteAllCourset2
    close browser
    log to console  \nu"----结束清理数据----"\n


logint
    log to console       \n----开始登录----\n
    go to           ${basicurl}mgr/login/login.html
    input text      id=username            @{info}[0]
    input text      id=password            @{info}[1]
    click element      css=[type="button"]
    sleep           0.5
    log many     ${basicurl}    @{info}[0]    @{info}[1]
    sleep           0.5
    go to           ${basicurl}mgr/ps/mgr/index.html#/teacher
    log to console       \n----结束登录----\n
    sleep           0.5
gotot
    go to           ${basicurl}mgr/ps/mgr/index.html#/teacher

listcourset
    log to console       \n----开始列出数据----\n
    ${eles}        get webelements      css=tbody>tr td:nth-child(3)
    :for           ${ele}               IN                   @{eles}
      \            log to console       current:${ele.text}

addcourset
    log to console       \n----开始添加数据----\n
    [Arguments]    ${realname}    ${username}    ${desc}    ${num}    ${course}
    click element  css=*[ng-click^=showAddOne]
    input text     css=*[ng-model="addEditData.realname"]            ${realname}
    input text     css=*[ng-model="addEditData.username"]            ${username}
    input text     css=*[ng-model="addEditData.desc"]                ${desc}
    input text     css=*[ng-model="addEditData.display_idx"]         ${num}
    click element  css=*[ng-click="addOne()"]
    select from list by label    css=*[ng-model="$parent.courseSelected"]    ${course}
    click element  css=*[ng-click="addEditData.addTeachCourse()"]
    sleep          1
    log to console       \n----结束添加数据----\n
    [Return]       ${username}

assertt_pass
    [Arguments]    ${username}
                   log to console       \n----开始验证_相等----\n
    ${eles}        get webelements      css=tbody>tr td:nth-child(3)
    :for           ${ele}               IN                   @{eles}
      \            log to console       current:${ele.text}
      \            log to console       getvalus:${username}
      \            run keyword if       $ele.text==$username          log to console       u"--验证成功--"\n
      ...          ELSE                 log to console            u"--验证失败--"\n
      \            ${len}=              tlenth                     ${eles}
      \            log to console       --u"当前数量: "${len}\n
                   log to console       \n----结束验证_相等----\n

assertt_fail
    [Arguments]    ${username}
                   log to console       \n----开始验证_不相等----\n
    ${eles}        get webelements      css=tbody>tr>td:nth-child(2)
    :for           ${ele}               IN                   @{eles}
      \            run keyword if       $ele.text!=$name          log to console       u"--验证成功--"\n
      ...          ELSE                 log to console            u"--验证失败--"\n
      \            log to console       current:${ele.text}
      \            log to console       getvalus:${username}
      \            ${len}=              tlenth                     ${eles}
      \            log to console       --u"当前数量: "${len}\n
                   log to console       \n----结束验证_不相等----\n


DeleteAllCourset1
    log to console       \n----开始删除所有数据----\n
    logint
    Set Selenium Implicit Wait   3
    :For   ${one}  IN RANGE  99
       \   sleep  1
       \   ${html}=  Get Webelement  tag=html
       \   ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click='delOne(one)']")
       \   Exit For Loop If   $eles==[]
       \   Click Element   @{eles}[0]
       \   Click Element   css=button.btn.btn-primary
       log to console       \n----结束删除所有数据----\n
       sleep        1.5
    Set Selenium Implicit Wait   10             1

deleteallcourset2
    log to console       \n----开始删除所有数据----\n
    logint
    set selenium implicit wait  3
    :for           ${ele}               IN RANGE    100
      \            ${eles}              get webelements       css=*[ng-click="delOne(one)"]
      \            ${len}=              tlenth    ${eles}
#      \            log to console       ${len}
      \            exit for loop if     $len==0
      \            click element        @{eles}[0]
      \            click element        css=*[class="btn btn-primary"]
      \            sleep                3
      log to console       \n----结束删除所有数据----\n
      sleep        1.5
      set selenium implicit wait  10




















