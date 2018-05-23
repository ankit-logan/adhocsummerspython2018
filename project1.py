#!/usr/bin/python2
import time
import webbrowser

print "#################################################"

print "MENU LIST"
option='''
Press 1 : enter anything - split each word and search on google
Press 2 : enter anything - split them and find there url
Press 3 : enter anything - split them and find image search
Press 4 : find current time and date 
Press 5 : open default browser
Press 6 : all network ip 
Press 7 : enter domain name and find owner , email , contact
'''
print option

ch=raw_input("Enter The Choice:")
if ch=='1' :
	search_data=raw_input("Enter data:")
	final_data=search_data.strip()
	#above removing leading and trailing space
	done_data=final_data.split()
	#splitting each word by space
	for i in done_data:
		webbrowser.open_new_tab('http://www.google.com/search?q='+i)
elif ch=='2' :
	print ""

elif ch=='3' :
	search_data=raw_input("Enter data:")
	final_data=search_data.strip()
	#above remob=ving leading and trailing space
	done_data=final_data.split()
	#splitting each word by space
	for i in done_data:
		webbrowser.open_new_tab('http://www.google.com/search?q='+i+'&source=lnms&tbm=isch')

elif ch=='4' :
	print time.ctime()

elif ch=='5' :
	webbrowser.open('http://www.google.com')

elif ch=='6' :
	print ""

elif ch=='7' :
	print ""

else:
	print "no choice" 




