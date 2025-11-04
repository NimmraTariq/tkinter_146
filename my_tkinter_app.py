import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Application for Predicting Preferred Study Program")
root.geometry("500x600")
root.configure(bg="#F5F5F5")

# Title label
title_label = tk.Label(
    root,
    text="Application for Predicting Preferred Study Program",
    font=("Arial", 14, "bold"),
    bg="#F5F5F5"
)
title_label.pack(pady=20)

# Frame for input fields
input_frame = tk.Frame(root, bg="#F5F5F5")
input_frame.pack(pady=10)

# Create 10 input fields for subject scores
entries = []
for i in range(10):
    label = tk.Label(input_frame, text=f"Subject {i+1} Score:", bg="#F5F5F5", font=("Arial", 11))
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(input_frame, width=25)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Function for prediction
def show_prediction():
    result_label.config(text="Predicted Study Program: Information Technology")

# Prediction button
predict_button = tk.Button(
    root,
    text="Show Prediction Result",
    command=show_prediction,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    width=25
)
predict_button.pack(pady=20)

# Label to display result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#F5F5F5",
    fg="blue"
)
result_label.pack(pady=10)

# Run GUI
root.mainloop()
