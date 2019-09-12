*** Setting ***
Library  SeleniumLibrary
Library  Dialogs
Library  Collections

*** Test Cases ***
Number_game
    # This is Number_game
    [Documentation]          ---- Guess number Game！----\n
    [Setup]                  log to console       ----\nWlcome to my Game!----\n
    :for   ${i}              IN RANGE  100
      \    ${num}=           evaluate  random.randint(60,99)  random
      \    ${input}=         get value from user    请输入您的数字      ${num}
      \    run keyword if    int($input)==100        log to console   恭喜你，答对了！
      ...    ELSE IF           int($input)>90        log to console    90分段数字错误，大于目标数
      ...    ELSE IF           int($input)>80       log to console     80分段数字错误，大于目标数
      ...    ELSE IF           int($input)>70       log to console     70分段数字错误，大于目标数
      ...    ELSE IF           str($input)=='q'  exit for loop
      ...    ELSE IF           str($input)=='c'     continue  for loop
      ...    ELSE              log to console                          你无法答对该问题，建议退出...


