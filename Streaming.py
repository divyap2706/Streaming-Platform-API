def streamOnline(streamers, categories, nametoAdd, viewtoAdd, categoryToAdd):
    if not streamers.get(nametoAdd):
        streamers[nametoAdd] = {}
        streamers[nametoAdd].update({categoryToAdd: viewtoAdd})
            
    if not categories.get(categoryToAdd):
        categories[categoryToAdd] = {}
        categories[categoryToAdd].update({nametoAdd: viewtoAdd})

    else:
        categories[categoryToAdd].update({nametoAdd: viewtoAdd})


def updateViews(name, category, views):
    if((streamers.get(name)) and category in streamers[name].keys()):
        streamers[name][category] = views
        categories[category][name] = views

def updateCategory(name, oldcategory, newcategory):
    if((streamers.get(name)) and oldcategory in streamers[name].keys()):
        streamers.pop(name)
        streamers[name] = {}
        streamers[name].update({newcategory:0})
        categories[oldcategory].pop(name)
        categories[newcategory].update({name: 0})


def streamOffline(streamers, categories, name, category):
    if category in streamers[name].keys():
        streamers.pop(name)
        categories[category].pop(name)

def viewsInCategory(category):
    if not categories.get(category):
        return 0
    else:
        values = categories[category].values()
        total = sum(values)

    return total
        
def getTopStreamersInCategory(category):
    if(category not in categories.keys() and len(categories[category]) == 0):
        return None
    else:
        categoryStreamers = {k: v for k, v in sorted(categories[category].items(), key=lambda item: item[1], reverse=True)}
        categoryStreamersKey = categoryStreamers.keys()
        categoryStreamersKeyList = list(categoryStreamersKey)
        return categoryStreamersKeyList[0]

def getTopStreamer():
    for names in streamers.values():
        topStreamer = {k: v for k, v in sorted(names.items(), key=lambda item: item[1], reverse=True)}
        topStreamerKey = topStreamer.keys()
        topStreamerKeyList = list(topStreamerKey)
    return topStreamerKeyList[0]


# def getTopStreamersInCategory(category):
#     #handling category DNE
#     if category not in categories:
#         return None
#     if categories.get(category):
#         if length(categories[category]["Streamers"]) == 0:
#             return None
#         else:
#             categoryStreamers = categories.get(category)['streamer'] # ask Kunwar
#             # categoryStreamers = {k: v for k, v in sorted(categories[category].items(), key=lambda item: item[1], reverse=True)}
#             # categoryStreamersKey = categoryStreamers.keys()
#             # categoryStreamersKeyList = list(categoryStreamersKey)
#             # print(categoryStreamersKeyList[0])
            

#             top = ""
#             count = 0
#             for name in categoryStreamers:
#                 if streamers[name]['views'] > count:
#                     top = name

#             return name #ask Kunwar
#     # else:
#     #     return None

# # if length(categories[category]["Streamers"] == 1):
# #     return categories[category][streamer].get(views)



    
# def viewsinCategory(category):
#     if categories.get(category):
#         return categories[category]
#     else:
#         return 0


streamers = defaultdict(dict)
categories = defaultdict(dict)



# for names in streamers.values():
# 	print(names)
    
    
# dicttt = {}
# for names in streamers.values():
# 	dicttt.update(names)
    
# print(dicttt)

# topStreamer = {k: v for k, v in sorted(dicttt.items(), key=lambda item: item[1], reverse=True)}
# topStreamerKey = topStreamer.keys()
# topStreamerKeyList = list(topStreamerKey)
# print(topStreamerKeyList[0])
