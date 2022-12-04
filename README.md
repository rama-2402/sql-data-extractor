# sql-data-extractor
A simple python script to extract data from sql output data

## What does it do?
As the description tells, This simple script extracts the tabled sql output data into a data format that can be used as input data for INSERT INTO statements.

Often I come across examples in websites where only the tabled data output will be given. It is painstakingly hard to type the data for INSERT INTO statements for populating a random database for practice. So this simple script can be used to get the data in the formatted way.

## How to use

- Paste the sql output in the "sqldata" string
- Set the **"total_columns"** variable to the number of columns in the tabled output
- The script uses "pyperclip" module to copy the output to clipboard. Run the following command to first install the pyperclip module for the script to work or you can comment out the import (line 1) and it's usage in (line 148). 

```
pip install pyperclip
```
