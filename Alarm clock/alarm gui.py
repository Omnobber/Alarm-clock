import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import winsound
from ttkthemes import ThemedStyle

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("300x150")
        
        self.hour = tk.StringVar()
        self.minute = tk.StringVar()
        self.am_pm = tk.StringVar()
        
        self.hour.set("00")
        self.minute.set("00")
        self.am_pm.set("AM")
        
        self.create_widgets()
        
    def create_widgets(self):
        style = ThemedStyle(self.root)
        style.set_theme("equilux")
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        hour_label = ttk.Label(main_frame, text="Hour:")
        hour_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.hour_entry = ttk.Combobox(main_frame, textvariable=self.hour, values=[str(i).zfill(2) for i in range(1, 13)], width=5)
        self.hour_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        minute_label = ttk.Label(main_frame, text="Minute:")
        minute_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.minute_entry = ttk.Combobox(main_frame, textvariable=self.minute, values=[str(i).zfill(2) for i in range(0, 60)], width=5)
        self.minute_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        am_pm_label = ttk.Label(main_frame, text="AM/PM:")
        am_pm_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.am_pm_combobox = ttk.Combobox(main_frame, textvariable=self.am_pm, values=("AM", "PM"), width=5)
        self.am_pm_combobox.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        
        set_alarm_button = ttk.Button(main_frame, text="Set Alarm", command=self.set_alarm)
        set_alarm_button.grid(row=1, columnspan=6, padx=5, pady=10)
        
    def set_alarm(self):
        alarm_time = self.hour.get() + ":" + self.minute.get() + " " + self.am_pm.get()
        try:
            time.strptime(alarm_time, "%I:%M %p")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid time in HH:MM AM/PM format")
            return
        
        current_time = time.strftime("%I:%M %p")
        while current_time != alarm_time:
            current_time = time.strftime("%I:%M %p")
            time.sleep(1)
        
        winsound.Beep(500, 1000)  # Beep sound
        messagebox.showinfo("Alarm", "Wake up!")
        
def main():
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
