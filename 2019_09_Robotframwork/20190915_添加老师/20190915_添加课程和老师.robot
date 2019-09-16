*** Setting ***
Library          SeleniumLibrary
Resource         ../20190915_添加老师/课程目录/courseRC.robot
Resource         ../20190915_添加老师/老师目录/teacherRC.robot
#Suite Setup         Setupt
#Suite Teardown      Teardownt

*** Test Cases ***
添加课程1
    [Setup]           Setupk
    addcoursek        python1        pydesc        2
    listcoursek
    assertk_pass      python1
    [Teardown]        Teardownk
添加课程2
    [Setup]           Setupk
    addcoursek        python2        pydesc        3
    listcoursek
    assertk_pass      python2
    [Teardown]        Teardownk
添加老师1
    [Setup]           Setupt
    addcourset        tName1        tloginname1     tdesc        1        报错课程_20190908
    listcourset
    assertt_pass      tloginname1
    [Teardown]        Teardownt
添加老师2
    [Setup]           Setupt
    addcourset        tName1        tloginname2     tdesc        1        报错课程_20190908
    listcourset
    assertt_pass      tloginname2
    [Teardown]        Teardownt