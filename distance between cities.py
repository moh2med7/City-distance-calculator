from pystyle import *
from geopy.distance import geodesic

print(Box.Lines("[+] Learn python [+]"))
Write.Print("[-] this program for distance between cities \n" , Colors.purple_to_red , interval=0.1)
print(Box.DoubleCube("Example 6"))

f_p = (36.7525 , 3.0420)
s_p = (35.6987 , -0.6349)    
dis = int(geodesic(f_p,s_p).km)
Write.Print(f'[+] Distence between cities is: {dis} kilometers \n', Colors.light_blue , interval=0.1 )
input('\n press any key to exit ...')