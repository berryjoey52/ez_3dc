from tkinter import Tk, Label, Entry, Button, Text, Scrollbar

tdcq1 = "1.   Was the rep able to answer all your questions?"
tdcq2 = "2.   Was he/she able to show you samples of our products and leave you with a price?"
tdcq3 = "3.   Was it a printed proposal or was it emailed after? Did it show discounts and financing options?"
tdcq4 = "4.   If you don't mind me asking, could you please tell me what stood out for you: Was it the features, colors, style options?"
tdcq5 = "5.   Is there any additional information that would help you in your decision-making process?"
tdcq6 = "6.   One last question, when did you discuss with your rep would be a good time to follow up with you?"

# Print red text method
def print_red(text):
    return f"\033[31m{text}\033[0m"

# This will show the output.
def submit_form():
    rep_name = rep_name_entry.get()
    opp = opp_entry.get()
    customer = opp.split(' -')[0]
    date = date_entry.get()
    q1 = q1_entry.get()
    q2 = q2_entry.get()
    q3 = q3_entry.get()
    q4 = q4_entry.get()
    q5 = q5_entry.get()
    q6 = q6_entry.get()

    output_text = opp + "\n" + "Appointment Date/Time: " + date + "\n\n"
    output_text += "Hi " + rep_name + ", I completed a 3 day Call for " + customer + ". Follow-up notes are below.\n\n"
    output_text += "     " + tdcq1 + "\n" + print_red(q1) + "\n"
    output_text += "     " + tdcq2 + "\n" + print_red(q2) + "\n"
    output_text += "     " + tdcq3 + "\n" + print_red(q3) + "\n"
    output_text += "     " + tdcq4 + "\n" + print_red(q4) + "\n"
    output_text += "     " + tdcq5 + "\n" + print_red(q5) + "\n"
    output_text += "     " + tdcq6 + "\n" + print_red(q6) + "\n\n"
    output_text += "I hope the customer's feedback is helpful in closing this deal when you do your follow-up!"

    output_text_widget.delete(1.0, "end")  # Clear previous content
    output_text_widget.insert("end", output_text)

def clear_form():
    rep_name_entry.delete(0, "end")
    opp_entry.delete(0, "end")
    date_entry.delete(0, "end")
    q1_entry.delete(0, "end")
    q2_entry.delete(0, "end")
    q3_entry.delete(0, "end")
    q4_entry.delete(0, "end")
    q5_entry.delete(0, "end")
    q6_entry.delete(0, "end")
    output_text_widget.delete(1.0, "end")  # Clear the output as well

# Create the GUI
root = Tk()
root.title(" EZ 3 Day Call")

# rep name Label and Entry
rep_name_label = Label(root, text="Enter the rep's first name:")
rep_name_label.pack(anchor='w')
rep_name_entry = Entry(root, width=50)
rep_name_entry.pack(anchor='w')

# Opportunity Label and Entry
opp_label = Label(root, text="Please copy and paste the opportunity name")
opp_label.pack(anchor='w')
opp_entry = Entry(root, width=50)
opp_entry.pack(anchor='w')

# Date Label and Entry
date_label=Label(root, text="Please enter the appointment date:")
date_label.pack(anchor='w')
date_entry = Entry(root, width=50)
date_entry.pack(anchor='w')

# Was the rep able to answer all your questions?
q1_label = Label(root, text=tdcq1)
q1_label.pack(anchor='w')
q1_entry = Entry(root, width=50)
q1_entry.pack(anchor='w')

# Was he/she able to show you samples of our products and leave you with a price?
q2_label = Label(root, text=tdcq2)
q2_label.pack(anchor='w')
q2_entry = Entry(root, width=50)
q2_entry.pack(anchor='w')

# Was it a printed proposal or was it emailed after? Did it show discounts and financing options?
q3_label = Label(root, text=tdcq3)
q3_label.pack(anchor='w')
q3_entry = Entry(root, width=50)
q3_entry.pack(anchor='w')

# If you don't mind me asking, could you please tell me what stood out for you: Was it the features, colors, style options?
q4_label = Label(root, text=tdcq4)
q4_label.pack(anchor='w')
q4_entry = Entry(root, width=50)
q4_entry.pack(anchor='w')

# Is there any additional information that would help you in your decision-making process?
q5_label = Label(root, text=tdcq5)
q5_label.pack(anchor='w')
q5_entry = Entry(root, width=50)
q5_entry.pack(anchor='w')

# One last question, when did you discuss with your rep would be a good time to follow up with you?
q6_label = Label(root, text=tdcq6)
q6_label.pack(anchor='w')
q6_entry = Entry(root, width=50)
q6_entry.pack(anchor='w')

# Submit Button
submit_button = Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Clear Form Button
clear_form_button = Button(root, text="Clear Form", command=clear_form)
clear_form_button.pack()

# Output Text Widget
output_text_widget = Text(root, width=80, height=15, wrap="word")
output_text_widget.pack()

# Scrollbar for the Output Text Widget
scrollbar = Scrollbar(root, command=output_text_widget.yview)
scrollbar.pack(side="right", fill="y")
output_text_widget.config(yscrollcommand=scrollbar.set)

# Define the "red" tag with red color configuration
output_text_widget.tag_configure("red", foreground="red")

root.mainloop()