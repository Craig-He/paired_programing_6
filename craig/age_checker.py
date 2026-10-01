from datetime import *

def age_checker(dob):
    d2 = date.today()
    d1 = datetime.strptime(dob, "%y/%m/%d").date()

    if not isinstance(d1, date):
        raise ValueError
    else:

        years = (d2.year - d1.year - ((d2.month,d2.day)<(d1.month, d1.day))) + 1

        if years < 16:
            return f"Access denied: You are {years}, you must be 16"
        else:
            return f"Access granted"
