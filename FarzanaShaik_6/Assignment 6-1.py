import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def read_employee_info_from_json(file_name):
    employee_list = []
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            for emp_info in data['employees']:
                employee = Employee(emp_info['Name'], emp_info['DOB'], emp_info['Height'], emp_info['City'], emp_info['State'])
                employee_list.append(employee)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    return employee_list

def write_dict_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

employee_data = {
    "employees": [
        {
            "Name": "John",
            "DOB": "1990-05-15",
            "Height": 175,
            "City": "New York",
            "State": "NY"
        },
        {
            "Name": "Alice",
            "DOB": "1988-09-23",
            "Height": 160,
            "City": "Los Angeles",
            "State": "CA"
        },
        {
            "Name": "Bob",
            "DOB": "1995-03-10",
            "Height": 182,
            "City": "Chicago",
            "State": "IL"
        },
        {
            "Name": "Eva",
            "DOB": "1985-12-04",
            "Height": 168,
            "City": "Houston",
            "State": "TX"
        },
        {
            "Name": "David",
            "DOB": "1992-07-30",
            "Height": 175,
            "City": "Miami",
            "State": "FL"
        }
    ]
}

with open('employee.json', 'w') as json_file:
    json.dump(employee_data, json_file, indent=4)

employee_list = read_employee_info_from_json('employee.json')

for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")

indian_states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Rajasthan": "Jaipur",
    "Tamil Nadu": "Chennai"
}

write_dict_to_json(indian_states_and_capitals, 'indian_states.json')