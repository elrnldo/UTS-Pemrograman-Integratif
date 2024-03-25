from datetime import date, timedelta

def get_future_date(days):
  today = date.today()
  future_date = today + timedelta(days=days)
  # strftime allows formatting the date object
  formatted_date = future_date.strftime("%A on %B %d %Y")
  return formatted_date

# Get the number of days from the user (replace with actual input method if needed)
days_from_now = int(input("Enter the number of days from now: "))

# Calculate and print the future date
future_date_str = get_future_date(days_from_now)
print(future_date_str)
