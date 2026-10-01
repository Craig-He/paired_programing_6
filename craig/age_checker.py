from datetime import *

def age_checker(dob):
    d2 = date.today()
    d1 = datetime.strptime(dob, "%y/%m/%d").date()
    years = d2.year - d1.year - ((d2.month,d2.day)<(d1.month, d1.day))

    return years

