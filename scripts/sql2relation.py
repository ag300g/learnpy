
import re
import os
import pandas as pd

path = '/Users/****/CodeRepo/IntelliJProjects/****'

'''
extract relationship between tables
'''
column_child = []
column_parent = []
column_file = []
for dirpath, dirnames, filenames in os.walk(path):
    # print('dirpath:{}'.format(dirpath))
    # print('dirnames:{}'.format(dirnames))
    print('filenames:{}'.format(filenames))

    for filename in filenames:
        if '.sql' in filename:
            f = os.path.join(dirpath, filename)
            with open(f, 'r') as myfile:
                data = myfile.read().replace('\n', ' ')
                # 正则，flags=re.IGNORECASE：不区分大小写，'\s'不区分间隔符，可以
                blocks = re.split('CREATE\s+TABLE', data, flags=re.IGNORECASE) 
                # blocks[0]中没有建表语句
                for b in blocks[1:]:
                    child = re.findall('^\s*(\S+)', b)
                    parents = re.findall('(?:JOIN|FROM)\s+(\S+)', b, re.I)
                    for parent in parents:
                        if '(' in parent:
                            pass ## why this type is skiped??
                        else:
                            column_child.append(child[0])
                            column_parent.append(parent)
                            column_file.append(f)

res = pd.DataFrame({'child': column_child,
                    'parent': column_parent,
                    'filename': column_file})

'''
remove duplicates table names due to SQL case insensitive
'''
upper_name = dict()
for w in res.values.ravel():
    lw = w.lower()
    if lw in upper_name:
        upper_name[lw] = min(w, upper_name[lw])
    else:
        upper_name[lw] = w
res = res.applymap(lambda x: upper_name[x.lower()])
res[['filename','child','parent']].drop_duplicates().to_csv('table_relationship.csv')
