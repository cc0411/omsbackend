# -*- coding:utf-8 -*-

list3 =[{'name': '游戏', 'id': 1, 'parent_unit': None},
        {'name': '一统地球', 'id': 2, 'parent_unit':"游戏" },
        {'name': '平台', 'id': 3, 'parent_unit': None},
        {'name': '天下一统', 'id': 4, 'parent_unit': "平台"},
        {'name': '天下一统2', 'id': 5, 'parent_unit': "天下一统"},
        ]


list4 =[]



list5 = [{'name': '游戏', 'id': 1, 'child': {'name': '一统地球', 'id': 2}},
         {'name': '平台', 'id': 3, 'child': {'name': '天下一统', 'id': 4, 'child': {'name': '天下一统2', 'id': 5}}}]

for item in  list3:
    for  dic in  list4:
        if item['parent_unit'] == dic['name']:
            dic['child']=({'name':item['name'],'id':item["id"]})
            break
        if  item['parent_unit'] == dic['child']['name']:
            dic['child']['child'] = ({'name': item['name'], 'id': item["id"]})
            break
    else:
        list4.append({"name":item["name"],"id":item["id"],"child":{}})
#print(list4)
#for item in list3:
#    for dic in list4:
#        if item['name'] == dic['name']:
#            dic['hobby_list'].append(item['hobby'])
#            break
#    else:
#        list4.append({"name":item["name"],"hobby_list":[item['hobby']]})
#

