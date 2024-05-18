import json


class PlantUMLGenerator:
    @staticmethod
    def generate_plantuml(json_data):
        data = json.loads(json_data)
        # 提取用例信息
        actors = data['actors']
        usecase = data['usecase']
        relationships = data['relationships']

        # 生成 PlantUML 语法
        plantuml_code = f"@startuml\n"
        plantuml_code += f"left to right direction\n\n"

        # 添加参与者（actors）
        for actor in actors:
            plantuml_code += f"actor {actor['name']}\n"

        # 添加用例（use case）
        for usecase in usecase:
            plantuml_code += f"usecase {usecase['name']}\n"

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

        return plantuml_code


# 示例用法
json_data = '''
{
    "actors": [
        {"name": "User"},
        {"name": "Admin"}
    ],
    "usecase": [
        {"name": "Login"},
        {"name": "Logout"}
    ],
    "relationships": [
        {"Initiator": "Login", "receiver": "Logout", "type": "dependency", "msg": "<<include>>"},
        {"Initiator": "User", "receiver": "Login", "type": "association", "msg": ""}
    ]
}
'''

plantuml_code = PlantUMLGenerator.generate_plantuml(json_data)
print(plantuml_code)