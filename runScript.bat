:ping
ping 1.2.3.4 -n 1 -w 1000 > nul
set target=www.google.com
ping %target% -n 1 | find "TTL="
if errorlevel==1 goto ping

rundll32 url.dll,FileProtocolHandler https://web.whatsapp.com/

git reset --hard
git pull https://github.com/coencuppen/Chore-Mate-Messenger
cd %HOMEPATH%\Documents\GitHub\Chore-Mate-Messenger

pip install -r requirements.txt

python main.py
