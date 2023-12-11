import pyperclip

sqldata = """
| AD_PRES    | President                       |      20000 |      40000 |
| AD_VP      | Administration Vice President   |      15000 |      30000 |
| AD_ASST    | Administration Assistant        |       3000 |       6000 |
| FI_MGR     | Finance Manager                 |       8200 |      16000 |
| FI_ACCOUNT | Accountant                      |       4200 |       9000 |
| AC_MGR     | Accounting Manager              |       8200 |      16000 |
| AC_ACCOUNT | Public Accountant               |       4200 |       9000 |
| SA_MAN     | Sales Manager                   |      10000 |      20000 |
| SA_REP     | Sales Representative            |       6000 |      12000 |
| PU_MAN     | Purchasing Manager              |       8000 |      15000 |
| PU_CLERK   | Purchasing Clerk                |       2500 |       5500 |
| ST_MAN     | Stock Manager                   |       5500 |       8500 |
| ST_CLERK   | Stock Clerk                     |       2000 |       5000 |
| SH_CLERK   | Shipping Clerk                  |       2500 |       5500 |
| IT_PROG    | Programmer                      |       4000 |      10000 |
| MK_MAN     | Marketing Manager               |       9000 |      15000 |
| MK_REP     | Marketing Representative        |       4000 |       9000 |
| HR_REP     | Human Resources Representative  |       4000 |       9000 |
| PR_REP     | Public Relations Representative |       4500 |      10500 |
"""


def extractor(data: str):
    # setting word count to go to the next line after certain number of words 
    word_count = 0
    total_columns = 4
    output = "("

    for w in data.split("|"):

        # if the word count reaches the number of words in the line we move to the next entry
        if word_count == total_columns:
            output = f"{output[:-1]}),\n("
            word_count = 0
        else:
            # stripping all the unwanted space from the content
            w = w.strip()
            # double check to remove any empty strings
            if w == "":
                print(w)
                continue

            # if the string is a number then we append the string without any quotations
            try:
                w_number = float(w)
                output = f"{output}{w_number},"
            except:
                output = f"{output}'{w}',"

            word_count += 1 


    # [:-3] to remove the last comma from the outpu
    out = str(output[:-3])
    print(out)
    # copying to the output to the clipboard
    pyperclip.copy(out)


if __name__ == "__main__":
    extractor(sqldata)

