@echo off
setlocal enabledelayedexpansion

REM
set VALIDATOR=bcsp_validate.exe

REM Loop for each method
for %%M in (depth, hill) do (
  REM Loop for each test
  for /l %%i in (1, 1, 8) do (
        set /a "result=%%i * 16"
    for /l %%t in (1, 1, 10) do (

        REM
        call %VALIDATOR% "test%%i_M!result!_N16_K6_%%t.txt" "solution_%%M_test%%i_M!result!_N16_K6_%%t.txt"

        REM Optionally, you can print the return code of the program
        echo Test %%M_%%i: Return Code - !ERRORLEVEL!
    ) 
  )
)
endlocal