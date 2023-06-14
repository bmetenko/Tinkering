from datetime import datetime, timedelta

def main():
    # Two date strings in the format mm/dd/yyyy
    start_date_str = "05/24/2023"
    end_date_str = "06/08/2023"

    # Convert the date strings to datetime objects
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
    end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

    # Calculate the date range
    date_range = end_date - start_date

    # Loop and print
    for i in range(date_range.days + 1):
        current_date = end_date - timedelta(days=i)
        current_date_str = current_date.strftime("%d%b%Y - %A")
        print("### " + current_date_str + " \n \n")


if __name__ == "__main__":
    main()