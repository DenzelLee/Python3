*** Setting ***
Library         SeleniumLibrary
Library         libPython.pythonApi.Webadmin

*** Test Cases ***
添加课程1
    #robot --pythonpath . --suite  20190918_添加培训班期 testCase
    [Setup]         deleteallcourseWeb
    RUN KEYWORDS    addcourseWeb          初中语文    语文描述    100
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
    RUN KEYWORDS    addclassWeb           初中班    综合描述1    100    初中语文
    ...  AND        listclassWeb
    ${class}=      listclassWeb
    log to console  \n${class}\n
#                    deleteallclassWeb
#    [Teardown]      selectcourseTab

添加培训班期1
    [Setup]         selectclassqiTab
                    deleteallclassqiWeb
    RUN KEYWORDS    addclassqiWeb          初中班1期    综合描述1  100   初中班
    ...  AND        listclassqiWeb
    ${class}=      listclassqiWeb
    log to console  \n${class}\n
                    deleteallclassqiWeb
    [Teardown]      selectcourseTab
