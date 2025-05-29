import os


def list_all_files(root_dir):
    files = []
    for entry in reversed(os.listdir(root_dir)):
        full_path = os.path.join(root_dir, entry).replace("\\","/")
        if os.path.isdir(full_path) and entry != ".git":
            files.extend(list_all_files(full_path))
        elif ("  "+entry)[-2:].lower() == "md":
            files.append(full_path)
    return files


file = open("./Site map.md", "w")
for f in list_all_files("./"):
    path = f[2:]
    name = ""
    if f.endswith("README.md"): name = ([".","."]+f.split("/"))[-2]
    else: name = f.split("/")[-1][:-3]
    file.write("["+name+"](./article.html?a="+path+")\n")
    