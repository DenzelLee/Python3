*** Setting ***
Library            SeleniumLibrary
Resource           courseRC.robot
Test Setup         Setupk
Suite Teardown     Teardownk

*** Test Cases ***
添加课程1
    addcoursek        python1        pydesc        2
    listcoursek
    assertk_pass      python1

添加课程2
    addcoursek        python2        pydesc        3
    listcoursek
    assertk_pass      python2
