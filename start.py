import requests
import csv
import time

request_url = 'https://leetcode.com/graphql'


def get_data(slug):
    headers = {
      'authority': 'leetcode.com',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
      'x-newrelic-id': 'UAQDVFVRGwEAXVlbBAg=',
      'dnt': '1',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
      'content-type': 'application/json',
      'accept': '*/*',
      'x-csrftoken': 'voLyNNl6YFQZQpDpAPqS2Qd1GbJe5YlrOuCiqMXjyiJ7TMrjGp7yS3wb29Lj8gRB',
      'sec-ch-ua-platform': '"macOS"',
      'origin': 'https://leetcode.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': f'https://leetcode.com/problems/{slug}/',
      'accept-language': 'en-CN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
      'cookie': 'csrftoken=voLyNNl6YFQZQpDpAPqS2Qd1GbJe5YlrOuCiqMXjyiJ7TMrjGp7yS3wb29Lj8gRB; messages="47ea2716b9a5fd18bea67274f5b6e8f0aad52691$[[\\"__json_message\\"\\0540\\05425\\054\\"Successfully signed in as bbbbb8bbbbb.\\"]]"; NEW_PROBLEMLIST_PAGE=1; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzU5NjIwMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNmODZhM2IyMjhjMDg2MzdkMDUwNzYyNDdkYzk1Mjc5NzZiODk1ZjkiLCJpZCI6MzU5NjIwMywiZW1haWwiOiJiYmJiYjhiYmJiYkBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImJiYmJiOGJiYmJiIiwidXNlcl9zbHVnIjoiYmJiYmI4YmJiYmIiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYmJiYmI4YmJiYmIvYXZhdGFyXzE2MDU2NjU5MjQucG5nIiwicmVmcmVzaGVkX2F0IjoxNjQ2NzMzNTc1LCJpcCI6IjI0MDQ6NDQwMjoxN2RhOjMwMDA6ZDliYjo1MGMwOjQ3MzQ6YTI2YyIsImlkZW50aXR5IjoiMDgzN2RjYzQyY2I3MTUzOWRlZjU5MjIyMzk2MTc0YjIiLCJzZXNzaW9uX2lkIjoxODkwODgyOCwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.0-FNODoEPFaEN6APb4FcTnJ0apEN1fnXDDPwCIq1n4E; c_a_u="YmJiYmI4YmJiYmI=:1nRv5i:Q51i-oddkv3RT0ejMW0KRi_XRWo"',
      'sec-gpc': '1',
  }
    query = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    isPaidOnly
    difficulty
    likes
    dislikes
    isLiked
    categoryTitle
    topicTags {
      name
    }
    companyTagStats
    stats
  }
}
"""
    variables = {"titleSlug": slug}
    response = requests.post(request_url, json={'query': query,'variables':variables},headers=headers)

    return response.text

def loop_csv():
    with open('leetcode.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        for row in reader:
            slug = (row[1].split('/')[-1])
            write_to_file(get_data(slug))
            time.sleep(5)

def write_to_file(data):
  with open("out.json", "a") as myfile:
    myfile.write(data+'\n')


loop_csv()
