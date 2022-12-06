import datetime
import requests
from CaseStudy2.models import News

def my_cron_job():
        # Get the max number of post from Hacker Newa
    url = "https://hacker-news.firebaseio.com/v0/maxitem.json"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    max_item = response.json()

    # Get the max number in the database
    last_item = News.objects.last()
    print(last_item)
    if last_item == None:
        for i in range(max_item-100,max_item):
            try:
                url = f"https://hacker-news.firebaseio.com/v0/item/{i}.json"
                payload = "{}"
                response = requests.request("GET", url, data=payload)
                response_text = response.json()
                # print(response_text)
                unixToDatetime = datetime.datetime.fromtimestamp(
                    response_text['time']
                )  # Unix Time
                new_post = News(
                    id=response_text["id"],
                    type=response_text["type"],
                    by=response_text["by"],
                    time=unixToDatetime,
                    text=response_text['text']
                    .replace("&amp;#x27", "'").replace("&lt;p&gt;", "")
                    .replace("&#x27;", "").replace("<p>", "")
                    .replace("&#x2F;", "/")
                )
                new_post.save()
            except Exception as e:
                print(e)
                print(f"I had an error with id {i}")
    else:
        # Get the news for this id
        for i in range(last_item.id,max_item):
            try:
                url = f"https://hacker-news.firebaseio.com/v0/item/{i}.json"
                payload = "{}"
                response = requests.request("GET", url, data=payload)
                response_text = response.json()
                # print(response_text)
                unixToDatetime = datetime.datetime.fromtimestamp(
                    response_text['time']
                )  # Unix Time
                new_post = News(
                    id=response_text["id"],
                    type=response_text["type"],
                    by=response_text["by"],
                    time=unixToDatetime,
                    text=response_text['text']
                    .replace("&amp;#x27", "'").replace("&lt;p&gt;", "")
                    .replace("&#x27;", "").replace("<p>", "")
                    .replace("&#x2F;", "/")
                )
                new_post.save()
            except Exception as e:
                print(e)
                print(f"I had an error with id {i}")

# End of loop and function