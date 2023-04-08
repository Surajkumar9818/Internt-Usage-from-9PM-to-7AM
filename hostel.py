import psutil
import datetime
import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.title("Internet Usage Report")
window.geometry("300x100")

start_time = datetime.time(21, 0, 0) # 9:00 PM
end_time = datetime.time(7, 0, 0) # 7:00 AM

network_data = psutil.net_io_counters()
bytes_sent = network_data.bytes_sent
bytes_received = network_data.bytes_recv

current_time = datetime.datetime.now().time()

if start_time <= current_time or current_time <= end_time:
    internet_usage = bytes_sent + bytes_received
else:
    internet_usage = 0

# Create a label to display the report
report_label = tk.Label(window, text=f"Internet usage from {start_time.strftime('%I:%M %p')} to {end_time.strftime('%I:%M %p')}: {internet_usage} bytes")
report_label.pack(pady=20)

# Start the tkinter mainloop
window.mainloop()
