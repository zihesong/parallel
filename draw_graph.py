import os
import json
import sys
from jsonpath import jsonpath 
from graphviz import Digraph


app_name = sys.argv[1]

graph = Digraph(name="Activity Map", format="png",strict=True)

for j in range(1,7):
    folder_name = app_name + '/' + app_name + '-' + str(j) + '/'
    file_list = [fn for fn in os.listdir(folder_name) if fn.endswith('.json')]
    file_list.sort()
    
    act = []
    try:
        for file in file_list:
            with open(folder_name + file) as f:
                js = json.loads(f.readline())
                act += jsonpath(js, "$..act_id") 

    except Exception as e:
        print('Error: {}'.format(e))
        print(file)


    graph.node(act[0])
    for i in range(1,len(act)):
        if int(act[i].split('.')[0]) < int(act[i+1].split('.')[0]):
            cur_act = act[i]
            graph.node(act[i])
            graph.edge(act[i-1], act[i])
        else: 
            print("sort error!!!")

graph.view()


