import csv


data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]


try:
    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Data written to packing_list.csv")
except Exception as e:
    print(f"Packing list file not found. Creating a new one.")
    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Data written to packing_list.csv")
    
    
