*** Test Cases ***
Case1
  ${a}  Set Variable  100
  ${integer}  Convert To Integer  ${a}
  log to console  ${integer}
  ${number}  Convert To Number  ${a}
  log to console  ${number}
  ${binary}  Convert To Binary  ${a}
  log to console  ${binary}
  ${octal}  Convert To Octal  ${a}
  log to console  ${octal}
  ${hex}  Convert To Hex  ${a}
  log to console  ${hex}
  ${string}  Convert To String  ${a}
  log to console  ${string}
  ${bytes}  Convert To Bytes  ${a}
  log to console  ${bytes}
  ${boolean}  Convert To Boolean  ${a}
  log to console  ${boolean}
Case2
  ${a}  Set Variable  100
  ${integer}  Convert To Integer  ${a}  2
  log to console  ${integer}
  ${binary}  Convert To Binary  ${a}  8
  log to console  ${binary}
  ${octal}  Convert To Octal  ${a}  16
  log to console  ${octal}
  ${hex}  Convert To Hex  ${a}  10
  log to console  ${hex}
  ${string}  Convert To String  ${a}
  log to console  ${string}
  ${bytes}  Convert To Bytes  ${a}
  log to console  ${bytes}
  ${boolean}  Convert To Boolean  ${a}
