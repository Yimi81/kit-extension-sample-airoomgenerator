import json

# 原数据
data = {
    "area_name": "Test_Area",
    "X": 0.0,
    "Y": 0.0,
    "Z": 0.0,
    "area_size_X": 244.81475830078125,
    "area_size_Z": 273.92938232421875,
    "area_objects_list": [
        {
            "object_name": "Dining_Table",
            "X": 0.0,
            "Y": 0.0,
            "Z": 0.0,
            "Length": 100,
            "Width": 75,
            "Height": 75,
            "Material": "Oak"
        },
        {
            "object_name": "Chair_1",
            "X": 0.0,
            "Y": 0.0,
            "Z": -60.0,
            "Length": 45,
            "Width": 45,
            "Height": 90,
            "Material": "Mahogany"
        },
        {
            "object_name": "Chair_2",
            "X": 0.0,
            "Y": 0.0,
            "Z": 60.0,
            "Length": 45,
            "Width": 45,
            "Height": 90,
            "Material": "Mahogany"
        },
        {
            "object_name": "Chair_3",
            "X": -60.0,
            "Y": 0.0,
            "Z": 0.0,
            "Length": 45,
            "Width": 45,
            "Height": 90,
            "Material": "Mahogany"
        },
        {
            "object_name": "Chair_4",
            "X": 60.0,
            "Y": 0.0,
            "Z": 0.0,
            "Length": 45,
            "Width": 45,
            "Height": 90,
            "Material": "Mahogany"
        }
    ]
}


# 将字典保存到JSON文件中，并指定缩进参数以提高可读性
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("数据已保存到 output.json 文件中。")