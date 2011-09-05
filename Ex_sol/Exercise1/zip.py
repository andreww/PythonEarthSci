
names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rain = [10.2, 12.4, 9.4, 8.2, 8.9, 7.2, 3.9, 7.6, 8.0, 11.2, 10.5, 9.9]

for month, inch in zip(names, rain):
    print "In " + month + " there was " + str(inch) + " inches of rain"

