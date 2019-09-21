*** Setting ***
Library         SeleniumLibrary
Library         Apipython.webpython.Webadmin
Library         Apipython.interfacepython.Interadmin

*** Test Cases ***
UI_添加老师2019092001
    [Setup]         startWeb
    run keywords    loginWeb
    ...  AND        deleteallcourseWeb
    ...  AND        addcourseWeb          初中语文    语文描述    1
    ...  AND        addcourseWeb          初中数学    数学描述    2
    ...  AND        selectteacherTab
    ...  AND        addteacherWeb         语文老师1   语文账户1   语文描述1    初中语文    1
    ${teacher}=     listteacherWeb
    log to console  \n${teacher}\n
                    deleteallteacherWeb
    [Teardown]      endWeb
API_添加老师2019092002
    [Setup]         interlogin
    run keywords    interdeleteallcourse
    ...  AND        interaddcourse        初中语文    语文描述    100
    ${lesson}=      intergetcourse
    log to console  ${lesson}
    interaddteacher       语文老师    语文账户    语文描述    100    @{lesson}[0]    @{lesson}[1]
    ${teacher}=     interlistteacher
    log to console  \n${teacher}\n
    [Teardown]      interdeleteallteacher


'''--结果：
API_添加老师2019092002                                                | PASS |
------------------------------------------------------------------------------
Tc.20190920 添加老师                                                  | PASS |
2 critical tests, 2 passed, 0 failed
2 tests total, 2 passed, 0 failed
==============================================================================
Tc                                                                    | PASS |
2 critical tests, 2 passed, 0 failed
2 tests total, 2 passed, 0 failed
==============================================================================
Output:  D:\MyTest\Python3\Tmp\Python3\20190920_接口测试\20190920_addTeacher\output.xml
Log:     D:\MyTest\Python3\Tmp\Python3\20190920_接口测试\20190920_addTeacher\log.html
Report:  D:\MyTest\Python3\Tmp\Python3\20190920_接口测试\20190920_addTeacher\report.html

'''