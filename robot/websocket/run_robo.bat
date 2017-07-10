# > nul 2>&1 || cd "%~dp0" && python "%~0" && goto :eof
import robot

robot.start('ws://47.92.105.64:12306/')