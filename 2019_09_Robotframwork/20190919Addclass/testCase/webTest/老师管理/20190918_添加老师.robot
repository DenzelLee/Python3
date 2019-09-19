*** Setting ***
Library         SeleniumLibrary
Library         libPython.pythonApi.Webadmin

*** Test Cases ***
添加课程1
    [Setup]         deleteallcourseWeb
    RUN KEYWORDS    addcourseWeb          初中语文    语文描述    1
    ...  AND        listcourseWeb
    ${course}=      listcourseWeb
    log to console  \n${course}\n
#    [Teardown]      deleteallcourseWeb

添加课程2
#    [Setup]         deleteallcourseWeb
    RUN KEYWORDS    addcourseWeb          初中数学    数学描述
    ...  AND        listcourseWeb
    ${course}=      listcourseWeb
    log to console  \n${course}\n
#    [Teardown]      deleteallcourseWeb
添加老师1
    [Setup]         selectteacherTab
                    deleteallteacherWeb
    RUN KEYWORDS    addteacherWeb          语文老师1    语文账户1    语文描述1    初中语文    1
    ...  AND        listteacherWeb
    ${teacher}=      listteacherWeb
    log to console  \n${teacher}\n
#    [Teardown]      deleteallcourseWeb

添加老师2
#    [Setup]         deleteallcourseWeb
#                    selectteacherTab
    RUN KEYWORDS    addteacherWeb          数学老师1    数学账户1    数学描述1    初中数学    1
    ...  AND        listteacherWeb
    ${teacher}=      listteacherWeb
    log to console  \n${teacher}\n
                    deleteallteacherWeb
    [Teardown]      selectcourseTab
