*** Setting ***
Library  SeleniumLibrary
Library  apiTest.py
Library    Collections

*** Test Cases ***
cource_test1
    log to console    \n\n----1.login_user----\n
    ${clogin}=   login   auto  sdfsdfsdf
    log to console  ${clogin}
    should be equal as integers   &{clogin}[retcode]    0

    log to console    \n----2.list_course----\n
    ${clist}=    list_course
    log to console    ${clist}

    log to console    \n----3.print_course----\n
    :FOR    ${course}    in     @{clist}
    \    log to console   ${course}
    \    log to console  \n

    ${expected}=    create list  测试修改课程11111    测试课程2019-08-24 13:06:14    测试课程2019-08-24 13:06:47    测试课程2019-08-24 13:06:50    测试课程2019-08-24 13:06:53
    Lists Should Be Equal     ${clist}     ${expected}

url_test2
    Open Browser                  https://www.vmall.com/index.html    chrome
    Set Selenium Implicit Wait    10
    ${texts}=    Get Webelements   css=.span-968.fl .grid-list.clearfix li
    :FOR    ${text}    in    @{texts}
    \     log to console  ${text.text}
    Close Browser