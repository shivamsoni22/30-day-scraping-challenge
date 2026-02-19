import jmespath
from curl_cffi import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://preisportal.pique-ferry.de',
    'priority': 'u=1, i',
    'referer': 'https://preisportal.pique-ferry.de/?locale=en',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6Ikt4NEVtMHpEZTNXZUxTbkhKSlNtTmc9PSIsInZhbHVlIjoibjBIempva25KVUVibVJNY1B3eTFVRjNMZ1J0T2U0VitIZldZd05VSDdLYUNETktaYk8wVGdlaVhqZFlQRmJHWUtnRG1PSnJxS0FpcUlWRThPTWdBVGRTdFJGbnlKUW91Z0dMNE4wYVc3KzlWem8wVVA0dDFFYXVHMUFvYzBacy8iLCJtYWMiOiIzOTE4NGQ3M2M5MzIwZDgwMjBlOGI2OTI1M2YxNjY0YmJjNDkzZGFiNWJkNTY3YzdlYWY5NWVlNmJjNDViNDJlIiwidGFnIjoiIn0=',
    'cookie': '_ga=GA1.1.1778200087.1771476839; _ga_EH638XP6NL=GS2.1.s1771476838$o1$g1$t1771477416$j18$l0$h0; XSRF-TOKEN=eyJpdiI6Ikt4NEVtMHpEZTNXZUxTbkhKSlNtTmc9PSIsInZhbHVlIjoibjBIempva25KVUVibVJNY1B3eTFVRjNMZ1J0T2U0VitIZldZd05VSDdLYUNETktaYk8wVGdlaVhqZFlQRmJHWUtnRG1PSnJxS0FpcUlWRThPTWdBVGRTdFJGbnlKUW91Z0dMNE4wYVc3KzlWem8wVVA0dDFFYXVHMUFvYzBacy8iLCJtYWMiOiIzOTE4NGQ3M2M5MzIwZDgwMjBlOGI2OTI1M2YxNjY0YmJjNDkzZGFiNWJkNTY3YzdlYWY5NWVlNmJjNDViNDJlIiwidGFnIjoiIn0%3D; preisportal_session=eyJpdiI6InQ2QXJycGlXZks2bWVxWFBNTWxab1E9PSIsInZhbHVlIjoiaTB2dlp6bmI4WFlLNmtkQ2xLU2x3eXpyaU5JczlTZkcvT3JvL0xab2F5TFZ4dHNLRCtURmdjeVJ0Z1VTZzF0NndSbWVlcWpWaXQ4SkNJSlZhdVZ2VWYxQk9IQ0ZSaFBpYnFhdGY3STJDTXgwSWZmWjlVMVVaODdwalF4WlpYMk4iLCJtYWMiOiI0ZDVhOWJjMWVmMjNkOWZiNDkxZjk1N2VjODNlZmE3NDEzMmQyYzBiYjFhZjcxOWFjNTdmNWMwNTZkMDMxNmQ1IiwidGFnIjoiIn0%3D',
}

json_data = {
    'harbour_from_id': 235,
    'harbour_to_id': 234,
    'date': '2026-02-17T18:30:00.000Z',
    'length': '18',
    'powerPlug': False,
    'secondDriver': False,
    'empty': False,
}

url = 'https://preisportal.pique-ferry.de/api/query'
def make_request(i):
   try:
       r = requests.post(
           url,
           # params=params,
           headers=headers,
           # cookies=cookies,
           json= json_data ,
           impersonate="chrome120",
           timeout=200
       )
       json = r.json()
       print(r.status_code)
       if '5071' in r.text and '267' in r.text :
           res =  'good response'
           return f"Request {i}   : {res}   "
       else:
           return f"Request {i}  No goods_name"
   except Exception as e:
       return f"Request {i}  Error: {e}"
if __name__ == "__main__":
   num_requests = 5000
   max_workers = 500
   results = []
   with ThreadPoolExecutor(max_workers=max_workers) as executor:
       futures = [executor.submit(make_request, i) for i in range(1, num_requests + 1)]
       for future in as_completed(futures):
           results.append(future.result())
           print(future.result())
