import tkinter as tk
import math

# Define the Calculator class
class Calculator:
    # Initialize the calculator
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("445x410")  # Set the size of the calculator window

        # StringVar to update and display the calculator's screen
        self.total = tk.StringVar()
        # Variables to store the first number, operation
        self.first_number = None
        self.operation = None
 
        # Entry widget for user input/output
        self.entry = tk.Entry(master, textvariable=self.total, font=("Helvetica", 20))
        self.entry.grid(row=0, column=0, columnspan=6, pady=6)
        self.history = []  # History list to keep track of past calculations
        self.constants = {"π": math.pi,"e": math.e}  # Constant dictionary

        # Method to create calculator buttons
        self.create_buttons() 

    def format_result(self, result):
        #Formats the result to display as an integer if it's a whole number, or as a float otherwise
        if result == int(result):
            return int(result)
        else:
            # Format as a float with a limited number of decimal places
            return round(result, 10)
    def create_buttons(self):
        # List of button labels arranged by rows
        button_list = [
            ['sin', 'cos', 'tan', 'arctan','arcsin','x^y'],     
            ['7', '8', '9', '/', 'log(x)','∛x'],
            ['4', '5', '6', '*', '1/x','arccos'],
            ['1', '2', '3', '-', 'x!','x√y'],
            ['0', '10^x', 'x^2', '+', '√x','x^ -1'],
            ['e^x', '%', '.','+/-','π','x^3'],
            ['e','DEL','AC','CH','History','='] 
   ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                # Create and place each button on the grid
                button = tk.Button(
                    self.master, text=button_text, width=5, height=3, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text),
                    bg="#e6e6e6", fg="#000000",
                    borderwidth=1, relief="solid"
                )
                button.grid(row=i + 1, column=j, sticky="nsew")

                # Mouse hover effects
                button.bind("<Enter>", lambda event, b=button: b.configure(bg="#d3d3d3"))
                button.bind("<Leave>", lambda event, b=button: b.configure(bg="#e6e6e6"))

            self.master.rowconfigure(i + 1, weight=1)
        for col in range(6):
            self.master.columnconfigure(col, weight=1)

    # Method to handle button click events
    def click(self, button_text):
        if button_text in ['+', '-', '*', '/', '%','x^y','x√y']:
            try:
                # Store the first number and operation, then reset for second number
                self.first_number = float(self.total.get())
                self.operation = button_text
                self.total.set("")
                self.second_number = None  # Reset second number
            except ValueError:
                self.total.set("Error")

        elif button_text == '=':
            try:
                a = self.first_number
                if self.second_number is None:
                    # Store the second number only the first time '=' is pressed
                    self.second_number = float(self.total.get())

                # Use the second number for the operation
                if self.operation == '+':
                    result = self.first_number + self.second_number
                elif self.operation == '-':
                    result = self.first_number - self.second_number
                elif self.operation == '*':
                    result = self.first_number * self.second_number
                elif self.operation == '/':
                    result = self.first_number / self.second_number
                elif self.operation == '%':
                    result = (self.first_number / 100) * self.second_number
                elif self.operation == 'x^y':
                    result = self.first_number ** self.second_number
                elif self.operation == 'x√y':
                    result = self.first_number ** (1 / self.second_number)

                self.first_number = result  # Update the first number with the result
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{a} {self.operation} {self.second_number} = {formatted_result}")
            except Exception as e:
                self.total.set("Error")

        elif button_text in self.constants:
            # Handle constant like π 
            self.total.set(self.constants[button_text])
        elif button_text == 'DEL':
            current_value = self.total.get()
            if len(current_value) > 1:
                # Remove the last character from the current value
                self.total.set(current_value[:-1])
            else:
                # If the entry is empty or has only one character, clear it
                self.total.set("")
        elif button_text == 'sin':
            try:
                # Retrieve the current value from the entry widget and store it in a throwaway variable '_'.
                _ = self.entry.get()
                 # Calculate the ... of the input. 
                result = math.sin(math.radians(float(self.entry.get())))
                # Format the result for display (e.g., reducing decimal places, handling large numbers).
                formatted_result = self.format_result(result)
                 # Set the formatted result to be displayed on the calculator's screen.
                self.total.set(formatted_result)
                 # Append the operation and its result to the history list for later viewing.
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'cos':
            try:
                _ = self.entry.get()
                result = math.cos(math.radians(float(self.entry.get())))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'x^ -1':
            try:
                _ = self.entry.get()
                result = 1 / float(self.entry.get())
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == '%':
            try:
                _ = self.entry.get()
                result = float(self.entry.get()) / 100
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.total.set(result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'tan':
            try:
                _ = self.entry.get()
                result = math.tan(math.radians(float(self.entry.get())))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'x^2':
            try: 
                _ = self.entry.get()
                result = float(self.entry.get()) ** 2
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'x^3':
            try: 
                _ = self.entry.get()
                result = float(self.entry.get()) ** 3
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'log(x)':
            try:
                _ = self.entry.get()
                # Using math.log10 to compute the logarithm with base 10
                result = math.log10(float(self.entry.get()))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == '1/x':
            try:
                _ = self.entry.get()
                result = 1 / float(self.entry.get())
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'x!':
            try:
                _ = self.entry.get()
                result = math.factorial(int(self.entry.get()))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == '10^x':
            try:
                _ = self.entry.get()
                result = 10 ** float(self.entry.get())
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == '√x':
            try:
                _ = self.entry.get()
                result = math.sqrt(float(self.entry.get()))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'e^x':
            try:
                _ = self.entry.get()
                result = math.exp(float(self.entry.get()))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'arcsin':
            try:
                _ = self.entry.get()
                result = math.degrees(math.asin(float(self.entry.get())))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")

        elif button_text == 'arccos':
            try:
                _ = self.entry.get()
                result = math.degrees(math.acos(float(self.entry.get())))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == '.':
            current = self.total.get()
            if '.' not in current:
                self.total.set(current + '.')
        elif button_text == '+/-':
            current_value = self.total.get()
            if current_value:  # Check if there is a current value
                if current_value.startswith('-'):
                    self.total.set(current_value[1:])  # Remove negative sign
                else:
                    self.total.set('-' + current_value)  # Add negative sign
        elif button_text == 'History':
            self.show_history()
        elif button_text == 'CH':
            self.clear_history()
        elif button_text == 'AC':
            self.total.set("")        # Clear the display
            self.first_number = None  # Reset the stored first number
            self.operation = None     # Reset the stored operation
            self.second_number = None # Reset the stored second number
        elif button_text == 'arctan':
            try:
                _ = self.entry.get()
                result = math.atan(int(self.entry.get()))
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"{button_text}({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == '∛x':
            try:
                _ = self.entry.get()
                result = float(self.entry.get()) ** (1/3)  # Calculate the cube root
                formatted_result = self.format_result(result)
                self.total.set(formatted_result)
                self.history.append(f"cube root({_}) = {formatted_result}")
            except:
                self.total.set("Error")
        elif button_text == 'x√y':
            try:
                # Store the radicand (x) and set the operation
                self.first_number = float(self.total.get())
                self.operation = 'x√y'
                self.total.set("")
            except ValueError:
                self.total.set("Error")
        else:
            self.total.set(self.entry.get() + button_text)

    # Method to display calculation history
    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Calculation History")
        history_text = tk.Text(history_window, height=10, width=40)
        history_text.pack()
        history_text.insert(tk.END, "\n".join(self.history))
        # Disable editing of history text
        history_text.config(state=tk.DISABLED)

    # Method to clear the calculation history
    def clear_history(self):
        self.history = []  # Reset the history list

# Main block to run the application
if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()


