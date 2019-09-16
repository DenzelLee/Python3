*** Setting ***
Library          SeleniumLibrary
Library          courseAPI.py

*** Variables ***
${basicurl}    http://localhost:8066/
@{info}        auto    sdfsdfsdf

*** Keywords ***
Setupk
    log to console  \nu"----开始初始化----"\n
    open browser    ${basicurl}    chrome
    DeleteAllCoursec2
    set selenium implicit wait  10
    log to console  \nu"----结束初始化----"\n

Teardownk
    log to console  \nu"----开始清理数据----"\n
    DeleteAllCoursec2
    close browser
    log to console  \nu"----结束清理数据----"\n


logink
    log to console       \n----开始登录----\n
    go to           ${basicurl}mgr/login/login.html
    input text      id=username            @{info}[0]
    input text      id=password            @{info}[1]
    click element      css=[type="button"]
    sleep           0.5
    log many     ${basicurl}    @{info}[0]    @{info}[1]
    log to console       \n----结束登录----\n
listcoursek
    log to console       \n----开始列出数据----\n
    ${eles}        get webelements      css=tbody>tr>td:nth-child(2)
    :for           ${ele}               IN                   @{eles}
      \            log to console       current:${ele.text}

addcoursek
    log to console       \n----开始添加数据----\n
    [Arguments]    ${name}    ${desc}    ${num}
    click element  css=*[ng-click^=showAddOne]
    input text     css=*[ng-model="addData.name"]            ${name}
    input text     css=*[ng-model="addData.desc"]            ${desc}
    input text     css=*[ng-model="addData.display_idx"]     ${num}
    click element  css=*[ng-click="addOne()"]
    sleep          1
    log to console       \n----结束添加数据----\n
    [Return]       ${name}

assertk_pass
    [Arguments]    ${name}
                   log to console       \n----开始验证_相等----\n
    ${eles}        get webelements      css=tbody>tr>td:nth-child(2)
    :for           ${ele}               IN                   @{eles}
      \            log to console       current:${ele.text}
      \            log to console       getvalus:${name}
      \            run keyword if       $ele.text==$name          log to console       u"--验证成功--"\n
      ...          ELSE                 log to console            u"--验证失败--"\n
      \            ${len}=              clenth                     ${eles}
      \            log to console       --u"当前数量: "${len}\n
                   log to console       \n----结束验证_相等----\n

assertk_fail
    [Arguments]    ${name}
                   log to console       \n----开始验证_不相等----\n
    ${eles}        get webelements      css=tbody>tr>td:nth-child(2)
    :for           ${ele}               IN                   @{eles}
      \            run keyword if       $ele.text!=$name          log to console       u"--验证成功--"\n
      ...          ELSE                 log to console            u"--验证失败--"\n
      \            log to console       current:${ele.text}
      \            log to console       getvalus:${name}
      \            ${len}=              clenth                     ${eles}
      \            log to console       --u"当前数量: "${len}\n
                   log to console       \n----结束验证_不相等----\n


DeleteAllCoursec1
    log to console       \n----开始删除所有数据----\n
    logink
    Set Selenium Implicit Wait   3
    :For   ${one}  IN RANGE  99
       \   sleep  1
       \   ${html}=  Get Webelement  tag=html
       \   ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")
       \   Exit For Loop If   $eles==[]
       \   Click Element   @{eles}[1]
       \   Click Element   css=button.btn-primary
       log to console       \n----结束删除所有数据----\n
       sleep        1.5
    Set Selenium Implicit Wait   10             1

deleteallcoursec2
    log to console       \n----开始删除所有数据----\n
    logink
    set selenium implicit wait  3
    :for           ${ele}               IN RANGE    100
      \            ${eles}              get webelements       css=*[ng-click="delOne(one)"]
      \            ${len}=              clenth    ${eles}
#      \            log to console       ${len}
      \            exit for loop if     $len==1
      \            click element        @{eles}[1]
      \            click element        css=*[class="btn btn-primary"]
      \            sleep                3
      log to console       \n----结束删除所有数据----\n
      sleep        1.5
      set selenium implicit wait  10




















