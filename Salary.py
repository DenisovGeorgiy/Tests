def expenses(salary, percent_mortgage, percent_life):
    mortgage_month = salary / 100 * percent_mortgage
    mortgage = mortgage_month * 12
    result = (salary - ((salary / 100 * percent_life) + mortgage_month)) * 12

    return  mortgage

def savings(salary, percent_mortgage, percent_life):
    mortgage_month = salary / 100 * percent_mortgage
    mortgage = mortgage_month * 12
    result = (salary - ((salary / 100 * percent_life) + mortgage_month)) * 12

    return result

