from flask import Flask, jsonify
import json

app = Flask(__name__)

# 假设你有一个包含用例数据的 JSON 字符串或文件
json_data = '''  
{
    "tables": [
        {"name": "table1", "contents": ["PRIMARY_KEY(user_id) : int", "username : varchar"]},
        {"name": "table2",
         "contents": ["PRIMARY_KEY(detail_id) : int", "user_id : int *--{ table1 : FOREIGN_KEY(user_id) }"]},
        {"name": "test", "contents": ["PRIMARY_KEY(user_id) : int"]}
    ],
    "relationships": [
        {"Initiator": "table1", "receiver": "table2", "content": "for", "relationship": ["1","1"]},
        {"Initiator": "(table1,table2)", "receiver": "test", "content": "", "relationship": []}
    ]
}
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 提取用例信息
tables = data['tables']
relationships = data['relationships']

# 生成 PlantUML 语法
plantuml_code = f"@startuml\n"

# 添加表
for table in tables:
    plantuml_code += f"entity {table['name']} "
    plantuml_code += "{\n"
    for content in table['contents']:
        plantuml_code += f"content\n"
    plantuml_code += "}\n"

# 添加关系
for relationship in relationships:
    if len(relationship['relationship']) != 0:
        plantuml_code += f"{relationship['Initiator']} \"{relationship['relationship'][0]}\" - \"{relationship['relationship'][1]}\" {relationship['receiver']} "
    else:
        plantuml_code += f"{relationship['Initiator']} - {relationship['receiver']} "
    if len(relationship['content']) != 0:
        plantuml_code += f": {relationship['content']}\n"
    else:
        plantuml_code += "\n"

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