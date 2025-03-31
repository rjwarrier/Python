# Importing the datetime module
import datetime

# ✅ Get the current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)

# ✅ Get today's date only
today = datetime.date.today()
print("Today's Date:", today)

# ✅ Create a specific date
gst_registration_date = datetime.date(2023, 7, 1)
print("GST Registration Date:", gst_registration_date)

# ✅ Format the date in a readable string
formatted = today.strftime("%d-%m-%Y")  # DD-MM-YYYY format
print("Formatted Date:", formatted)

# ✅ Calculate date difference
due_date = datetime.date(2025, 4, 20)
days_remaining = (due_date - today).days  # Difference in days
print("Days left until due date:", days_remaining)
