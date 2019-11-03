# ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

def find_duplicate_file(paths):
    content_map = {}
    res = []

    for folder in paths:
        #  data = ["root/a", "1.txt(abcd)", "2.txt(efgh)""]
        data = folder.split()
        path = data[0]

        for i in range(1, len(data)):
            file = data[i]
            name,_, content = file.partition('(')
            content = content[:-1]
            # path = root/a
            #  file = 1.txt(abcd)
            #  name = 1.txt
            #  content = abcd
            if content in content_map.keys():
                res.append(path+name)
                path_list = content_map.get(content)
            else:
                path_list = []
            path_list.append(path+name)
            content_map[content] = path_list
    return res

        


        





