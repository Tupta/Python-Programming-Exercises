# x = '1300'

# if int(x) >= 1201:
#     dp = 'pm'
# else:
#     dp = 'am'

# hh = x[:2]
# mm = x[2:4]
# if int(hh) >= 13:
#     hh1 = int(hh)-12
# else:
#     hh1 = hh
# #print(hh1, mm)
# #print(x[:2]+':'+x[2:4]+dp)
# time = (f'{hh1}:{mm} {dp}')
# return time

################################
# def to12hourtime(timestring):

#     x = timestring
#     if int(x) >= 1201:
#         dp = 'pm'
#     else:
#         dp = 'am'

#     hh = x[:2]
#     mm = x[2:4]
#     if int(hh) >= 13:
#         hh1 = int(hh)-12
#     else:
#         hh1 = int(hh)
#     #print(hh1, mm)
#     #print(x[:2]+':'+x[2:4]+dp)
#     time = (f'{hh1}:{mm} {dp}')

#     return time
#     pass
#     # return 'h:mm am' or 'h:mm pm
    
# print(to12hourtime('0059'))

# import json

# stringOfJsonData = '{"name": "Zophie", "isCat": true,"miceCaught": 0,"felineIQ": null}'

# jsonDataAsPythonValue = json.loads(stringOfJsonData)

# print(jsonDataAsPythonValue)

import time

d = time.time()

print(d)