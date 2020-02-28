# Add a reference to the required .NET assembly
# This only need be done once per application
import clr
clr.AddReference("System.Windows.Forms")

# Then import symbols from the assembly, as if from a Python module
from System.Windows.Forms import Application, Form

# Then use the imported symbols as though they were native Python types
form = Form()
form.Text = "Hello World"
Application.Run(form)
