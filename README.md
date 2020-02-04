# Python Web and Image Scraper
> This scraper is built in Python3 and uses Beautiful Soup to parse and scrape the webpages.

[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

It scrapes bing.com for either text or images.

![](header.png)


## Usage example

```python3 scraper.py
Choose one of the following Scraper 
 1.Web Scraper 
 2.Image Scraper
 
 1
 Anirudh Tulasiram - Bengaluru, Karnataka, India | Professional …
https://in.linkedin.com/in/anirudhtulasiram
Summary :  View Anirudh Tulasiram’s profile on LinkedIn, the world's largest professional community. Anirudh has 5 jobs listed on their profile. See the complete profile on LinkedIn and discover Anirudh’s connections and jobs at similar companies.
TAdityaAnirudh (Aditya Anirudh Tulasi) · GitHub
https://github.com/TAdityaAnirudh
Summary :  TAdityaAnirudh has 7 repositories available. Follow their code on GitHub.
Anirudh Tulasi - Quora
https://www.quora.com/profile/Anirudh-Tulasi
Summary :  Anirudh Tulasi, Fantasy > Reality. As per a report by market research firm Strategy Analytics, though Samsung would begin 2020 as the leader in 5G smartphone, Apple would take the lead in the 5G race by the end of next year.. The report says that the South Korean tech giant would rely majorly on the cheaper Galaxy A90G before launching the 5G versions of Galaxy S11, S11+ and S11e.With all these 5G …
TAdityaAnirudh (Aditya Anirudh Tulasi) / Repositories · GitHub
https://github.com/TAdityaAnirudh?tab=repositories
Summary :  TAdityaAnirudh has 7 repositories available. Follow their code on GitHub.
TAdityaAnirudh (Aditya Anirudh Tulasi) / Followers · GitHub
https://github.com/TAdityaAnirudh?tab=followers
Summary :  Hide content and notifications from this user ...
Anirudh Tulasiram - Product Manager - The Fuller Life | LinkedIn
https://in.linkedin.com/in/anirudh-tulasiram-01b17930
Summary :  View Anirudh Tulasiram’s profile on LinkedIn, the world's largest professional community. Anirudh has 5 jobs listed on their profile. See the complete profile on LinkedIn and discover Anirudh’s connections and jobs at similar companies.
Tulasi Aditya Anirudh Aditya | Facebook
https://www.facebook.com/tulasiadityaanirudh.aditya
Summary :  Tulasi Aditya Anirudh Aditya is on Facebook. Join Facebook to connect with Tulasi Aditya Anirudh Aditya and others you may know. Facebook gives people the power to share and makes the world more open...
Aditya Anirudh Tulasi - Software Engineer 2 - Microsoft | LinkedIn
https://www.linkedin.com/in/tadityaanirudh
Summary :  View Aditya Anirudh Tulasi’s profile on LinkedIn, the world's largest professional community. Aditya Anirudh has 3 jobs listed on their profile. See the complete profile on LinkedIn and discover ...
U TURN / Marokasari chudu / Samantha / Anirudh Ravichander / …
https://www.youtube.com/watch?v=Il4W1VuvMlM
Summary :  12-10-2019 · Hai all This Is My Second Video..
Velaikkaran - Iraiva Video l Sivakarthikeyan, Nayanthara l Anirudh ...
https://www.youtube.com/watch?v=dE5SLY5tKEc
Summary :  29-12-2017 · Presenting this stunning video featuring the super-talented Anirudh , the charming Jonita Gandhi , lead pair of Velaikkaran- the dapper Sivakarthikeyan and the gorgeous Nayanthara.

Process finished with exit code 0

## Required Packages

```sh
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

