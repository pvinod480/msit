import os

def Directory_Size(g_path):
    total_size = 0
    for path, dirs, files in g_path:
        for f in files:
            fp = os.path.join(path, f)
            #total_size += os.path.getsize(fp)
            st = os.stat(fp)
            total_size+=st[6]
    return total_size
path="C:\\Users\\pvino\\OneDrive\\Desktop\\msit"
g_path = os.walk(path)

result = Directory_Size(g_path)

print("Directory size:{} KB ".format(result/1024))
