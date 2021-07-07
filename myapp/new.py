# import requests
# import urllib.parse

# address = 'Shivaji Nagar, Bangalore, KA 560001'
# url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

# response = requests.get(url).json()
# # print(response[0]["lat"])
# # print(response[0]["lon"])
# print(response)

# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="my_user_agent")
# # city ="London"
# # country ="Uk"
# address="Bangalore, KA 560001"
# #loc = geolocator.geocode(city+','+ country)
# loc = geolocator.geocode(address)
# print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)

import xlwt
from xlwt import Workbook
  
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
  
sheet1.write(1, 0, 'ISBT DEHRADUN')
sheet1.write(2, 0, 'SHASTRADHARA')
sheet1.write(3, 0, 'CLEMEN TOWN')
sheet1.write(4, 0, 'RAJPUR ROAD')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(0, 1, 'ISBT DEHRADUN')
sheet1.write(0, 2, 'SHASTRADHARA')
sheet1.write(0, 3, 'CLEMEN TOWN')
sheet1.write(0, 4, 'RAJPUR ROAD')
sheet1.write(0, 5, 'CLOCK TOWER')
  
wb.save('xlwt example.xls')