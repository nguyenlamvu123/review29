import requests

# url = "http://127.0.0.1:8000/save-review/"
#
# payload = {'video_url': 'https://www.youtube.com/watch?v=uj1qdsfJ2-U',
# 'aff_link_1': 'https://www.youtube.com/watch?v=PCSaqek18PI&list=RDPCSaqek18PI&start_radio=1&pp=oAcB',
# 'aff_link_2': 'https://www.youtube.com/watch?v=1ORDCsC0_L4&list=RD1ORDCsC0_L4&start_radio=1&pp=oAcB',
# 'aff_link_4': 'https://www.youtube.com/watch?v=qoqjxg7HXiY&list=RDqoqjxg7HXiY&start_radio=1&pp=oAcB'}
# files=[
#
# ]
# headers = {
#   'Key': 'X-CSRFToken',
#   'Value': '{{csrftoken}}'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# url = "http://127.0.0.1:8000/"
url = "http://127.0.0.1:8000/review-by-url/?video_url=https://www.youtube.com/watch?v=uj1qdsfJ2-U"
# url = "http://127.0.0.1:8000/reviews/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)