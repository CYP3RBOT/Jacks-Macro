import tkinter
from dataclasses import dataclass
import customtkinter  # <- import the CustomTkinter module
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
root_tk.geometry("400x400")
root_tk.title("Jacks Macro")
x_padding = 10
y_padding = 5

from jacks_data import do_gj
from jacks_data import do_hj
from jacks_data import do_dj

################################################################################################

jack_type_label = customtkinter.CTkLabel(master=root_tk, text="Jack Type", width=120, height=25, fg_color=("black"), corner_radius=8)
jack_type_label.pack(pady=y_padding, padx=x_padding)

jacks_var = tkinter.IntVar(value=1)

grammar_jacks_radio = customtkinter.CTkRadioButton(master=root_tk, text="Grammar Jacks", variable=jacks_var, value=1)
grammar_jacks_radio.pack(pady=y_padding, padx=x_padding)

hell_jacks_radio = customtkinter.CTkRadioButton(master=root_tk, text="Hell Jacks", variable=jacks_var, value=2)
hell_jacks_radio.pack(pady=y_padding, padx=x_padding)

death_jacks_radio = customtkinter.CTkRadioButton(master=root_tk, text="Death Jacks", variable=jacks_var, value=3)
death_jacks_radio.pack(pady=y_padding, padx=x_padding)

################################################################################################

jack_amount_label = customtkinter.CTkLabel(master=root_tk, text="Amount of Jacks", width=120, height=25, fg_color=("black"), corner_radius=8)
jack_amount_label.pack(pady=y_padding, padx=x_padding)

jack_amount_entry = customtkinter.CTkEntry(master=root_tk, placeholder_text="Amount")
jack_amount_entry.pack(pady=y_padding, padx=x_padding)

################################################################################################

start_from_label = customtkinter.CTkLabel(master=root_tk, text="Start From", width=120, height=25, fg_color=("black"), corner_radius=8)
start_from_label.pack(pady=y_padding, padx=x_padding)

start_from_entry = customtkinter.CTkEntry(master=root_tk, placeholder_text="Amount")
start_from_entry.pack(pady=y_padding, padx=x_padding)

# < ---------- >

@dataclass
class Checkbox:
    root: object

    def __post_init__(self):
        self.var = tkinter.StringVar()
        self.enabled_check = customtkinter.CTkCheckBox(master=self.root, text="Enabled", variable=self.var, offvalue="disabled", onvalue="enabled")
        self.enabled_check.pack(padx=20, pady=5)

enabled = Checkbox(root_tk)

################################################################################################

def start():
    if not jack_amount_entry.get().isnumeric():
        print("Please enter a numerical value for Jack Amount")
        return
    if enabled.enabled_check.get() == "enabled":
        isStartingFrom = True
    else:
        isStartingFrom = False
    JACK_AMOUNT = int(jack_amount_entry.get())

    if jacks_var.get() == 1:
        do_gj(JACK_AMOUNT+1, isStartingFrom, int(start_from_entry.get()))
    elif jacks_var.get() == 2:
        do_hj(JACK_AMOUNT+1, isStartingFrom, int(start_from_entry.get()))
    elif jacks_var.get() == 3:
        do_dj(JACK_AMOUNT+1, isStartingFrom, int(start_from_entry.get()))

def stop():
    root_tk.quit()

start_button = customtkinter.CTkButton(master=root_tk, text="Start", width=120, height=25, command=start)
start_button.pack(pady=y_padding, padx=x_padding)

stop_button = customtkinter.CTkButton(master=root_tk, text="Stop", width=120, height=25, command=stop)
stop_button.pack(pady=y_padding, padx=x_padding)

root_tk.mainloop()