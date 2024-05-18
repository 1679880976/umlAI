from plantUml import plantumlUsecase
from plantUml import plantumlAnalyzing

# 准备你的 JSON 数据
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

# 使用 PlantUMLGenerator 类来生成 PlantUML 代码
plantuml_code = plantumlAnalyzing.generate_plantuml(json_data)

# 打印生成的 PlantUML 代码
print(plantuml_code)
