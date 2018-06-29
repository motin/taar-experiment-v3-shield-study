import glob
import os

for path in glob.glob("./shield-integrated-addon/addons/taar-study/addon/webextension/popup/locales/*"):
  try:
    with open(path+"/raw.txt") as f:
      raw = f.read()
    header, body, buttons = raw.split("]]]\n\n")[1].split("\n---\n")
    close, browse = buttons.split(",")
    html = """
    <!DOCTYPE HTML>

    <html>
      <head>
      <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link  rel="stylesheet" type="text/css" href="../../popup.css">
      </head>
      <body>
        <div id="topbar"></div>
        <div id="topsection">
          <div id="picture">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">   <path fill="context-fill" d="M14.5 8c-.971 0-1 1-1.75 1a.765.765 0 0 1-.75-.75V5a1 1 0 0 0-1-1H7.75A.765.765 0 0 1 7 3.25c0-.75 1-.779 1-1.75C8 .635 7.1 0 6 0S4 .635 4 1.5c0 .971 1 1 1 1.75a.765.765 0 0 1-.75.75H1a1 1 0 0 0-1 1v2.25A.765.765 0 0 0 .75 8c.75 0 .779-1 1.75-1C3.365 7 4 7.9 4 9s-.635 2-1.5 2c-.971 0-1-1-1.75-1a.765.765 0 0 0-.75.75V15a1 1 0 0 0 1 1h3.25a.765.765 0 0 0 .75-.75c0-.75-1-.779-1-1.75 0-.865.9-1.5 2-1.5s2 .635 2 1.5c0 .971-1 1-1 1.75a.765.765 0 0 0 .75.75H11a1 1 0 0 0 1-1v-3.25a.765.765 0 0 1 .75-.75c.75 0 .779 1 1.75 1 .865 0 1.5-.9 1.5-2s-.635-2-1.5-2z"></path> </svg>
          </div>
          <div id="textsection">
            <div id="messagesection">
              <h1 id="header">{}</h1>
              <p>{}</p>
            </div>
          </div>
        </div>
        
        <div id="bottomsection">
          <div id="button-container">
                  <button id="close-button" class="button-style">{}</button>

            <button id="browse-addons-button" class="button-style">{}</button>
          </div>
        </div>
       <script src="../../popup.js"></script> 
      </body>
    </html>
    """.format(header, body, close, browse)

    with open(path + "/popup.html", "w") as f:
        f.write(html)

  except:
    print "error for ", path



