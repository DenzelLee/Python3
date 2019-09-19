*** Setting ***
Library  SeleniumLibrary
Library  Collections
Library  robotapiTest.py
Suite Setup    login    auto    sdfsdfsdf
Test Setup     deleteall_course
Suite Teardown  log to console  \n----1.end add_course DefaulSuite!\n
Test Teardown  log to console  \n----2.end add_course DefaultTest!\n
*** Test Cases ***
add_course001
#    [Setup]       LOG TO CONSOLE    \n--3.start  testcase
    open browser  http://localhost:8066/mgr/login/login.html    chrome
    set selenium implicit wait  10
    input text    id=username    auto
    input text    id=password    sdfsdfsdf
    click element  css=*[type=button]

    sleep          2
    click element  css=*[class="btn btn-blue btn-outlined btn-md"]
    input text     css=*[ng-model="addData.name"]  python01
    input text     css=*[ng-model="addData.desc"]                      python02
    input text     css=*[ng-model="addData.display_idx"]               10
    click element  css=*[ng-click="addOne()"]
#    click element  css=*[ng-click="logout()"]
    sleep          2


    ${lessons}     create list
    ${eles}=       Get Webelements    css=*[ng-if="theList.length>0"] tr>td:nth-child(2)
    :FOR           ${ele}     IN      @{eles}
       \            log to console     ${ele.text}
       \            run keyword if     '${ele.text}'==u'报错课程_20190908'    CONTINUE FOR LOOP
       \            append to list     ${lessons}    ${ele.text}
       \            should be true     ${lessons}==['python01']
    [Teardown]     deleteall_course





#add_course002
#    [Setup]     log to console  \n----strt add_course testCase!
#    [Setup]     deleteall_course
#    ${oldlistc}=    list course    1    20
#    log to console    &{oldlistc}[total]
#    run keyword if    &{oldlistc}[total]==0    log to console  \n----clear
#    ...  ELSE IF      &{oldlistc}[total]>0     log to console  \n----dirty
#    log to console    \n${oldlistc}
#    ${addc}=    add_course    pname    pdesc    10
#    log to console  \n${addc}
#    ${newlistc}=    list course    1    20
#    log to console    \n${newlistc}
#    :FOR    ${course}    in    &{newlistc}[retlist]

##      \    run keyword if     ${course}   not in  &{oldlistc}[retlist]
#       \    log to console     @{course}[1]
#       \    ${values}   get dictionary values     @{course}[1]
#       \    log to console     ${values}
#       \    ${name}=    create list    ${values}[3]
#       \   ${expected}=   create list    pname
#        \   lists should be equal    ${expected}   ${name}
#    [Teardown]    log to console  \n----3.end add_course testCase!\n