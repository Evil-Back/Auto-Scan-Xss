# Auto-Scan-Xss
Automatic xss vulnerability checking tool

install tools linux
git clone https://github.com/AesTeams/Auto-Scan-Xss.git
cd Auto-Scan-Xss
zip xss.zip *
cd xss 
python3 Auto-Scan-Xss.py -h 


It collects all the barometers on the website and checks them for xss vulnerabilities 
It also injects xsshunter payload at the top of the page

 scan one  target
 python3 -u target.com -HX autoscanxss.xss.ht
 
 set proxy list 
 python3 -u target.com -HX autoscanxss.xss.ht -pl proxy.txt
 
 scan list target
 
  python3 -fd target.txt -HX autoscanxss.xss.ht
  
