import datetime, os

def calculateAge():
    birth_day = int(input('\nDate of the brith. Ex- 01, 28, etc.\nAnswer : '))
    dob_month = (input('\nMonth of the brith. Ex- 02, february, etc.\nAnswer : '))
    birth_year = int(input('\nYear of the brith. Ex- 1980, 2002, etc.\nAnswer : '))
    months = {
        'january': '1',
        'february': '2',
        'march': '3',
        'april': '4',
        'may': '5',
        'june': '6',
        'july': '7',
        'august': '8',
        'september': '9',
        'ocober': '10',
        'november': '11',
        'december': '12'
    }
    try:
        birth_month = int(months[dob_month])
    except KeyError:
        birth_month = int(dob_month)
    now = datetime.datetime.now()
    # print(now)
    D = now.strftime('%d')
    M = now.strftime('%m')
    Y = now.strftime('%Y')
    given_day = int(D)
    given_month = int(M)
    given_year = int(Y)
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (birth_day > given_day):
        given_month = given_month - 1  # 0
        given_day = given_day + month[given_month-1]  # 13 + 1 = 14
    if (birth_month > given_month):
        given_year = given_year - 1  # 2023
        given_month = given_month + 12  #12
    # calculate day, month, year
    calculated_day = given_day - birth_day #14-13 = 1
    calculated_month = given_month - birth_month #12-02 = 10
    calculated_year = given_year - birth_year #23-23 = 0
    os.system('cls')
    print(f'-----------------------------> Today <----------------------------\n\n==>Your age is :  {str(calculated_year)} Year, {str(calculated_month)} Month, {str(calculated_day)} Day\n\n')
if __name__ == "__main__":
    calculateAge()