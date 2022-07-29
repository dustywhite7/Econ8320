# Web APIs - The Alternative to Scraping

Web scraping doesn't always work. Many modern websites are built in a way that makes it particularly hard to scrape. They may do one of the following:

- Incorporate "infinite scrolling", so that the page that is loaded is not the same as the content you want to scrape
- Block scraping through bot detection
- Have a website sufficiently complex that scraping is too hard to implement

Why would websites actively discourage or even make scraping impossible? For the most part, we can imagine websites as a storefront. The website is designed to provide some good or service in exchange for either money (through purchases) or in exchange for the consumption of advertisements or other forms of compensation. Although these "storefronts" are online, they are not costless. 

Every time a website is requested, the server must send that information to the person/computer/bot that has requested it. This might be very cheap for a single request, but these costs add up when hundreds, thousands, or even millions of requests must be processed. When we scrape a website, we are in essence trying to collect a good (data) without compensating the group who maintains the website. For this reason, many websites will seek to block web scraping whenever they detect it, and will include a statement to this effect in their terms of service.

In cases where scraping is not feasible for one reason or another, we will need an alternative way to collect data. Web APIs will be our key to data collection in these situations.

## What are Web APIs?

The acronym **API** stands for **Application Programming Interface**, and is the name for the way in which a program or user may communicate with another program. Using an API enables the creation of explicit mechanisms for input and output of data.

A **web API** is simply the API that allows users and programs to interact with a website or web service, so that we can automate or streamline online interactions. APIs are used for the following (and much more!):

- 3rd party social media apps
- Map interfaces on business websites
- Data collection


## Comparing APIs to Scraping

When using a web API, our process is very different than when we scrape. As discussed earlier, scraping typically occurs at the expense of the service provider, making many websites averse to allowing scraping to take place. On the other hand, when using an API, there is an explicit agreement between the provider of data and the consumer. In many cases, APIs cost money to use, and are designed to compensate the service provider in a transaction reflecting the fact that the consumer no longer seeks to buy a good/service on the website or view advertisements. Instead, the data being transferred is the product to be consumed.

While we will use a free and open API to learn during this class, bear in mind that many (if not most) APIs will require the user to register before making requests, and may also require payment. This arrangement allows both users and providers to benefit from the exchange of data.

## Using a Web API

To learn about using web APIs, we will experiment with the free location API provided by [zippopotam.us](http://www.zippopotam.us/). We will learn the basics of API use with the simple examples that can be implemented through the Zippopotamus API, and hopefully make some fun graphs while we are at it!

Most web APIs are accessed through the use of a URL, just like any other website. We then use the various extensions of the URL to make a request for an API call, rather than to request a specific website. Let's give this a try with the `requests` library, and see what we get back as we request various URLs from Zippopotamus:


```python
import requests

requests.get("https://api.zippopotam.us/us/68022").text
```




    '{"post code": "68022", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Elkhorn", "longitude": "-96.2431", "state": "Nebraska", "state abbreviation": "NE", "latitude": "41.2756"}]}'



Cool! We got some random stuff when we requested a random page from Zippopotamus... What is this? Let's break down our URL to learn more about what is going on:

 - `https://api.zippopotam.us` is the URL that we will always call when making requests to or from Zippopotamus
 - `/us` tells Zippopotamus that the location we are referencing is in the United States
 - `/68022` is the postal code for which we want to extract information from Zippopotamus
 
The data that we receive back from our request is information about the postal code that we want to examine. Before we start learning how to work with our results, let's try another API call:


```python
requests.get("https://api.zippopotam.us/us/wa/redmond").text
```




    '{"country abbreviation": "US", "places": [{"place name": "Redmond", "longitude": "-122.1232", "post code": "98052", "latitude": "47.6718"}, {"place name": "Redmond", "longitude": "-122.0386", "post code": "98053", "latitude": "47.6462"}, {"place name": "Redmond", "longitude": "-121.8034", "post code": "98073", "latitude": "47.4323"}], "country": "United States", "place name": "Redmond", "state": "Washington", "state abbreviation": "WA"}'



In this new request, we have the following:

- `https://api.zippopotam.us` is the URL that we will always call when making requests to or from Zippopotamus
- `/us` tells Zippopotamus that the location we are referencing is in the United States
- `/wa` tells Zippopotamus that the location is in Washington state
- `/redmond` is the city for which we would like to extract information

As might be evident from the differences between the two requests we have made, many APIs are able to access different kinds of information depending on the different requests that we make. We can find information on the city in which a postal code is located, or we can find postal codes within a city of interest! This will allow us to make requests that will generate a map of places that I have lived during my life. Let's try it out.


```python
livedThere = [
    {"country": "/us", "postal_code": "/92056"},
    {"country": "/us", "postal_code": "/98052"},
    {"country": "/us", "postal_code": "/84602"},
    {"country": "/br", "postal_code": "/96225-000"},
    {"country": "/br", "postal_code": "/96600-000"},
    {"country": "/us", "postal_code": "/99163"},
    {"country": "/us", "postal_code": "/68022"},
    {"country": "/us", "postal_code": "/84102"},
]
```

The cell above contains a list of dictionaries. I will iterate over this list to create my API calls:


```python
for i in livedThere:
    call = "https://api.zippopotam.us{0}{1}".format(i["country"],i["postal_code"])
    print(call)
```

    https://api.zippopotam.us/us/92056
    https://api.zippopotam.us/us/98052
    https://api.zippopotam.us/us/84602
    https://api.zippopotam.us/br/96225-000
    https://api.zippopotam.us/br/96600-000
    https://api.zippopotam.us/us/99163
    https://api.zippopotam.us/us/68022
    https://api.zippopotam.us/us/84102


The above code combines my country codes for each location with the postal code and the base-URL to provide my API call. Now it is time to write some code to retrieve each request and store the results in a new list:


```python
locales = []

for i in livedThere:
    call = "https://api.zippopotam.us{0}{1}".format(i["country"],i["postal_code"])
    locales.append(requests.get(call).text)
    
locales
```




    ['{"post code": "92056", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Oceanside", "longitude": "-117.2831", "state": "California", "state abbreviation": "CA", "latitude": "33.1968"}]}',
     '{"post code": "98052", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Redmond", "longitude": "-122.1232", "state": "Washington", "state abbreviation": "WA", "latitude": "47.6718"}]}',
     '{"post code": "84602", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Provo", "longitude": "-111.7325", "state": "Utah", "state abbreviation": "UT", "latitude": "40.3563"}]}',
     '{"post code": "96225-000", "country": "Brazil", "country abbreviation": "BR", "places": [{"place name": "S\\u00e3o Jos\\u00e9 do Norte", "longitude": "-51.762", "state": "Rio Grande do Sul", "state abbreviation": "23", "latitude": "-31.8009"}]}',
     '{"post code": "96600-000", "country": "Brazil", "country abbreviation": "BR", "places": [{"place name": "Cangu\\u00e7u", "longitude": "-52.6682", "state": "Rio Grande do Sul", "state abbreviation": "23", "latitude": "-31.2117"}]}',
     '{"post code": "99163", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Pullman", "longitude": "-117.1729", "state": "Washington", "state abbreviation": "WA", "latitude": "46.7352"}]}',
     '{"post code": "68022", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Elkhorn", "longitude": "-96.2431", "state": "Nebraska", "state abbreviation": "NE", "latitude": "41.2756"}]}',
     '{"post code": "84102", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Salt Lake City", "longitude": "-111.8627", "state": "Utah", "state abbreviation": "UT", "latitude": "40.76"}]}']



Awesome! We have the results! Except, they are really garbled.... We have results, but now we need to take these results and clean them up into a useable format. Let's figure out how.

## Processing Request Results

Each response from a web API will typically be returned in a **JSON** object. **JSON** stands for **Java Script Object Notation**, and is the standard format for transmitting information on the internet. While this may sound confusing, JSON is actually very easy for us to handle in Python, because it is structured EXACTLY like a Python dictionary. All we need is a way to take a JSON object and translate it into an official `dict` object.

Lucky for us, the `json` library (built right into Python itself!) will make this an easy exercise.


```python
import json

locales = [json.loads(i) for i in locales]

locales
```




    [{'post code': '92056',
      'country': 'United States',
      'country abbreviation': 'US',
      'places': [{'place name': 'Oceanside',
        'longitude': '-117.2831',
        'state': 'California',
        'state abbreviation': 'CA',
        'latitude': '33.1968'}]},
     {'post code': '98052',
      'country': 'United States',
      'country abbreviation': 'US',
      'places': [{'place name': 'Redmond',
        'longitude': '-122.1232',
        'state': 'Washington',
        'state abbreviation': 'WA',
        'latitude': '47.6718'}]},
     {'post code': '84602',
      'country': 'United States',
      'country abbreviation': 'US',
      'places': [{'place name': 'Provo',
        'longitude': '-111.7325',
        'state': 'Utah',
        'state abbreviation': 'UT',
        'latitude': '40.3563'}]},
     {'post code': '96225-000',
      'country': 'Brazil',
      'country abbreviation': 'BR',
      'places': [{'place name': 'São José do Norte',
        'longitude': '-51.762',
        'state': 'Rio Grande do Sul',
        'state abbreviation': '23',
        'latitude': '-31.8009'}]},
     {'post code': '96600-000',
      'country': 'Brazil',
      'country abbreviation': 'BR',
      'places': [{'place name': 'Canguçu',
        'longitude': '-52.6682',
        'state': 'Rio Grande do Sul',
        'state abbreviation': '23',
        'latitude': '-31.2117'}]},
     {'post code': '99163',
      'country': 'United States',
      'country abbreviation': 'US',
      'places': [{'place name': 'Pullman',
        'longitude': '-117.1729',
        'state': 'Washington',
        'state abbreviation': 'WA',
        'latitude': '46.7352'}]},
     {'post code': '68022',
      'country': 'United States',
      'country abbreviation': 'US',
      'places': [{'place name': 'Elkhorn',
        'longitude': '-96.2431',
        'state': 'Nebraska',
        'state abbreviation': 'NE',
        'latitude': '41.2756'}]},
     {'post code': '84102',
      'country': 'United States',
      'country abbreviation': 'US',
      'places': [{'place name': 'Salt Lake City',
        'longitude': '-111.8627',
        'state': 'Utah',
        'state abbreviation': 'UT',
        'latitude': '40.76'}]}]



And we are done making our data into Python data! That was easy! Next, let's just take this list of dictionaries, and make it into a Data Frame. It turns out that we can write a little bit of code to make Data Frames out of our API results through `pandas`:


```python
import pandas as pd

locales = pd.DataFrame(locales)

data = []
for i in locales.index:
    temp = pd.DataFrame(locales.loc[i, 'places'])
    temp['post_code'] = locales.loc[i, 'post code']
    temp['country'] = locales.loc[i, 'country']
    temp['country_code'] = locales.loc[i, 'country abbreviation']
    data.append(temp)
    
data = pd.concat(data, axis=0).reset_index(drop=True)

data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>place name</th>
      <th>longitude</th>
      <th>state</th>
      <th>state abbreviation</th>
      <th>latitude</th>
      <th>post_code</th>
      <th>country</th>
      <th>country_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Oceanside</td>
      <td>-117.2831</td>
      <td>California</td>
      <td>CA</td>
      <td>33.1968</td>
      <td>92056</td>
      <td>United States</td>
      <td>US</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Redmond</td>
      <td>-122.1232</td>
      <td>Washington</td>
      <td>WA</td>
      <td>47.6718</td>
      <td>98052</td>
      <td>United States</td>
      <td>US</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Provo</td>
      <td>-111.7325</td>
      <td>Utah</td>
      <td>UT</td>
      <td>40.3563</td>
      <td>84602</td>
      <td>United States</td>
      <td>US</td>
    </tr>
    <tr>
      <th>3</th>
      <td>São José do Norte</td>
      <td>-51.762</td>
      <td>Rio Grande do Sul</td>
      <td>23</td>
      <td>-31.8009</td>
      <td>96225-000</td>
      <td>Brazil</td>
      <td>BR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Canguçu</td>
      <td>-52.6682</td>
      <td>Rio Grande do Sul</td>
      <td>23</td>
      <td>-31.2117</td>
      <td>96600-000</td>
      <td>Brazil</td>
      <td>BR</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Pullman</td>
      <td>-117.1729</td>
      <td>Washington</td>
      <td>WA</td>
      <td>46.7352</td>
      <td>99163</td>
      <td>United States</td>
      <td>US</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Elkhorn</td>
      <td>-96.2431</td>
      <td>Nebraska</td>
      <td>NE</td>
      <td>41.2756</td>
      <td>68022</td>
      <td>United States</td>
      <td>US</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Salt Lake City</td>
      <td>-111.8627</td>
      <td>Utah</td>
      <td>UT</td>
      <td>40.76</td>
      <td>84102</td>
      <td>United States</td>
      <td>US</td>
    </tr>
  </tbody>
</table>
</div>



Now that we have a nice, clean Data Frame containing the information on different locations, we can make a map out of it:


```python
import plotly.express as px

px.scatter_geo(data, 'latitude', 'longitude', 
               hover_data=['place name', 'state', 'country'], 
               color='country', 
               projection = 'natural earth',
               width = 900,
               height = 600,
               )
```

And there you have it! A map of places that I have lived!

It really looks a lot less impressive on a world map...

APIs will allow us to do all sorts of amazing work. Some APIs that are awesome but require accounts are listed below:

- [Twitter Realtime Tweet Filter](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview)
- [Tracker.gg](https://tracker.gg/)
- [Google Maps Distance Matrix](https://developers.google.com/maps/documentation/distance-matrix/intro)

With web scraping and APIs at our fingertips, our ability to gather and investigate data is limited only by our ability to come up with interesting research questions.

**Solve it:**

Below is a Data Frame called `capitals` containing capital cities in states across the United States. Use the [Zippopotam.us](https://api.zippopotam.us) API to gather latitude and longitude information on each city, and add columns named `lat` and `lon` containing the latitude and longitude data for each city, respectively. Once you have done that, map all of the cities using their latitude and longitude data on a map with `scope=usa`.

*Hints:* 
1. If you use my code, you can't use the projection that I used with `scope="usa"`. Get rid of the projection.
2. You just need to grab a single latitude and longitude for the cities. I recommend using the first one in the list.

You will be graded on the following:
- Created columns named `lat` and `lon` in the `capitals` Data Frame [1 point]
- `lat` contains correct latitude for the city [1 point]
- `lon` contains correct longitude for the city [1 point]
- Latitude and longitude values are obtained through the [Zippopotam.us](https://api.zippopotam.us) API [1 point]
- Map correctly displays capitals based on latitude and longitude values [1 point]


```python
import pandas as pd
import json
import plotly.express as px
import requests

capitals = pd.DataFrame([["Alabama","Montgomery","AL"],
["Alaska","Juneau","AK"],
["Arizona","Phoenix","AZ"],
["Arkansas","Little Rock","AR"],
["California","Sacramento","CA"],
["Colorado","Denver","CO"],
["Connecticut","Hartford","CT"],
["Delaware","Dover","DE"],
["Florida","Tallahassee","FL"],
["Georgia","Atlanta","GA"],
["Hawaii","Honolulu","HI"],
["Idaho","Boise","ID"],
["Illinois","Springfield","IL"],
["Indiana","Indianapolis","IN"],
["Iowa","Des Moines","IA"],
["Kansas","Topeka","KS"],
["Kentucky","Frankfort","KY"],
["Louisiana","Baton Rouge","LA"],
["Maine","Augusta","ME"],
["Maryland","Annapolis","MD"],
["Massachusetts","Boston","MA"],
["Michigan","Lansing","MI"],
["Minnesota","Saint Paul","MN"],
["Mississippi","Jackson","MS"],
["Missouri","Jefferson City","MO"],
["Montana","Helena","MT"],
["Nebraska","Lincoln","NE"],
["Nevada","Carson City","NV"],
["New Hampshire","Concord","NH"],
["New Jersey","Trenton","NJ"],
["New Mexico","Santa Fe","NM"],
["New York","Albany","NY"],
["North Carolina","Raleigh","NC"],
["North Dakota","Bismarck","ND"],
["Ohio","Columbus","OH"],
["Oklahoma","Oklahoma City","OK"],
["Oregon","Salem","OR"],
["Pennsylvania","Harrisburg","PA"],
["Rhode Island","Providence","RI"],
["South Carolina","Columbia","SC"],
["South Dakota","Pierre","SD"],
["Tennessee","Nashville","TN"],
["Texas","Austin","TX"],
["Utah","Salt Lake City","UT"],
["Vermont","Montpelier","VT"],
["Virginia","Richmond","VA"],
["Washington","Olympia","WA"],
["West Virginia","Charleston","WV"],
["Wisconsin","Madison","WI"],
["Wyoming","Cheyenne","WY"]], columns = ['state', 'capital', 'abbrev'])

```

