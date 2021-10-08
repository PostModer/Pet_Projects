import datetime
today = datetime.datetime.today() 
hour_minut = str(today.strftime('%H')) + ":" + str(today.strftime('%M'))
print(hour_minut)