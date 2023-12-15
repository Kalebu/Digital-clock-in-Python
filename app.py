from time import strftime
from tkinter import Label, Tk, Button

# ======= Configuring window =========
window = Tk()
window.title("")
window.geometry("250x120")
window.resizable(False, False)  # =====setting a fixed window size =======

clock_label = Label(
    window, bg="black", fg="cyan", font=("Arial", 18, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)

format_24hour = False  # Set to True for 24-hour format, False for 12-hour format


def toggle_format():
    global format_24hour
    format_24hour = not format_24hour
    update_label()


toggle_button = Button(
    window,
    text="Toggle Format",
    font=("Arial", 12),
    relief="flat",
    command=toggle_format,
)
toggle_button.place(x=70, y=80)


def update_label():
    """
    This function will update the clock

    every 80 milliseconds
    """
    current_time_12hr = strftime("%I:%M:%S %p\n%d-%m-%Y ") if not format_24hour else ""
    current_time_24hr = strftime("%H:%M:%S\n%d-%m-%Y ") if format_24hour else ""

    clock_label.configure(text=current_time_12hr + current_time_24hr)

    # Change background color based on the time of day
    current_hour = int(strftime("%H"))
    if 6 <= current_hour < 12:
        window.configure(bg="yellow")  # Morning
    elif 12 <= current_hour < 18:
        window.configure(bg="orange")  # Afternoon
    else:
        window.configure(bg="blue")  # Evening/Night

    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()

