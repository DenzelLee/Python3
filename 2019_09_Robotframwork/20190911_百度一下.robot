*** Setting ***
Library  SeleniumLibrary

*** Test Cases ***
百度一下
    # This is testCase
    open browser    http://www.baidu.com    chrome
    set selenium implicit wait  10
    input text      id=kw    selenium
    click element   id=su
    ${eles}=       get webelements  css=#container #content_left div h3>a
    :FOR    ${ele}     IN              @{eles}
       \               log to console  ${ele}
       \               log to console  ${ele.text}
       \               run keyword if  '${ele.text}'=='selenium_百度翻译'     log to console   yes!
       \               should be equal  '${ele.text}'  'selenium_百度翻译1'    notequeal报错提示：