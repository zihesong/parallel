import os
import json
from jsonpath import jsonpath 
from graphviz import Digraph


# path = '/Users/apple/Desktop/OCR'

# path_list = os.listdir(path)

# path_list.remove('crash.log')
# path_list.remove('tool.log')
# path_list.sort(key=lambda x:int(x.split('.')[0]))




graph = Digraph(name="Activity Map", format="png",strict=True)

for j in range(1,7):
    folder_name = 'ape-autoscout24/ape-autoscout24-'+str(j)+'/'
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
        cur_act = act[i]
        graph.node(act[i])
        graph.edge(act[i-1], act[i])

graph.view()

