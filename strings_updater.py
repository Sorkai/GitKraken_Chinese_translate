#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 转移已有翻译到最新的string_json文件中

import json
import os

path_json_raw = "./strings_default.json"
path_json_trans = "./strings_old.json"
path_json_final = "./strings_final.json"

path_json_raw = os.path.realpath(path_json_raw)
path_json_trans = os.path.realpath(path_json_trans)
path_json_final = os.path.realpath(path_json_final)

path_sys = os.environ["localappdata"]
path_app_bin = os.path.join(path_sys, "gitkraken/bin/gitkraken.cmd")
path_app_res = os.path.join(path_sys, "gitkraken")
path_app_version = ""  # 下面获取

if not os.path.isfile(path_app_bin):
    print("检测到电脑未安装gitkraken，程序退出")
    exit()
with open(path_app_bin, 'r', encoding="utf-8") as f:
    line = f.readline()
    line = f.readline()
    # print(line)
    line_index_s = line.find("app-")
    line_index_e = line.find("resources")
    path_app_version = line[line_index_s:line_index_e - 1]
    path_app_res = os.path.join(path_app_res,
                                path_app_version,
                                "resources/app.asar.unpacked/src/strings.json")
    path_app_res = os.path.realpath(path_app_res)
    # print(path_app_res)
    if not os.path.isfile(path_app_res):
        print("未获取到gitkraken原始资源路径，程序退出")
        exit()
    os.system("copy /y {} {}".format(path_app_res, path_json_raw))


# 开始进行合并

d_trans = {}
d_raw = {}
d_final = {}

with open(path_json_trans, 'r', encoding="utf-8") as f_trans:
    d_trans = json.load(f_trans)

with open(path_json_raw, 'r', encoding="utf-8") as f_raw:
    d_raw = json.load(f_raw)

for key, val in d_trans['menuStrings'].items():
    d_raw['menuStrings'][key] = val

for key, val in d_trans['strings'].items():
    d_raw['strings'][key] = val

d_final = d_raw

# for key,val in d_raw['menuStrings'].items():
#     print(key,val)

with open(path_json_final, 'w', encoding="utf-8") as f_final:
    json.dump(d_final, f_final, ensure_ascii=False)

exit()
# 下面暂时注释，修改string_final.json完善最新翻译，然后自行复制或者使用install.bat复制

if os.path.isfile(path_json_final):
    print(path_json_final, '\n', path_app_res)
    os.system("copy /y {} {}".format(path_json_final, path_app_res))
    print("复制升级后文件到程序内成功")

print("Done.")
