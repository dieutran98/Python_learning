import numpy as np
import os
import json
class point:
    def __init__(self, dict_data ):
        self.name = dict_data["name"]
        #self.value = [0]*2
        self.value = dict_data["value"] # value is a list
        self. color = dict_data["color"]
    """
    def __init__(self):
        self.name = ""
        self.value = [0]*2
        self. color = ""
    """

    def print(self):
        print ("'{name}', {value}, '{color}' ".format(name=self.name, value=self.value, color=self.color))
        #print("===================================================================")

    def save_json(self, save_file):
        point_dict={
            "name": self.name,
            "value": self.value,
            "color": self.color
        }
        content = []
        #check if file isn't empty then do code below
        if not os.stat(save_file).st_size == 0:
            with open(save_file,"r") as save_f:
                content = ( json.load(save_f))
        # if file is empty just need to do code below
        content.append(point_dict)
        json_obj = json.dumps(content, indent=4)
        with open(save_file, "w") as save_f: 
            save_f.write(json_obj)
    def __add__(self, a):
        name = chr(ord(a.name) + 1)
        value = np.array(self.value) + np.array(a.value)
        dict_data ={
            "name": name,
            "value": value,
            "color": self.color
        }

        return point(dict_data)
    def __sub__(self, a):
        name = chr(ord(a.name) + 1)
        value = np.array(self.value) - np.array(a.value)
        dict_data ={
            "name": name,
            "value": value,
            "color": self.color
        }

        return point(dict_data)
    def convert_dict(self):
        dict_data ={
            "name": self.name,
            "value": self.value,
            "color": self.color,
        }
        return dict_data