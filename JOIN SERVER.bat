@echo off

set /P ttUsername="Username (DEFAULT: username): " || ^
set ttUsername=username
set ttPassword=password
set TT_PLAYCOOKIE=%ttUsername%
set TT_GAMESERVER=188.165.250.225
rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

echo ===============================
echo Starting Project Altis...
echo ppython: %PPYTHON_PATH%
echo Username: %ttUsername%
echo Client Agent IP: %TT_GAMESERVER%
echo ===============================

%PPYTHON_PATH% -m toontown.toonbase.ToontownStart
pause
