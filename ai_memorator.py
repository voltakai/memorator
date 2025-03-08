import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class AIMemoratorApp:
    def __init__(self, root):
        # Setup the root window
        self.root = root
        self.root.title("AI Memorator")
        self.root.geometry("380x390")  # Longer and slightly less wide
        self.root.resizable(True, True)
        self.root.configure(bg="#1e1e2e")
        self.root.minsize(380, 390)  # Set minimum size
        
        # Configure styles
        self.configure_styles()
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#1e1e2e")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            self.main_frame, 
            text="AI Model Memory Calculator", 
            font=("Segoe UI", 16, "bold"),
            fg="#fff",
            bg="#1e1e2e"
        )
        title_label.pack(pady=(0, 20))
        
        # Center container for inputs and result
        center_frame = tk.Frame(self.main_frame, bg="#1e1e2e")
        center_frame.pack(expand=True, fill=tk.BOTH)
        
        # Input frame
        input_frame = tk.Frame(center_frame, bg="#1e1e2e")
        input_frame.pack(fill=tk.X, pady=10)
        
        # Parameters input
        param_label = tk.Label(
            input_frame, 
            text="Model Parameters (billions):", 
            font=("Segoe UI", 11),
            fg="#fff",
            bg="#1e1e2e",
            anchor="center",
            justify=tk.CENTER
        )
        param_label.pack(fill=tk.X)
        
        self.param_entry = ttk.Entry(input_frame, width=10, style="TEntry", justify=tk.CENTER)
        self.param_entry.pack(pady=5, anchor=tk.CENTER)
        
        # Quantization input
        quant_label = tk.Label(
            input_frame, 
            text="Quantization Bits:", 
            font=("Segoe UI", 11),
            fg="#fff", 
            bg="#1e1e2e",
            anchor="center",
            justify=tk.CENTER
        )
        quant_label.pack(fill=tk.X, pady=(10, 0))
        
        self.quant_values = ["32", "16", "8", "4"]
        self.quant_var = tk.StringVar(value="8")  # Default to 8 bits
        self.quant_dropdown = ttk.Combobox(
            input_frame, 
            textvariable=self.quant_var,
            values=self.quant_values,
            width=8,
            style="TCombobox",
            justify=tk.CENTER
        )
        self.quant_dropdown.pack(pady=5, anchor=tk.CENTER)
        
        # Calculate button
        btn_frame = tk.Frame(center_frame, bg="#1e1e2e")
        btn_frame.pack(pady=15)
        
        calc_button = tk.Button(
            btn_frame,
            text="Calculate",
            font=("Segoe UI", 11),
            bg="#7289da",
            fg="#ffffff",
            activebackground="#5e73b9",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            borderwidth=0,
            cursor="hand2",
            command=self.calculate_memory
        )
        calc_button.pack()
        
        # Result display
        result_frame = tk.Frame(center_frame, bg="#1e1e2e", pady=10)
        result_frame.pack(fill=tk.X)
        
        self.result_var = tk.StringVar(value="0.0 GB")
        self.result_label = tk.Label(
            result_frame,
            textvariable=self.result_var,
            font=("Segoe UI", 18, "bold"),
            fg="#66ff99",
            bg="#1e1e2e"
        )
        self.result_label.pack(anchor=tk.CENTER)
        
        # Brand name in corner
        brand_label = tk.Label(
            self.root, 
            text="AI Memorator", 
            font=("Arial Rounded MT Bold", 8),
            fg="#aaaaaa",
            bg="#1e1e2e"
        )
        brand_label.place(relx=0.05, rely=0.93)  # Added more padding
        
        # Info button in top right - make it responsive with more padding
        info_icon = tk.Label(
            self.root, 
            text="ⓘ", 
            font=("Segoe UI", 14),
            fg="#aaaaaa",
            bg="#1e1e2e",
            cursor="hand2"
        )
        info_icon.place(relx=0.92, rely=0.05)  # Added more padding
        info_icon.bind("<Button-1>", self.show_about)
        
        # Window resize event binding
        self.root.bind("<Configure>", self.on_resize)
    
    def on_resize(self, event=None):
        # Keep elements responsive when window resizes
        self.root.update_idletasks()
    
    def configure_styles(self):
        # Configure ttk styles for better look
        style = ttk.Style()
        style.theme_use('clam')
        
        # Entry style
        style.configure(
            "TEntry",
            fieldbackground="#2d2d3f",
            foreground="#ffffff",
            insertcolor="#ffffff",
            borderwidth=0
        )
        
        # Combobox style
        style.configure(
            "TCombobox",
            fieldbackground="#2d2d3f",
            foreground="#ffffff",
            selectbackground="#7289da",
            selectforeground="#ffffff"
        )
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#2d2d3f")],
            selectbackground=[("readonly", "#7289da")],
            foreground=[("readonly", "#ffffff")]
        )
    
    def calculate_memory(self):
        try:
            # Get input values
            p = float(self.param_entry.get())
            q = int(self.quant_var.get())
            
            # Calculate memory
            m = (p * 4) / (32/q) * 1.2
            
            # Update result
            self.result_var.set(f"{m:.2f} GB")
            
        except ValueError:
            self.result_var.set("Invalid input")
    
    def show_about(self, event=None):
        # Create about window
        about_window = tk.Toplevel(self.root)
        about_window.title("About AI Memorator")
        about_window.geometry("400x350") 
        about_window.configure(bg="#1e1e2e")
        about_window.resizable(True, True)
        
        # Add content
        about_frame = tk.Frame(about_window, bg="#1e1e2e", padx=20, pady=20)
        about_frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.Label(
            about_frame,
            text="About AI Memorator",
            font=("Segoe UI", 14, "bold"),
            fg="#fff",
            bg="#1e1e2e"
        )
        title.pack(pady=(0, 15))
        
        formula_text = "Formula: M = (P × 4) / (32/Q) × 1.2"
        formula = tk.Label(
            about_frame,
            text=formula_text,
            font=("Segoe UI", 12),
            fg="#fff",
            bg="#1e1e2e",
            justify=tk.LEFT,
            wraplength=400
        )
        formula.pack(anchor=tk.W, pady=5, fill=tk.X)
        
        variables_text = """Variables:
• M - GPU memory required (in GB)
• P - Number of parameters in the model (billions)
• 4 - 4 bytes used for each parameter
• 32 - 32 bits in 4 bytes
• Q - Quantization bits (32, 16, 8, or 4 bits)
• 1.2 - 20% overhead for additional data in GPU memory"""
        
        variables = tk.Label(
            about_frame,
            text=variables_text,
            font=("Segoe UI", 11),
            fg="#fff",
            bg="#1e1e2e",
            justify=tk.LEFT,
            wraplength=400,
            pady=0  # Reduced padding
        )
        variables.pack(anchor=tk.W, pady=(5, 0), fill=tk.X)  # Reduced bottom padding
        
        # Contact at the bottom with more visible spacing
        contact_frame = tk.Frame(about_window, bg="#1e1e2e", pady=0)
        contact_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        contact = tk.Label(
            contact_frame,
            text="contact: voltakai@pm.me",
            font=("Segoe UI", 8),
            fg="#aaaaaa",
            bg="#1e1e2e"
        )
        contact.pack(side=tk.BOTTOM, pady=10)
        
        # Make the about window responsive
        about_window.bind("<Configure>", lambda e: formula.config(wraplength=about_window.winfo_width() - 60) or 
                                                variables.config(wraplength=about_window.winfo_width() - 60))

def main():
    root = tk.Tk()
    app = AIMemoratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
