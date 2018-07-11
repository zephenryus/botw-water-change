@ECHO OFF
for %%i in (%*) do (
    python "%~dp0change_water.py" "%%~i"
)
