# Reference: https://blog.matthewurch.ca/?cat=8
# Date: 15.12.2015
# Description: Script watches MS Outlook and prints lines into the pyhton console, when an e-mail arrives.
# TODO: The script was in python 2.7. I added the parenthesis for print. In line 11 is a problem, but script runs when commented out
# 
#


import win32com.client
import pythoncom
 
class Handler_Class(object):
    def OnNewMailEx(self, receivedItemsIDs):
        for ID in receivedItemsIDs.split(","):
            # Microsoft.Office.Interop.Outlook _MailItem properties:
            # https://msdn.microsoft.com/en-us/library/microsoft.office.interop.outlook._mailitem_properties.aspx
            mailItem = outlook.Session.GetItemFromID(ID)
            print ("Subj: " + mailItem.Subject)
            # print ("Body: " + mailItem.Body.encode( 'ascii', 'ignore' ))
            print ("========")
         
outlook = win32com.client.DispatchWithEvents("Outlook.Application", Handler_Class)
pythoncom.PumpMessages()
