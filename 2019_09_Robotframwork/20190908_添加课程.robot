*** Setting ***
Library  SeleniumLibrary
Library  Collections
Library  robotapiTest.py
Suite Setup    login    auto    sdfsdfsdf
Test Setup     deleteall_course
Suite Teardown  log to console  \n----1.end add_course Suite!\n
Test Teardown  log to console  \n----2.end add_course DefaultTest!\n
*** Test Cases ***
add_course
    [Setup]     log to console  \n----strt add_course testCase!
    [Setup]     deleteall_course
    ${oldlistc}=    list course    1    20
    log to console    &{oldlistc}[total]
    run keyword if    &{oldlistc}[total]==0    log to console  \n----clear
    ...  ELSE IF      &{oldlistc}[total]>0     log to console  \n----dirty
    log to console    \n${oldlistc}
    ${addc}=    add_course    pname    pdesc    10
    log to console  \n${addc}
    ${newlistc}=    list course    1    20
    log to console    \n${newlistc}
    :FOR    ${course}    in    &{newlistc}[retlist]
#      \    run keyword if     ${course}   not in  &{oldlistc}[retlist]
       \    log to console     @{course}[1]
       \    ${values}   get dictionary values     @{course}[1]
       \    log to console     ${values}
       \    ${name}=    create list    ${values}[3]
       \   ${expected}=   create list    pname
        \   lists should be equal    ${expected}   ${name}

    [Teardown]    log to console  \n----3.end add_course testCase!\n