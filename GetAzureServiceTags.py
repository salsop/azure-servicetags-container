# Azure Public
url = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519"
# Azure Government
#url = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=57063"
# Azure China
#url = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=57062"
# Azure Germany
#url = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=57064"

# Output directory for files
output_path = '/var/www/html'

RE_PATTERN = 'https:\\/\\/download\\.microsoft\\.com\\/download\\/[a-zA-Z0-9\\/\\-\\_\\.]+'

import requests
import json
import os
import re
from datetime import datetime

def get_azure_servicetags():
  '''
  Get Azure Service endpoint IP addresses
  '''
  regex = re.compile(RE_PATTERN)
  r = requests.get(url)
  article_text = r.text
  m = regex.findall(article_text)
  r = requests.get(m[0], stream=True)
  response = r.raw
  service_tags = json.load(response)

  for key in service_tags['values']:
    with open(f"{output_path}/{key['id']}.txt", 'w') as out_file:
      for item in key['properties']['addressPrefixes']:
        out_file.write("%s\n" % item)

def generate_webpage():
  '''
  Generate Webpage for List of Azure ServiceTags
  '''
  artifacts_files = os.listdir(output_path)
  artifacts_files.sort(reverse=True)
  main_page_content = '<html>\n<head>\n</head>\n<body>\n Generated date:<br>' + str(datetime.now()) + '<br><br>Generated list:<br>'
  for item in artifacts_files:
    print(item)
    main_page_content = main_page_content + '<a href="' + item + '">' + item + '</href>\n <br>'
  main_page_content += '</body></html>'
  with open(output_path + '/index.html','w') as out_file:
    out_file.write("%s" % main_page_content)

get_azure_servicetags()
generate_webpage()
