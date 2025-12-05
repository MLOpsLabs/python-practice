import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#2b2b2b")
        self.root.resizable(False, False)
        
        # Colors
        self.DARK_BG = "#2b2b2b"
        self.BTN_BG = "#3b3b3b"
        self.BTN_FG = "#ffffff"
        self.OPERATOR_BG = "#ff9500"
        self.FUNCTION_BG = "#4a4a4a"
        self.DISPLAY_BG = "#1c1c1c"
        self.DISPLAY_FG = "#ffffff"
        self.HOVER_COLOR = "#4a4a4a"
        self.OPERATOR_HOVER = "#ffaa33"
        
        # Variables
        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.reset_next_input = False
        self.decimal_used = False
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Center window
        self.center_window()
        
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, height=150, bg=self.DISPLAY_BG)
        display_frame.pack(fill="x", padx=10, pady=(10, 5))
        display_frame.pack_propagate(False)
        
        # Previous expression
        self.previous_label = tk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 12),
            bg=self.DISPLAY_BG,
            fg="#888888",
            anchor="e",
            padx=20
        )
        self.previous_label.pack(fill="x", pady=(20, 0))
        
        # Current display
        self.display_label = tk.Label(
            display_frame,
            text="0",
            font=("Segoe UI", 36, "bold"),
            bg=self.DISPLAY_BG,
            fg=self.DISPLAY_FG,
            anchor="e",
            padx=20
        )
        self.display_label.pack(fill="both", expand=True)
        
        # Memory indicator
        self.memory_label = tk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 10),
            bg=self.DISPLAY_BG,
            fg="#888888",
            anchor="w",
            padx=20
        )
        self.memory_label.pack(fill="x", pady=(0, 10))
        
        # Memory variable
        self.memory = 0
        
    def create_buttons(self):
        # Button configuration
        buttons = [
            # Row 1
            [
                {"text": "MC", "command": self.memory_clear, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "MR", "command": self.memory_recall, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "M+", "command": self.memory_add, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "M-", "command": self.memory_subtract, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "⌫", "command": self.backspace, "bg": self.FUNCTION_BG, "colspan": 1}
            ],
            # Row 2
            [
                {"text": "%", "command": lambda: self.operation("%"), "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "CE", "command": self.clear_entry, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "C", "command": self.clear_all, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "÷", "command": lambda: self.operation("/"), "bg": self.OPERATOR_BG, "colspan": 1}
            ],
            # Row 3
            [
                {"text": "x²", "command": self.square, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "√x", "command": self.square_root, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "1/x", "command": self.reciprocal, "bg": self.FUNCTION_BG, "colspan": 1},
                {"text": "×", "command": lambda: self.operation("*"), "bg": self.OPERATOR_BG, "colspan": 1}
            ],
            # Row 4
            [
                {"text": "7", "command": lambda: self.add_digit("7"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "8", "command": lambda: self.add_digit("8"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "9", "command": lambda: self.add_digit("9"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "-", "command": lambda: self.operation("-"), "bg": self.OPERATOR_BG, "colspan": 1}
            ],
            # Row 5
            [
                {"text": "4", "command": lambda: self.add_digit("4"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "5", "command": lambda: self.add_digit("5"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "6", "command": lambda: self.add_digit("6"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "+", "command": lambda: self.operation("+"), "bg": self.OPERATOR_BG, "colspan": 1}
            ],
            # Row 6
            [
                {"text": "1", "command": lambda: self.add_digit("1"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "2", "command": lambda: self.add_digit("2"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "3", "command": lambda: self.add_digit("3"), "bg": self.BTN_BG, "colspan": 1},
                {"text": "=", "command": self.equals, "bg": self.OPERATOR_BG, "rowspan": 2}
            ],
            # Row 7
            [
                {"text": "+/-", "command": self.toggle_sign, "bg": self.BTN_BG, "colspan": 1},
                {"text": "0", "command": lambda: self.add_digit("0"), "bg": self.BTN_BG, "colspan": 1},
                {"text": ".", "command": self.add_decimal, "bg": self.BTN_BG, "colspan": 1}
            ]
        ]
        
        # Create button frame
        button_frame = tk.Frame(self.root, bg=self.DARK_BG)
        button_frame.pack(expand=True, fill="both", padx=10, pady=5)
        
        # Configure grid
        for i in range(7):
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)
        
        # Create buttons
        self.buttons = {}
        for row_idx, row in enumerate(buttons):
            col_idx = 0
            for btn_config in row:
                colspan = btn_config.get("colspan", 1)
                rowspan = btn_config.get("rowspan", 1)
                
                btn = tk.Button(
                    button_frame,
                    text=btn_config["text"],
                    font=("Segoe UI", 18, "bold"),
                    bg=btn_config["bg"],
                    fg=self.BTN_FG,
                    bd=0,
                    relief="flat",
                    activebackground=self.HOVER_COLOR if btn_config["bg"] != self.OPERATOR_BG else self.OPERATOR_HOVER,
                    activeforeground=self.BTN_FG,
                    cursor="hand2",
                    command=btn_config["command"]
                )
                
                # Bind hover effects
                btn.bind("<Enter>", lambda e, b=btn: self.on_enter(e, b))
                btn.bind("<Leave>", lambda e, b=btn: self.on_leave(e, b))
                
                btn.grid(
                    row=row_idx,
                    column=col_idx,
                    columnspan=colspan,
                    rowspan=rowspan,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )
                
                # Store reference for memory indicator
                if btn_config["text"] in ["MC", "MR", "M+", "M-"]:
                    self.buttons[btn_config["text"]] = btn
                
                col_idx += colspan
        
        # Update memory indicator
        self.update_memory_indicator()
    
    def on_enter(self, event, button):
        if button["bg"] == self.OPERATOR_BG:
            button.config(bg=self.OPERATOR_HOVER)
        else:
            button.config(bg=self.HOVER_COLOR)
    
    def on_leave(self, event, button):
        if button["text"] in ["MC", "MR", "M+", "M-"]:
            button.config(bg=self.FUNCTION_BG)
        elif button["text"] in ["÷", "×", "-", "+", "="]:
            button.config(bg=self.OPERATOR_BG)
        elif button["text"] in ["%", "CE", "C", "⌫", "x²", "√x", "1/x"]:
            button.config(bg=self.FUNCTION_BG)
        else:
            button.config(bg=self.BTN_BG)
    
    def update_display(self):
        # Format the display with thousands separator
        try:
            if "." in self.current_input:
                num = float(self.current_input)
                formatted = f"{num:,}"
            else:
                num = int(self.current_input)
                formatted = f"{num:,}"
        except:
            formatted = self.current_input
        
        # Limit display length
        if len(formatted) > 15:
            formatted = formatted[:15] + "..."
        
        self.display_label.config(text=formatted)
    
    def update_previous(self):
        if self.previous_input and self.operator:
            self.previous_label.config(text=f"{self.previous_input} {self.operator}")
        else:
            self.previous_label.config(text="")
    
    def update_memory_indicator(self):
        if self.memory != 0:
            self.memory_label.config(text=f"M: {self.memory}")
            # Enable memory buttons
            for key in ["MC", "MR", "M+", "M-"]:
                self.buttons[key].config(state="normal")
        else:
            self.memory_label.config(text="")
            # Disable MC and MR buttons when memory is 0
            self.buttons["MC"].config(state="disabled")
            self.buttons["MR"].config(state="disabled")
    
    def add_digit(self, digit):
        if self.reset_next_input:
            self.current_input = "0"
            self.reset_next_input = False
            self.decimal_used = False
        
        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        
        self.update_display()
    
    def add_decimal(self):
        if self.reset_next_input:
            self.current_input = "0"
            self.reset_next_input = False
        
        if not self.decimal_used:
            if "." not in self.current_input:
                self.current_input += "."
                self.decimal_used = True
                self.update_display()
    
    def toggle_sign(self):
        if self.current_input and self.current_input != "0":
            if self.current_input[0] == "-":
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display()
    
    def clear_entry(self):
        self.current_input = "0"
        self.decimal_used = False
        self.update_display()
    
    def clear_all(self):
        self.current_input = "0"
        self.previous_input = ""
        self.operator = ""
        self.decimal_used = False
        self.reset_next_input = False
        self.update_display()
        self.update_previous()
    
    def backspace(self):
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
            if "." not in self.current_input:
                self.decimal_used = False
        else:
            self.current_input = "0"
        
        self.update_display()
    
    def operation(self, op):
        if self.previous_input and not self.reset_next_input:
            self.equals()
        
        self.previous_input = self.current_input
        self.operator = {
            "+": "+",
            "-": "-",
            "*": "×",
            "/": "÷",
            "%": "%"
        }[op]
        self.reset_next_input = True
        self.update_previous()
    
    def equals(self):
        if not self.previous_input or not self.operator:
            return
        
        try:
            num1 = float(self.previous_input)
            num2 = float(self.current_input)
            
            if self.operator == "+":
                result = num1 + num2
            elif self.operator == "-":
                result = num1 - num2
            elif self.operator == "×":
                result = num1 * num2
            elif self.operator == "÷":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            elif self.operator == "%":
                result = num1 % num2
            
            # Format result
            if result.is_integer():
                result_str = str(int(result))
            else:
                result_str = f"{result:.10f}".rstrip('0').rstrip('.')
            
            self.current_input = result_str
            self.previous_input = ""
            self.operator = ""
            self.reset_next_input = True
            self.decimal_used = "." in result_str
            
            self.update_display()
            self.update_previous()
            
        except ZeroDivisionError:
            self.current_input = "Error"
            self.previous_input = ""
            self.operator = ""
            self.reset_next_input = True
            self.update_display()
            self.update_previous()
        except:
            self.current_input = "Error"
            self.update_display()
    
    # Scientific functions
    def square(self):
        try:
            num = float(self.current_input)
            result = num ** 2
            if result.is_integer():
                self.current_input = str(int(result))
            else:
                self.current_input = f"{result:.10f}".rstrip('0').rstrip('.')
            self.reset_next_input = True
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()
    
    def square_root(self):
        try:
            num = float(self.current_input)
            if num < 0:
                self.current_input = "Error"
            else:
                result = math.sqrt(num)
                if result.is_integer():
                    self.current_input = str(int(result))
                else:
                    self.current_input = f"{result:.10f}".rstrip('0').rstrip('.')
            self.reset_next_input = True
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()
    
    def reciprocal(self):
        try:
            num = float(self.current_input)
            if num == 0:
                self.current_input = "Error"
            else:
                result = 1 / num
                if result.is_integer():
                    self.current_input = str(int(result))
                else:
                    self.current_input = f"{result:.10f}".rstrip('0').rstrip('.')
            self.reset_next_input = True
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()
    
    # Memory functions
    def memory_clear(self):
        self.memory = 0
        self.update_memory_indicator()
    
    def memory_recall(self):
        if self.memory != 0:
            self.current_input = str(self.memory)
            self.reset_next_input = True
            self.update_display()
    
    def memory_add(self):
        try:
            num = float(self.current_input)
            self.memory += num
            self.update_memory_indicator()
        except:
            pass
    
    def memory_subtract(self):
        try:
            num = float(self.current_input)
            self.memory -= num
            self.update_memory_indicator()
        except:
            pass
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()