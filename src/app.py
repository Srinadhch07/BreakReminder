import time
import tkinter as tk

class BreakReminder:
    def __init__(self):
        self.running_status = True
        

    def setup(self):
        self.root.title("REMINDER FOR SRINADH !")
        self.root.state("zoomed")
        # Middling elements
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

    def display(self):
        """Starts the Tkinter event loop."""
        self.root.mainloop()

    def stop(self):
        """Stop the reminder loop and close the window."""
        self.running_status = False
        self.root.quit()  # Stop the event loop, effectively ending the program

    def start(self):
        """Create and display the reminder window."""
        self.setup()
        banner = tk.Label(self.root, text="Take Break Srinadh!", font=("Arial", 50, "bold italic"))
        banner.grid(row=0, column=0, pady=100)

        text = tk.Label(self.root, text="You have been working for 45 minutes", font=("Arial", 25, "bold"))
        text.grid(row=1, column=0, pady=50)

        ok_button = tk.Button(self.root, text="Okay", font=("Arial", 20, "bold"), fg='white', bg='green', command=self.root.destroy)
        ok_button.grid(row=2, column=0, pady=50)

        stop_button = tk.Button(self.root, text="Stop", font=("Arial", 20, "bold"), fg='white', bg='red', command=self.stop)
        stop_button.grid(row=3, column=0, pady=50)

        self.display()

    def run(self):
        """Runs the loop, showing reminders every 5 seconds until stopped."""
        while self.running_status:
            self.root = tk.Tk()  # Create a new root window for each reminder
            self.start()  # Show the reminder window
            time.sleep(5)  # Wait before showing the next reminder (still blocking the event loop)
            if not self.running_status:  # Check if stop was called
                break  # Break the loop if stop was called

# Instantiate and start the reminder system
instance = BreakReminder()
instance.run()
