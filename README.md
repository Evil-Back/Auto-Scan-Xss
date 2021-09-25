# Auto-Scan-Xss
<image src="https://i.ibb.co/gjwfHM9/Screenshot-from-2021-01-18-07-21-09.png">
Automatic xss vulnerability checking tool

install tools linux

git clone https://github.com/AesTeams/Auto-Scan-Xss.git && cd Auto-Scan-Xss && cd  xss && python3 Auto-Scan-Xss.py -h 
<br>

It collects all the barometers on the website and checks them for xss vulnerabilities 
It also injects xsshunter payload at the top of the page

 scan one  target
 
 python3 -u target.com -HX autoscanxss.xss.ht
 
 set proxy list 
 
 python3 -u target.com -HX autoscanxss.xss.ht -pl proxy.txt
 
 scan list target
 
  python3 -fd target.txt -HX autoscanxss.xss.ht
  
https://youtu.be/I46Z_EF5SC4
