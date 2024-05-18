from flask import Flask, jsonify
import json

app = Flask(__name__)

# 假设你有一个包含用例数据的 JSON 字符串或文件
json_data = '''  
{
    "packages": [
        {"name": "package1", "child": [{"type": "package", "name": "package2"}, {"type": "package", "name": "package3"},
         {"type": "interface", "name": "interface1"}]},
        {"name": "package2", "child": []},
        {"name": "package3", "child": []}
    ],
    "interfaces": [
        {"name": "interface1"}
    ],
    "components": [
        {"name": "component1"}
    ],
    "relationships": [
        {"Initiator": "package3", "receiver": "package2", "type": "generalization", "msg": "test"},
        {"Initiator": "package3", "receiver": "package2", "type": "composition", "msg": ""},
        {"Initiator": "package3", "receiver": "package2", "type": "aggregation", "msg": "test"},
        {"Initiator": "package3", "receiver": "package2", "type": "association", "msg": "test"},
        {"Initiator": "package3", "receiver": "package2", "type": "bidirectionalAssociation", "msg": ""},
        {"Initiator": "package3", "receiver": "package2", "type": "dependency", "msg": ""},
        {"Initiator": "package3", "receiver": "package2", "type": "realization", "msg": ""}
    ]
}
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 提取用例信息
packages = data['packages']
interfaces = data['interfaces']
components = data['components']
relationships = data['relationships']

# 生成 PlantUML 语法
plantuml_code = f"@startuml\n"

# 添加包
for package in packages:
    if len(package['child']) != 0:
        plantuml_code += f"package {package['name']} "
        plantuml_code += "{\n"
        for child in package['child']:
            plantuml_code += f"{child['type']} {child['name']}\n"
        plantuml_code += "}\n"
    else:
        plantuml_code += f"package {package['name']}\n"

# 添加接口
for interface in interfaces:
    plantuml_code += f"interface {interface['name']}\n"

# 添加组件
for component in components:
    plantuml_code += f"component {component['name']}\n"

# 添加交互步骤
for relationship in relationships:
    # 依赖
    if relationship['type'] == "dependency":
        plantuml_code += f"{relationship['Initiator']} ..> {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 单向关联
    if relationship['type'] == "association":
        plantuml_code += f"{relationship['Initiator']} --> {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 泛化
    if relationship['type'] == "generalization":
        plantuml_code += f"{relationship['Initiator']} --|> {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 组合
    if relationship['type'] == "composition":
        plantuml_code += f"{relationship['Initiator']} --* {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 聚合
    if relationship['type'] == "aggregation":
        plantuml_code += f"{relationship['Initiator']} --o {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 双向关联
    if relationship['type'] == "bidirectionalAssociation":
        plantuml_code += f"{relationship['Initiator']} -- {relationship['receiver']} : \"{relationship['msg']}\"\n"
    # 实现
    if relationship['type'] == "realization":
        plantuml_code += f"{relationship['Initiator']} ..|> {relationship['receiver']} : \"{relationship['msg']}\"\n"

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