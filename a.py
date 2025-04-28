# Author: Ayush Singh
# GitHub: https://github.com/ayushsin2004


import tkinter as tk
from tkinter import ttk
import subprocess

def run_command():
    """Run the selected command in the background."""
    selected_mode = mode_var.get()

    if selected_mode == "Single Player":
        command = single_player_commands.get(single_player_var.get(), None)
    elif selected_mode == "Multiplayer":
        command = multiplayer_commands.get(multiplayer_var.get(), None)
    else:
        return
# Ayush Singh - https://github.com/ayushsin2004
    if command:
        subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def quit_app():
    """Terminate cmd.exe and exit the application."""
    subprocess.call("exit", shell=True)  # Force close Command Prompt
    root.quit()  # Exit Tkinter GUI

def update_dropdown():
    """Show the correct dropdown based on mode selection."""
    selected_mode = mode_var.get()
# Ayush Singh - https://github.com/ayushsin2004
    # Hide both dropdowns
    single_dropdown.pack_forget()
    multi_dropdown.pack_forget()

    # Show the relevant dropdown
    if selected_mode == "Single Player":
        single_dropdown.pack(pady=5)
    else:
        multi_dropdown.pack(pady=5)

# Commands for Single Player
single_player_commands = {
"Bike": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/bike.csv",
"Doom": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/doom.csv",
"Flappybird": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/flappybird.csv",
"Hillclimb": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/hillclimb.csv",
"Mariokart": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/mariokart.csv",
"Qwop": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/qwop.csv",
"Shoot": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/shoot.csv",# Ayush Singh - https://github.com/ayushsin2004
"Simon": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/simon.csv",
"Spaceinvaders": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/spaceinvaders.csv",
"Starfox": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/starfox.csv",
"Subwaysuffer": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/subwaysuffer.csv",
"Supermario": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/supermario.csv",
"Tetris": "python play.py -f 1 -l 1 -s 1 -r 1 -m single_player/tetris.csv"

    
}

# Commands for Multiplayer
multiplayer_commands = {
"Mortalkombat": "python play.py -f 1 -l 1 -s 2 -r 1 -m multi_player/mortalkombat.csv",
"Pacman": "python play.py -f 1 -l 1 -s 2 -r 1 -m multi_player/pacman.csv",# Ayush Singh - https://github.com/ayushsin2004
"Pong": "python play.py -f 1 -l 1 -s 2 -r 1 -m multi_player/pong.csv",
"Smashbros": "python play.py -f 1 -l 1 -s 2 -r 1 -m multi_player/smashbros.csv"
}

# Create main window
root = tk.Tk()
root.title("Game Mode Selector")
root.geometry("400x300")  # Increased height for Quit button
root.configure(bg="#2c3e50")  # Dark theme
# Ayush Singh - https://github.com/ayushsin2004
# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TCombobox", font=("Arial", 12), padding=5)

# Header Label
header_label = tk.Label(root, text="Select Game Mode", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
header_label.pack(pady=10)

# Variable to store selected mode
mode_var = tk.StringVar(value="Single Player")

# Frame for mode selection
frame = tk.Frame(root, bg="#2c3e50")
frame.pack()

# Radio Buttons for selecting mode
single_radio = tk.Radiobutton(frame, text="Single Player", variable=mode_var, value="Single Player", 
                              command=update_dropdown, font=("Arial", 12), bg="#2c3e50", 
                              fg="white", selectcolor="#34495e")
multi_radio = tk.Radiobutton(frame, text="Multiplayer", variable=mode_var, value="Multiplayer", 
                             command=update_dropdown, font=("Arial", 12), bg="#2c3e50", 
                             fg="white", selectcolor="#34495e")

single_radio.pack(side="left", padx=10)
multi_radio.pack(side="left", padx=10)
# Ayush Singh - https://github.com/ayushsin2004
# Dropdowns for selecting commands
single_player_var = tk.StringVar()
single_dropdown = ttk.Combobox(root, textvariable=single_player_var, values=list(single_player_commands.keys()), state="readonly")
single_dropdown.set("Select a Single Player Game")  # Placeholder text

multiplayer_var = tk.StringVar()
multi_dropdown = ttk.Combobox(root, textvariable=multiplayer_var, values=list(multiplayer_commands.keys()), state="readonly")
multi_dropdown.set("Select a Multiplayer Command")  # Placeholder text

# Run button
run_button = ttk.Button(root, text="Run Command", command=run_command)
run_button.pack(pady=10)

# Quit button to close the app and terminate cmd
quit_button = ttk.Button(root, text="Quit", command=quit_app, style="TButton")
quit_button.pack(pady=10)

# Initialize with Single Player dropdown visible
update_dropdown()

# Run the application
root.mainloop()


# ------------------------
# End of file
# Script built and maintained by Ayush Singh
# GitHub: https://github.com/ayushsin2004
# ------------------------