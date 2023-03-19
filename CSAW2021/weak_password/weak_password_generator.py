from datetime import date, timedelta

start_date = date(1900, 1, 1)
end_date = date(2022, 1, 1)
delta = timedelta(days=1)

f = open("aaron_password_list.txt", "w")

while start_date <= end_date:
    curr_date = start_date.strftime("%Y%m%d")
    f.write(f"Aaron{curr_date}")
    f.write("\n")
    f.write(f"{curr_date}Aaron")
    f.write("\n")
    start_date += delta

f.close()