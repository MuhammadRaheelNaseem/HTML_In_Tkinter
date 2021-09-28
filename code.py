# first install library
# if you linux user use this ---> pip3 install tkhtmltview 
# else window user use this  ---> py -m pip install tkhtmlview
# than import this all things like this
from tkinter import *
from tkhtmlview import *
# initialize Tk method
gui=Tk()
# add title
gui.title("Html")
# now add html script 
html_text="""
<h3 style="color:gold2: background-color:black: text-align:center">
<b>HTML Text GUI</b>
</h3>
<p style="text-align:left;">
<b>tkhtmlview</b> is a <i>collection of</i> <u>tkinter widgets</u>
whose text can be set in HTML format.<br>
<b>Heading Tags</b>
<ol type='1'>
<li>h1</h1>
<li>h2</h1>
<li>h3</h1>
<li>h4</h1>
</ol>
<p>
"""
# then pack html in a label
label = HTMLLabel(gui,html=html_text)
label.pack(pady=15,padx=15,fill=BOTH)
# then write mainloop
gui.mainloop()
