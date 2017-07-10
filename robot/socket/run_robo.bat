# > nul 2>&1 || cd "%~dp0" && python "%~0" && goto :eof
import robot

robot.start('192.168.2.51',10010)