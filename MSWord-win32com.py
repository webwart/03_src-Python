#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Deal with MS-Word documents 
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: --
#  ------------------------------------




# Reference: The internet
# Description: The scripts creates a MS Word file and writes text to it. User needs to save file.
# Date: 15.12.2015
# TODO: Script is okay. I can try it with MS-Excel see internet. 
# >NEXT: http://etienned.github.io/, and 
#		https://python-docx.readthedocs.org/en/latest/
#       http://lxml.de/tutorial.html


import win32com.client
 
wordapp = win32com.client.Dispatch("Word.Application") # Create new Word Object
wordapp.Visible = 0 # Word Application should`t be visible
worddoc = wordapp.Documents.Add() # Create new Document Object
worddoc.PageSetup.Orientation = 1 # Make some Setup to the Document:
worddoc.PageSetup.LeftMargin = 20
worddoc.PageSetup.TopMargin = 20
worddoc.PageSetup.BottomMargin = 20
worddoc.PageSetup.RightMargin = 20
worddoc.Content.Font.Size = 11
worddoc.Content.Paragraphs.TabStops.Add (100)
worddoc.Content.Text = "Hello, I am a text!"
worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Application
