*** Setting ***
Library            SeleniumLibrary
Resource           teacherRC.robot
Suite Setup         Setupt
Suite Teardown      Teardownt

*** Test Cases ***
添加老师1
    addcourset        tName1        tloginname1     tdesc        1        报错课程_20190908
    listcourset
    assertt_pass      tloginname1
添加老师2
    addcourset        tName1        tloginname2     tdesc        1        报错课程_20190908
    listcourset
    assertt_pass      tloginname2
