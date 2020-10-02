import json
def IPL(date):
	f = open('ipl.json')
	response = json.load(f)
	list1 = []
	#list2 = []
	for match in response:
		if match['Date'] == date:
			list1.append((match['Matches'],match['Time']))
			#list2.append(match['Time'])
	message = "the requested scheule \n"
	#message1 = "the time is"
	for text in list1:
		message += text[0]+ "time: "+text[1] +"\n"
	#for text in list2:
		#message1 += message + text
	return message


