# 用例图
var1 = {
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
        {"Initiator": "User", "receiver": "Login", "type": "association", "msg": ""},
    ]
}

# 时序图
var2 = {
    "actors": [
        {"name": "User"},
    ],
    "boundarys": [
        {"name": "loginUI"}
    ],
    "controls": [
        {"name": "LoginManager"}
    ],
    "entitys": [
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
        {"Initiator": "loginUI", "receiver": "LoginManager", "type": "message", "msg": "login(account,password)"},
        {"Initiator": "LoginManager", "receiver": "UserLibrary", "type": "message",
         "msg": "VerifyUserValidity(account,password)"},
        {"Initiator": "UserLibrary", "receiver": "LoginManager", "type": "returnMessage", "msg": "UserValidity"},
        {"Initiator": "LoginManager", "receiver": "loginUI", "type": "returnMessage", "msg": "LoginResult"},
        {"Initiator": "LoginManager", "receiver": "LoginManager", "type": "selfMessage", "msg": "test"},
    ]
}

# 分析类图
var3 = {
    "abstracts": [
        {
            "name": "abstract"
        }
    ],
    "abstract_classes": [
        {
            "name": "abstract class"
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
            "name": "class"
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
        {
            {"object": "class", "methodName": "field1", "type": "private"},
            {"object": "class", "methodName": "field2", "type": "protected"},
            {"object": "class", "methodName": "method1", "type": "packagePrivate"},
            {"object": "class", "methodName": "method2", "type": "public"}
        }
    ],
    "relationships": [
        # --|>泛化
        {"Initiator": "class1", "receiver": "class2", "type": "generalization"},
        # --*组合
        {"Initiator": "class1", "receiver": "class2", "type": "composition"},
        # --o聚合
        {"Initiator": "class1", "receiver": "class2", "type": "aggregation"},
        # -->单向关联
        {"Initiator": "class1", "receiver": "class2", "type": "association"},
        # --双向关联
        {"Initiator": "class1", "receiver": "class2", "type": "bidirectionalAssociation"},
        # ..>依赖
        {"Initiator": "class1", "receiver": "class2", "type": "dependency"},
        # ..|>实现
        {"Initiator": "class1", "receiver": "class2", "type": "realization"}
    ]
}

# 包图
var4 = {
    "packages": [
        {"name": "package1"},
        {"name": "package2"},
        {"name": "package3"}
    ],
    "interfaces": [
        {"name": "interface1"}
    ],
    "inclusions": [
        {"father": "package3", "child": ["package1", "package2", "interface1"]}
    ],
    "relationships": [
        {"Initiator": "package1", "receiver": "package2", "type": "generalization"},
        {"Initiator": "package1", "receiver": "package2", "type": "composition"},
        {"Initiator": "package1", "receiver": "package2", "type": "aggregation"},
        {"Initiator": "package1", "receiver": "package2", "type": "association"},
        {"Initiator": "package1", "receiver": "package2", "type": "bidirectionalAssociation"},
        {"Initiator": "package1", "receiver": "package2", "type": "dependency"},
        {"Initiator": "package1", "receiver": "package2", "type": "realization"}
    ]
}

# er图
var5 = {
    "tables": [
        {"name": "table1", "contents": ["PRIMARY_KEY(user_id) : int", "username : varchar"]},
        {"name": "table2",
         "contents": ["PRIMARY_KEY(detail_id) : int", "user_id : int *--{ table1 : FOREIGN_KEY(user_id) }"]},
        {"name": "test", "contents": ["PRIMARY_KEY(user_id) : int"]},
    ],
    "relationships": [
        {"Initiator": "table1", "receiver": "table2", "content": "for", "relationship": ["1","1"]},
    ]
}

# 活动图
var6 = {
    "flowsheeting": [
        {
            "flowsheeting": '''|Swimlane1|
start
:foo1;
|#AntiqueWhite|Swimlane2|
:foo2;
:foo3;
|Swimlane1|
:foo4;
|Swimlane2|
:foo5;
stop'''
        }
    ]
}
