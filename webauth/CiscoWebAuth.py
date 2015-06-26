"""Script that establishes a session in a network managed by Cisco Web Authentication.

This script requests for re-establishing a session in a network managed by Cisco Web 
Authentication.

Copyright 2013 Dario B. darizotas at gmail dot com
This software is licensed under a new BSD License. 
Unported License. http://opensource.org/licenses/BSD-3-Clause
"""

import httplib, urllib, socket
import sys
import re
class CiscoWebAuthCrawler:
  """Class responsible for parsing responses regarding messages from Cisco Web Authentication.
  
  Particularly it parses the response from "login.html".
  """

  def isConnected(self, html):
    """Returns true whether it is already established a session in the Cisco Web Authentication.
    
    Particularly it parses the title tag within the response from "login.html" 
    """
    # Parses for <title>Logged in</title>
    match = re.search('<title>Logged In</title>', html, re.I)
    return match

  def isDisconnected(self, html):
    """Returns true whether the session was eneded successfully.
    
    Particularly it parses the title tag within the response from "logout.html" 
    """
    # Parses for <title>Web Authentication</title>
    match = re.search('<title>Web Authentication</title>', html, re.I)
    return match
    
  def getMessage(self, html, flag):
    """Returns the message contained by the given flag (err, info) if enabled (value=1)."""
    pattern = 'NAME="' + flag + '_flag"\s+(?:\w+="\d+"\s+)*VALUE="1"'
    match = re.search(pattern, html, re.I)
    if match:
      msgPattern = 'NAME="' + flag + '_msg"\s+(?:\w+="\d+"\s+)*VALUE="([\w\s,\.]+)"'
      msgMatch = re.search(msgPattern, html, re.I)
      if msgMatch:
        return flag + ': ' + msgMatch.group(1)  
      else:
        return flag
    else:
      return ''