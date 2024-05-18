from flask import Flask, jsonify
import json

app = Flask(__name__)

# 假设你有一个包含用例数据的 JSON 字符串或文件
json_data = '''  
{
    "abstracts": [
        {
            "name": "abstract"
        }
    ],
    "annotations": [
        {
            "name": "annotation"
        }
    ],
    "circles": [
        {
            "name": "circle"
        }
    ],
    "()": [
        {
            "name": "circle_short_forms"
        }
    ],
    "classes": [
        {
            "name": "class1"
        },
        {
            "name": "class2"
        }
    ],
    "diamonds": [
        {
            "name": "diamond"
        }
    ],
    "<>": [
        {
            "name": "diamond_short_forms"
        }
    ],
    "entities": [
        {
            "name": "entity"
        }
    ],
    "enums": [
        {
            "name": "enum"
        }
    ],
    "exceptions": [
        {
            "name": "exception"
        }
    ],
    "interfaces": [
        {
            "name": "interface"
        }
    ],
    "metaclasses": [
        {
            "name": "metaclass"
        }
    ],
    "protocols": [
        {
            "name": "protocol"
        }
    ],
    "stereotypes": [
        {
            "name": "stereotype"
        }
    ],
    "structs": [
        {
            "name": "struct"
        }
    ],
    "methods": [
            {"type": "class", "name": "class1", "methodName": "field1", "methodType": "private"},
            {"type": "class", "name": "class1", "methodName": "field2", "methodType": "protected"},
            {"type": "class", "name": "class1", "methodName": "method1", "methodType": "packagePrivate"},
            {"type": "class", "name": "class1", "methodName": "method2", "methodType": "public"}
    ],
    "relationships": [
        {"Initiator": "class1", "receiver": "class2", "type": "generalization", "msg": "test"},
        {"Initiator": "class1", "receiver": "class2", "type": "composition", "msg": ""},
        {"Initiator": "class1", "receiver": "class2", "type": "aggregation", "msg": ""},
        {"Initiator": "class1", "receiver": "class2", "type": "association", "msg": ""},
        {"Initiator": "class1", "receiver": "class2", "type": "bidirectionalAssociation", "msg": ""},
        {"Initiator": "class1", "receiver": "class2", "type": "dependency", "msg": ""},
        {"Initiator": "class1", "receiver": "class2", "type": "realization", "msg": ""}
    ]
}
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 提取用例信息
abstracts = data['abstracts']
annotations = data['annotations']
circles = data['circles']
circleShortForms = data['()']
classes = data['classes']
diamonds = data['diamonds']
diamondShortForms = data['<>']
entities = data['entities']
enums = data['enums']
exceptions = data['exceptions']
interfaces = data['interfaces']
metaclasses = data['metaclasses']
protocols = data['protocols']
stereotypes = data['stereotypes']
structs = data['structs']

methods = data['methods']
relationships = data['relationships']

# 生成 PlantUML 语法
plantuml_code = f"@startuml\n"

#添加方法(methods)
for method in methods:
    plantuml_code += f"{method['type']} {method['name']} \n"
    plantuml_code += "{\n"
    if method['methodType'] == "private":
        plantuml_code += f"-{method['methodName']}\n"
    if method['methodType'] == "protected":
        plantuml_code += f"#{method['methodName']}\n"
    if method['methodType'] == "packagePrivate":
        plantuml_code += f"~{method['methodName']}\n"
    if method['methodType'] == "public":
        plantuml_code += f"+{method['methodName']}\n"
    plantuml_code += "}\n"

# 添加对象
for abstract in abstracts:
    plantuml_code += f"abstract {abstract['name']}\n"

for annotation in annotations:
    plantuml_code += f"annotation {annotation['name']}\n"

for circle in circles:
    plantuml_code += f"circle {circle['name']}\n"

for circleShortForm in circleShortForms:
    plantuml_code += f"() {circleShortForm['name']}\n"

for classe in classes:
    plantuml_code += f"class {classe['name']}\n"

for diamond in diamonds:
    plantuml_code += f"diamond {diamond['name']}\n"

for diamondShortForm in diamondShortForms:
    plantuml_code += f"<> {diamondShortForm['name']}\n"

for entity in entities:
    plantuml_code += f"entity {entity['name']}\n"

for enum in enums:
    plantuml_code += f"enum {enum['name']}\n"

for exception in exceptions:
    plantuml_code += f"exception {exception['name']}\n"

for interface in interfaces:
    plantuml_code += f"interface {interface['name']}\n"

for metaclass in metaclasses:
    plantuml_code += f"metaclass {metaclass['name']}\n"

for protocol in protocols:
    plantuml_code += f"protocol {protocol['name']}\n"

for stereotype in stereotypes:
    plantuml_code += f"stereotype {stereotype['name']}\n"

for struct in structs:
    plantuml_code += f"struct {struct['name']}\n"


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