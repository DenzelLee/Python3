*** Setting ***
Library         SeleniumLibrary
Resource        courseRecourse.robot

*** Test Cases ***
add_new_cousrse
    [Setup]      Setupk
    ${num}    Evaluate    random.randint(1,100)    random
    logink
    ${cname}=    addcoursek        python${num}    pydesc    ${num}
    assertk_pass      ${cname}
    deleteallcourse2
    [Teardown]   Teardownk
add_same_cousrse
    [Setup]      Setupk
    logink
    ${cname}=    addcoursek        python1      pydesc    10
    assertk_pass      ${cname}
    ${cname1}=    addcoursek       python1     pydesc    10
    click element                  css=*[class="btn btn-default"]
    assertk_fail      ${cname1}
    deleteallcourse2
    [Teardown]   Teardownk