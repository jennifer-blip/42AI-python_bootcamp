import datetime

kata = (2019, 9, 25, 3, 30)

# print ("{number:02}".format(number = kata[1]),"/{number:02}".format(number = kata[2]),"/{number:04}".format(number = kata[0]), " {number:02}".format(number = kata[3]), ":{number:02}".format(number = kata[4]), sep='')
print(f"{kata[1]:02}/{kata[2]:02}/{kata[0]:04} {kata[3]:02}:{kata[4]:02}")
print (datetime.datetime(*kata).strftime("%m/%d/%Y %H:%M"))