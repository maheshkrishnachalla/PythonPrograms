import sys
from datetime import datetime
from Date_Calculation import find_date_diff
from Read_CSV_Data import read_data


def interest_calculation(principle, time, rate_of_interest=1.5):
    years = time[0]
    months = time[1]
    days = time[2]
    compound_interest = 0.0
    total_principle = principle
    """print("default rate_of_interest = 1.5", end=' ')
    r = input("Please enter Y/N:")[0]
    if r == 'n' or r == 'N':
        rate_of_interest = float(input("rate of interest = "))
    """
    for year in range(1, years + 1):
        simple_interest = 12 * (principle * rate_of_interest) / 100
        print("interest of year_{} = {}".format(year, simple_interest))
        principle = simple_interest + principle
        print("principle after year_{} = {}".format(year, principle))
        compound_interest = compound_interest + simple_interest

    compound_principle = principle

    """if years > 1:
        print("{} years interest = {}".format(years, compound_interest))
        print("after {} years principle = {}".format(years, compound_principle))
    """
    monthly_interest = compound_principle * rate_of_interest * months / 100
    compound_principle = compound_principle + monthly_interest

    if months > 0 and years > 0:
        print("{} months interest = {}".format(months, monthly_interest))
        print("after {} years {} months principle = {}".format(years, months, compound_principle))
    elif months > 0:
        print("{} months interest = {}".format(months, monthly_interest))
        print("after {} months principle = {}".format(months, compound_principle))

    daily_interest = compound_principle * rate_of_interest * days / (100 * 30)
    compound_principle = compound_principle + daily_interest

    if days > 0 and months > 0 and years > 0:
        print("{} days interest = {}".format(days, daily_interest))
        print("after {} years {} months {} days principle = {}".format(years, months, days, compound_principle))
    elif days > 0 and months > 0:
        print("{} days interest = {}".format(days, daily_interest))
        print("after {} months {} days principle = {}".format(months, days, compound_principle))
    elif days > 0:
        print("{} days interest = {}".format(days, daily_interest))
        print("after {} days principle = {}".format(days, compound_principle))

    total_interest = compound_interest + monthly_interest + daily_interest

    amount = total_principle + total_interest
    interest_per_day = amount * rate_of_interest / (100 * 30)

    print("...................................................")
    print("Principle =", total_principle)
    print("Interest =", total_interest)
    print("Amount =", amount)
    print("Interest per day from now =", interest_per_day)
    return total_principle, total_interest, interest_per_day


total_Principle = 0.0
total_Interest = 0.0
total_Amount = 0.0
total_interest_per_day = 0.0


def main():
    global total_Interest, total_interest_per_day, total_Principle, total_Amount
    print("Calculations of Interests on ", datetime.now())
    file_path = "interest.csv"
    row = read_data(load_file_path=file_path)
    for i in row:
        principle = float(i[1])
        rate_of_interest = float(i[2])
        start_date = i[3]
        end_date = str(datetime.now().date())
        print()
        print(
            "========================================================================================================")
        print("Amount from person :", i[0])
        print(
            "principle = {}, rate_of_interest = {}, start_date = {}, end_date = {}".format(principle, rate_of_interest,
                                                                                           start_date, end_date))

        date_diff = find_date_diff(start_dt=start_date, end_dt=end_date)
        years, months, days = date_diff[0], date_diff[1], date_diff[2]
        # if days > 0:
        #   days = days - 1
        print("years:{}, months:{}, days:{} ".format(years, months, days))
        date_diff = (years, months, days)
        amount = interest_calculation(principle=principle, time=date_diff, rate_of_interest=rate_of_interest)

        total_Principle = total_Principle + amount[0]
        total_Interest = total_Interest + amount[1]
        total_Amount = total_Principle + total_Interest
        total_interest_per_day = total_interest_per_day + amount[2]

    print(
        "================================================================================================")
    print("Total Principle = {}".format(total_Principle))
    print("Total Interest = {}".format(total_Interest))
    print("Total Amount = {}".format(total_Amount))
    print("...........................................................................................")
    print("Interest_Per_Day from now on Amount {} = {}".format(total_Amount, total_interest_per_day))

    """try:
        while True:
            end_date = input("end date = ")
            start_date = input("start date = ")

            principle = float(input("principle = "))
            # rate_of_interest = float(input("rate of interest = "))

            date_diff = find_date_diff(start_dt=start_date, end_dt=end_date)
            years, months, days = date_diff[0], date_diff[1], date_diff[2]
            if days > 0:
                days = days - 1
            print("years:{}, months:{}, days:{} ".format(years, months, days))
            date_diff = (years, months, days)
            amount = interest_calculation(principle=principle, time=date_diff)

            total_Principle = total_Principle + amount[0]
            total_Interest = total_Interest + amount[1]
            total_Amount = total_Principle + total_Interest

            print("==============================================")
            x = int(input("Enter 1 to continue:"))
            if x == 1:
                pass
    except ValueError:
        print("******* Thank you ********")
        print()
    finally:
        print("Total Principle = {}".format(total_Principle))
        print("Total Interest = {}".format(total_Interest))
        print("Total Amount = {}".format(total_Amount))
    """


if __name__ == "__main__":
    sys.stdout = open("result.txt", "w")
    main()
    sys.stdout.close()
