#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: --
#    Goals: Learn clr module to work with windows forms
#      Ref: --
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: --

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
