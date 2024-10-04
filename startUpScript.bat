:ping
ping 1.2.3.4 -n 1 -w 1000 > nul
set target=www.google.com
ping %target% -n 1 | find "TTL="
if errorlevel==1 goto ping
git pull https://github.com/coencuppen/Chore-Mate-Messenger
cd C:\Users\coenc\Documents\GitHub\Chore-Mate-Messenger
python main.py