import nmap  
nm = nmap.PortScanner()
print "[*] start scanning"

nm.scan('127.0.0.1', '20-443')
print nm.command_line()  
print nm.scaninfo()
print "[*] end scanning"