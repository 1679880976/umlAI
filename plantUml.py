import json


# 用例图
class plantumlUsecase:
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


# 分析类图
class plantumlAnalyzing:
    @staticmethod
    def generate_plantuml(json_data):
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

        # 添加方法(methods)
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

        return plantuml_code


# 包图
class plantumlPackage:
    @staticmethod
    def generate_plantuml(json_data):
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

        return plantuml_code


# 时序图
class plantumlSequence:
    @staticmethod
    def generate_plantuml(json_data):
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

        return plantuml_code


# 活动图
class plantumlActivity:
    @staticmethod
    def generate_plantuml(json_data):
        data = json.loads(json_data)
        # 提取用例信息
        flowsheetings = data['flowsheetings']

        # 生成 PlantUML 语法
        plantuml_code = f"@startuml\n"

        for flowsheeting in flowsheetings:
            for item in flowsheeting["flowsheeting"]:
                plantuml_code += f"{item}\n"

        # 结束 PlantUML 语法
        plantuml_code += "@enduml\n"

        return plantuml_code


# er图
class plantumlEr:
    @staticmethod
    def generate_plantuml(json_data):
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

        return plantuml_code
