
header = """
rowid int,
orderid varchar(15),
orderdata date,
shipdate date,
shipmode varchar(15),
customerid varchar(12),
customername varchar(50),
segment varchar(10),
country varchar(15),
city varchar(30),
state varchar(20),
postalcode varchar(10),
region varchar(10),
productid varchar(25),
category varchar(15),
subcategory varchar(15),
productname varchar(100),
sales float,
quantity int,
discount float,
profit float
"""

data = """
a
"""

def header_to_dict() -> dict:
    # splitting the string into a list
    header_items = header.split("\n")

    # checks if the column names and types are in a single line or new lines
    if len(header_items) > 3:
        # if new lines we remove the first and last new lines from the list 
        header_items.pop(0)
        header_items.pop()
    else:
        # if in a single line we remove the first and last new lines from the list and split it by commas
        header_items.pop(0)
        header_items.pop()
        header_items = header.split(",")

    header_dict = dict()
    # populating the header dictionary by col name key and data type as values
    for item in header_items:
        header_dict[item.split(" ")[0].replace("\n", "")] = item.split(" ")[1].replace("\n", "")

    return header_dict

def parse_data(header_dict: dict):


if __name__ == "__main__":
    if not data.strip() or not header.strip():
        print("Please provide all the input data to parse")
    else:
        parse_data(header_to_dict())
    


