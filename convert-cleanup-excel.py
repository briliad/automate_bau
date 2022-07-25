#Breaking down records into dictionary

#1. Load Excel into a Python dictionary
#2. Parse through the Python dictionary, locate duplicate risks
#3. Create a records for each risk with multiple entries in the apps column
import pandas

xls = pandas.read_excel('F:/programming/test.xlsx')
risks = xls.to_dict('records')
# print (risks[0])


# for key, value in risks.iteritems():   # iter on both keys and values
#     print (key, value)
#     if "," in value:
#         print (key, value)

# discarded approach of unique risk and app pairs
# for key in risks:
#     # print(key)
#     print(key['risk id'], key['apps'])
#     if "," in key['apps']:
#         applist = key['apps'].split(",")
#         print(key['risk id'])
#         for x in applist:
#             print(x)
#             riskapp = {'risk id': key['risk id'], 'apps': x}
#     else:
#         riskapp = {'risk id': key['risk id'], 'apps': x}

# for key in riskapp:
#     print(key)

#approach create a nested dictionary, with list of apps
# check if the risk id exists and add the app to the list of apps
risklist = dict()
risklist = {}

for key in risks:
    applist = key['apps'].split(",")
    print (key)

    # risklist[key['risk id']] = {'applist' = applist}  #a list within a dictionary doesnt work
    if bool(risklist):
        if key['risk id'] in risklist.keys():
            applist = key['apps'].split(",")
            for i in applist: 
                if (i in risklist[key['risk id']].get('apps')):
                    print('already in')
                else:
                    risklist[key['risk id']]['apps'] = risklist[key['risk id']]['apps'] + ',' + i.strip()
        else:
            risklist[key['risk id']] = key
    else:
        risklist[key['risk id']] = key

print(risklist)
# result = [(key, value) for key, value in my_dict.iteritems() if key.startswith("seller_account")]

#data structure
# risk id = unique id
# object

