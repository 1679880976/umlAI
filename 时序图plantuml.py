from flask import Flask, jsonify
import json

app = Flask(__name__)

# 假设你有一个包含用例数据的 JSON 字符串或文件
json_data = '''  
{
    "actors": [
        {"name": "User"}
    ],
    "boundaries": [
        {"name": "loginUI"}
    ],
    "controls": [
        {"name": "LoginManager"}
    ],
    "entities": [
        {"name": "UserLibrary"}
    ],
    "databases": [
    ],
    "collections": [
    ],
    "queues": [
    ],
    "relationships": [
        {"Initiator": "User", "receiver": "loginUI", "type": "message", "msg": "goto"},
        {"Initiator": "", "receiver": "", "type": "groupBegin", "msg": "循环"},
        {"Initiator": "loginUI", "receiver": "LoginManager", "type": "message", "msg": "login(account,password)"},
        {"Initiator": "LoginManager", "receiver": "UserLibrary", "type": "message",
         "msg": "VerifyUserValidity(account,password)"},
        {"Initiator": "UserLibrary", "receiver": "LoginManager", "type": "returnMessage", "msg": "UserValidity"},
        {"Initiator": "LoginManager", "receiver": "loginUI", "type": "returnMessage", "msg": "LoginResult"},
        {"Initiator": "", "receiver": "", "type": "groupEnd", "msg": ""},
        {"Initiator": "LoginManager", "receiver": "LoginManager", "type": "selfMessage", "msg": "test"}
    ]
}
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 提取用例信息
actors = data['actors']
boundaries = data['boundaries']
controls = data['controls']
entities = data['entities']
databases = data['databases']
collections = data['collections']
queues = data['queues']
relationships = data['relationships']

# 生成 PlantUML 语法
plantuml_code = f"@startuml\n"

# 添加参与者（actors）
for actor in actors:
    plantuml_code += f"actor {actor['name']}\n"
    plantuml_code += f"activate {actor['name']}\n"

# 添加边界类(boundaries)
for boundary in boundaries:
    plantuml_code += f"boundary {boundary['name']}\n"
    plantuml_code += f"activate {boundary['name']}\n"

# 添加控制类(controls)
for control in controls:
    plantuml_code += f"control {control['name']}\n"
    plantuml_code += f"activate {control['name']}\n"

# 添加实体类(entities)
for entity in entities:
    plantuml_code += f"entity {entity['name']}\n"
    plantuml_code += f"activate {entity['name']}\n"

# 添加数据库类(databases)
for database in databases:
    plantuml_code += f"database {database['name']}\n"
    plantuml_code += f"activate {database['name']}\n"

# 添加集合类(collections)
for collection in collections:
    plantuml_code += f"collection {collection['name']}\n"
    plantuml_code += f"activate {collection['name']}\n"

# 添加队列类(queues)
for queue in queues:
    plantuml_code += f"queue {queue['name']}\n"
    plantuml_code += f"activate {queue['name']}\n"

# 添加交互步骤
for relationship in relationships:
    # 消息
    if relationship['type'] == "message":
        plantuml_code += f"{relationship['Initiator']} -> {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 自消息
    if relationship['type'] == "selfMessage":
        plantuml_code += f"{relationship['Initiator']} -> {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 返回信息
    if relationship['type'] == "returnMessage":
        plantuml_code += f"{relationship['Initiator']} --> {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 组框开始
    if relationship['type'] == "groupBegin":
        plantuml_code += f"group {relationship['msg']}\n"
    # 组框结束
    if relationship['type'] == "groupEnd":
        plantuml_code += f"end\n"

# 结束 PlantUML 语法
plantuml_code += "@enduml\n"

# 打印或保存 PlantUML 语法
print(plantuml_code)

# 定义一个接口，返回包含 PlantUML 语法的 JSON 对象
# @app.route('/get_plantuml', methods=['GET'])
# def get_plantuml():
#     # 将 plantuml_code 放入一个字典中
#     response_data = {
#         'plantuml_code': plantuml_code
#     }
#     # 将字典转换为 JSON 格式的响应并返回
#     return jsonify(response_data)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)