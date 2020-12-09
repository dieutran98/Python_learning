from point_class import point
import sys
import json
import os
import numpy as np

dict_list = []
cmd_split = []
dict_data ={
    "name": "",
    "value": [0]*2,
    "color": ""
}

dict_operator ={
    "+": "addP",
    "-": "sub",
    "*": "mul",
    "/": "dev",
    "=": "result"
}
key = 1 # print result if key = 1 else dont
res = point(dict_data)

class switch_case:
    def __init__(self,cmd):
        method = getattr(self,cmd,lambda: "invalid")
        return method()

    def add(none):
        try: 
            dict_data["name"] = cmd_split[1]
            dict_data["value"] = [int( cmd_split[2]),int( cmd_split[3])]
            dict_data["color"] = cmd_split[4]
            dict_list.append( point(dict_data))
            #print (dict_list)
        except:
            print("syntax error! please type: add name value color")

    def save(none):
        try:
            if not os.path.exists(cmd_split[1]):
                print("No path {} exist".format(cmd_split[1]))
                return 0
            for obj in dict_list:
                obj.save_json(cmd_split[1])
        except:
            print("syntax error! please type: save file_name.json")

    def dele(none):
        try:
            with open( cmd_split[1], "w") as save_f:
                save_f.write("")
            dict_list = []
        except:
            print("syntax error! please type: dele target_file")

    def import_data(none):
        try:
            if not os.path.exists(cmd_split[1]):
                print("No path {} exist".format(cmd_split[1]))
                return 0
            
            with open( cmd_split[1], 'r') as openfile: 
                json_object = json.load(openfile)
            #print(type(json_object))
            #print(dict_list)
            for obj in json_object:
                dict_list.append(point(obj))
            #print(dict_list)
            print("Imported: ",end="")
            for obj in dict_list:
                print("'{}',".format(obj.name),end=" ")
            print()
        except:
            print("syntax error! Please type: import_data file_name.json")
    
    def addP(none):
        try:
            for obj0 in dict_list:
                if obj0.name == cmd_split[0]:
                    #pa = obj0
                    break
            #print(obj0)
            for obj1 in dict_list:
                if obj1.name == cmd_split[2]:
                    #pb = obj1
                    break
            global res
            #print(obj1)
            res = obj0 + obj1
            if key == 1:
                print (res.value)
            #return res.value
        except:
            print("syntax error! Please type: <point> + <point>")

    def sub(none):
        try:
            for obj0 in dict_list:
                if obj0.name == cmd_split[0]:
                    #pa = obj0
                    break
            #print(obj0)
            for obj1 in dict_list:
                if obj1.name == cmd_split[2]:
                    #pb = obj1
                    break
            global res
            #print(obj1)
            res = obj0 - obj1
            if key == 1:
                print (res.value)
            #return res.value
        except:
            print("syntax error! Please type: <point> - <point>")
        
    def result(none):
        try:
            global cmd_split
            global key
            key = 0
            operator = cmd_split[3]
            cmd_split = cmd_split[2:]
            #print(cmd_split)
            switch_case(dict_operator[cmd_split[1]])
            #print(res.convert_dict())
            res.print()
            key = 1
            #return res
        except:
            print("syntax error! Please type: <point> = <point> <operator> <point>")
        
    def help(none):
        print("Usage: add <name> <value>(list) <color> ")
        print("       <point> <operator> <point> ")
        print("       <point> = <point> <operator> <point> ")
        print("       import_data file_name.json ")
        print("       dele target_file")
        print("       save file_name.json")
#def import_data():

while True:

    command = input("enter your input: ")
    cmd_split = command.split()
    
    try:
        if cmd_split[0] == "exit":
            break
        try:
            #print(dict_operator[cmd_split[1]])
            switch_case( dict_operator[ cmd_split[1]])
            continue
        except:
            #pass
            switch_case(cmd_split[0])
    except:
        print("syntax error!")
        print("type 'help' for help")