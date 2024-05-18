from flask import Flask, jsonify
import json

app = Flask(__name__)

# 假设你有一个包含用例数据的 JSON 字符串或文件
json_data = '''  
{
    "flowsheetings": [
        {
            "flowsheeting": ["|Swimlane1|", "start", ":foo1;", "|#AntiqueWhite|Swimlane2|", ":foo2;", ":foo3;",
                             "|Swimlane1|", ":foo4;", "|Swimlane2|", ":foo5;", "stop"]
        }
    ]
}

'''

# 解析 JSON 数据
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