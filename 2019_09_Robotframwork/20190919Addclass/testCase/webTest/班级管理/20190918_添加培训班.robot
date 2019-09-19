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

添加培训班1
    [Setup]         selectclassTab
                    deleteallclassWeb
    RUN KEYWORDS    addclassWeb          综合老师1    综合描述1    1    初中语文    初中数学
    ...  AND        listclassWeb
    ${class}=      listclassWeb
    log to console  \n${class}\n
                    deleteallclassWeb
    [Teardown]      selectcourseTab
