# Web Scraping

Have you ever needed to collect data from websites where the data is not made readily available? If you have, then you probably spent a significant amount of time copying and pasting from the website to a spreadsheet, and trying to carefully collect only the information that you need, while avoiding mistakes based on copying and pasting or typing. If your project required that data be collected from *many* pages, then this likely became a painful and repetitive effort that occupied a substantial amount of time.

Fortunately, your knowledge of Python can facilitate the data collection process through libraries designed to automate the collection of data from large numbers of pages. This class, we will focus on how to use a few of these libraries to streamline the collection of information from websites. The best way to understand this process is to do it, so we will be walking through the process while learning about why we scrape data the way that we do.

## Accessing a website through Python

Obviously, if we want to scrape a website, we will first want to *access* that website. We can do this with the `requests` library, like we did back in Topic 5 to grab some text for our regex experiments.


```python
import requests
myPage = requests.get("https://brickset.com/sets/year-2020")
```

During this lesson, we will be using [brickset.com](https://brickset.com/) as our example. This is a GREAT website for learning to scrape, because all of the information that we will attempt to collect can also be collected via the CSV export tool built into the website! This means that we can very easily compare our results against a CSV of the *correct* results to determine whether or not the results of our scrape match the true output of the website. Even better, the website is about Legos, and Legos are the best!

Now we will focus on exploring the page to see what information we can extract.

## Process the HTML


```python
from bs4 import BeautifulSoup

parsed = BeautifulSoup(myPage.text)
```

The code above imports the `BeautifulSoup` library/function, and prepares our requested URL for scraping. When we feed our website into the parser, we need to make sure to pass the `text` attribute of the requested URL, since this is the place in which the full HTML of the page is stored. If we just pass the `myPage` object, then we will be unable to parse the HTML like we want to. Now, we simply store a parsed website as an object (in this case we call it `parsed`), and we are ready to go.


```python
parsed.title
```




    <title>2020  | Brickset: LEGO set guide and database</title>



`BeautifulSoup`'s parsed pages are structured based on the HTML tags that are encountered within the page. For example, above we requested the `title` tag from the page, and we got back the full tag, as well as all content within that tag. In order to only return the text inside the tag, we can use the following code:


```python
parsed.title.text
```




    '2020  | Brickset: LEGO set guide and database'



For a tag with nothing else embedded inside, this is a great way to extract the text. However, many tags will contain one or more other tags, which add to the formatting of the page. The tag that we will be most interested in for now is the `article` tag, which is wrapped around each individual Lego set that is listed on the website. If we just look for the article tag like we did with the title, then we will only see the first article on the page:


```python
parsed.article
```




    <article class="set">
    <a class="highslide plain mainimg" href="/assets/images/misc/blankbox.gif" onclick="return hs.expand(this)"><img onerror="this.src='/assets/images/spacer2.png'" src="/assets/images/misc/blankbox.gif" title="356-2: Basic Building Set with Storage Case"/></a>
    <div class="highslide-caption">
    <h1>Basic Building Set with Storage Case</h1><div class="tags floatleft"><a href="/sets/356-2/Basic-Building-Set-with-Storage-Case">356-2</a> <a href="/sets/theme-Basic">Basic</a> <a class="year" href="/sets/theme-Basic/year-2020">2020</a> </div><div class="floatright">©2020 LEGO Group</div>
    <div class="pn">
    <a href="#" onclick="return hs.previous(this)" title="Previous (left arrow key)">« Previous</a>
    <a href="#" onclick="return hs.next(this)" title="Next (right arrow key)">Next »</a>
    </div>
    </div>
    <div class="meta"><h1><a href="/sets/356-2/Basic-Building-Set-with-Storage-Case"><span>356: </span> Basic Building Set with Storage Case</a></h1><div class="tags"><a href="/sets/356-2/Basic-Building-Set-with-Storage-Case">356-2</a> <a href="/sets/theme-Basic">Basic</a> <a class="year" href="/sets/theme-Basic/year-2020">2020</a> </div><div class="tags"><span id="tags30652"></span></div><div class="col"><dl><dt>Pieces</dt><dd>1987</dd><dt>Set type</dt><dd>Normal</dd></dl></div><div class="col"><dl></dl><dl class="highlight"></dl></div></div><div class="action"><dl class="admin"><dt class="hideingallery">Our community</dt><dd class="hideingallery"><a class="popuplink" href="ownedBy?SetID=30652">0 own this set</a>, 3 want it</dd></dl><dl class="admin"><dt class="hideingallery">Your collection</dt><dd><a href="/signup">Sign up</a> for a free account to record your LEGO collection here at Brickset</dd></dl><dl class="buylinks"><dt>Buy this set at</dt><dd><ul><li>
    </li><li>
    <a class="amazon" href="https://www.amazon.com/s/?url=search-alias=aps&amp;field-keywords=LEGO%20356&amp;tag=brickset-20&amp;link_code=wql&amp;camp=212361&amp;creative=380601&amp;_encoding=UTF-8">Amazon</a>
    </li><li>
    <a class="ebay" href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=9&amp;pub=5574779132&amp;toolid=10001&amp;campid=5336183597&amp;customid=&amp;icep_uq=LEGO+356&amp;icep_sellerId=&amp;icep_ex_kw=&amp;icep_sortBy=12&amp;icep_catId=&amp;icep_minPrice=&amp;icep_maxPrice=&amp;ipn=psmain&amp;icep_vectorid=229466&amp;kwid=902099&amp;mtid=824&amp;kw=lg">eBay</a>
    </li><li>
    <a class="bricklink" href='http://alpha.bricklink.com/pages/clone/catalogitem.page?S=356-2#T=S&amp;O={"ss":"US"}'>BrickLink</a>
    </li></ul></dd></dl></div></article>



Wow! There sure is a lot of stuff for us to work through within that tag! It turns out that the article tag contains *everything* related to a particular set, so we will have to work through that information more carefully if we would like to be able to scrape information about each set. 

The first thing that we need to do, though, is collect ALL of the article tags (or all of the sets), so that we can scrape each one and collect the most useful information.

## Explore the Page

Our processed website has some other tools besides being able to reference each tag. One of the most helpful is a method called `find_all`, which will allow us to look in a specific portion of the page (or across the whole page) for *all instances* of a specific tag. Before, we could only see the first instance of the article tag, but this will allow us to find all the articles on a page!

In order to not end up with a massive text blob for output, let's store the results of our `find_all` method in a list.


```python
a = [i for i in parsed.find_all('article')]
```

To store the article tags in a list, we use a simple list comprehension, so that each separate article tag is a new entry in the list called `a`. One of the really cool things about `BeautifulSoup` is that each object is treated just like the full parsed webpage: we can use tags as attributes to walk through each of our new objects in the list.

Let's try finding a `ul` tag inside of the first article:


```python
a[1].ul
```




    <ul><li>
    <a class="lego" href="https://click.linksynergy.com/link?id=oSv/vWYkQIY&amp;offerid=115554.10270&amp;type=15&amp;murl=https%3A%2F%2Fwww.lego.com%2Fen-us%2Fproduct%2Fbookshop-10270">LEGO</a></li><li>
    <a class="amazon" href="https://www.amazon.com/s/?url=search-alias=aps&amp;field-keywords=LEGO%2010270&amp;tag=brickset-20&amp;link_code=wql&amp;camp=212361&amp;creative=380601&amp;_encoding=UTF-8">Amazon</a>
    </li><li>
    <a class="ebay" href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?icep_ff3=9&amp;pub=5574779132&amp;toolid=10001&amp;campid=5336183597&amp;customid=&amp;icep_uq=LEGO+10270&amp;icep_sellerId=&amp;icep_ex_kw=&amp;icep_sortBy=12&amp;icep_catId=&amp;icep_minPrice=&amp;icep_maxPrice=&amp;ipn=psmain&amp;icep_vectorid=229466&amp;kwid=902099&amp;mtid=824&amp;kw=lg">eBay</a>
    </li><li>
    <a class="bricklink" href='http://alpha.bricklink.com/pages/clone/catalogitem.page?S=10270-1#T=S&amp;O={"ss":"US"}'>BrickLink</a>
    </li></ul>



Awesome! We can walk through that list if we would like, as well!

Next, let's see how many articles are stored on each page of search results:


```python
parsed.find("ul", class_="pagelength").span.text
```




    '25'



It looks like each results page has 25 or fewer results. How did we know to look for a `ul` tag that had the class `pagelength`? We opened a page of results up, and we used the developer "Inspect" tool built into our browser to help us find the part of the page that tells us how many results will be shown on each page. As we prepare to scrape a page, we will spend a lot of time going back and forth between the website as we see it, and the code that we are designing to scrape that website.

As we look through our list of articles, though, we will want to start extracting information that will help us learn about each Lego set. Let's try our hand at finding the name of the sets, and the price of the sets in Euros. Fortunately, the title of each set will be very easy to find. If we inspect the title of the first result (using the link that we started with at the top of the notebook), we can see that the name of the set is stored within the article tag using an `h1` tag. Let's request that from our list:


```python
a[1].h1.text
```




    'Basic Building Set with Storage Case'



Perfect! We get back the text title for our first search result! We can also return the title of each set on the page:


```python
[i.h1.text for i in a]
```




    ['Basic Building Set with Storage Case',
     'Bookshop',
     'Fiat 500',
     'Old Trafford - Manchester United',
     'Haunted House',
     '{?}',
     '{?}',
     '{?}',
     'Crocodile Locomotive',
     'Heart Box',
     'Brick Box',
     'Deluxe Brick Box',
     'Alphabet Truck',
     'Fire Truck',
     'Tow Truck',
     'Batcave',
     "Elsa and Olaf's Tea Party",
     'Super Heroes Lab',
     "Ariel's Undersea Castle",
     "Lightning McQueen's Race Day",
     'Playroom',
     'Bedroom',
     'Pizza Stand',
     'Bakery',
     'Modular Playhouse']



That was the easy part. Now that we have the set names, we need to find their prices. We will start by finding their prices on the website itself. We can see that the prices are listed in both dollars and Euros, and that they are always shown next to text that says "RRP". This stands for Recommended Retail Price, and is the number we want to collect.

Our first step in extracting the price is to note that, because the price changes from set to set, we are going to have to find some other consistent marker from which we can reference the price. That marker is the text "RRP". We need to describe a way to always reach that text, no matter which set we are focused on. If we inspect the page, we will see that "RRP" is contained in a `dt` tag. There are several of these tags, each containing different information about the set, so we will need to make sure that we get the right one.

Using the `.find` method, we can tell `BeautifulSoup` to look for a tag of specific kind (in this case, `dt`) with some attribute (in this case, text that is equal to "RRP").


```python
a[1].find('dt', text="RRP")
```




    <dt>RRP</dt>



Got it! This isn't so bad if we just move slowly. Next up, we need to make our way from the "RRP" tag to the tag containing the price. It turns out that `dt` tags are part of a table, and each one will correspond to a `dd` tag. These tags within a table are considered **siblings**, meaning that they exist embedded within the same tag as one another. 

Since the `dd` tag containing the price ALWAYS immediately follows the `dt` containing "RRP", we can use the `.find_next_sibling()` method to move from the `dt` tag to the `dd` tag! The price is contained as the text of the `dd` tag, so let's go ahead and grab that text, now.


```python
a[1].find('dt', text="RRP").find_next_sibling().text
```




    '$179.99, 155.96€ | More'



Almost there.... Unfortunately, the text contains more stuff than just the price in Euros. It turns out that the website just has a blob of text that contains prices, possibly in dollars, possibly in Euros, and possibly both, with some extra text at the end. Since price isn't a consistent number of digits, we need a way to recognize patterns in text and extract only the part that we want.

Regular expression comes to the rescue!


```python
import re

re.search(r'(\d+.\d+)(\u20AC)', a[1].find('dt', text="RRP").find_next_sibling().text, re.UNICODE).groups()[0]
```




    '155.96'



`r'(\d+.\d+)(\u20AC)'` is a regular expression that looks for one or more numbers before a period, a period, and one or more numbers after the period followed by the Euro symbol (`\u20AC` is the code that represents the Euro symbol). We simply provide the string to the `re.search` function, along with our regular expression and an extra argument (`re.UNICODE`) that allows us to find less common characters like the Euro symbol.

When we get back the results from this search, we only need the first group (or value in parentheses), which omits the Euro symbol. This will return only the number value representing the price of the set. It's a string, but we can easily convert it to a number using the `float()` function.

Now that we know how to find each of the two values that we care about, it is time to start formalizing our code with a `for` loop to grab the same pieces of information from each set. We can use our loop to walk through each `article` tag and extract the relevant information.


```python
data = []

for i in a:
    row = []
    row.append(i.h1.text)
    try:
        row.append(re.search(r'(\d+.\d+)(\u20AC)', i.find('dt', text="RRP").find_next_sibling().text, re.UNICODE).groups()[0])
    except:
        row.append('')
    data.append(row)
```

We created an empty list called `data`, and our `for` loop was used to add rows to that list. Each row consists of a list of two items: set name and set price. Once we have created the list representing that row, we simply append it to the `data` list and move on to the next set.

The next step (below) is to create a Data Frame based on our list called `data`, and to name our columns. This provides easy structure and functionality to our data:


```python
import pandas as pd

data = pd.DataFrame(data, columns = ['Set', 'Price_Euro'])

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
      <th>Set</th>
      <th>Price_Euro</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Basic Building Set with Storage Case</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bookshop</td>
      <td>155.96</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fiat 500</td>
      <td>77.97</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Old Trafford - Manchester United</td>
      <td>263.18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Haunted House</td>
      <td>224.19</td>
    </tr>
    <tr>
      <th>5</th>
      <td>{?}</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>{?}</td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <td>{?}</td>
      <td></td>
    </tr>
    <tr>
      <th>8</th>
      <td>Crocodile Locomotive</td>
      <td>97.47</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Heart Box</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Brick Box</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Deluxe Brick Box</td>
      <td>48.73</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Alphabet Truck</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Fire Truck</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Tow Truck</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Batcave</td>
      <td>34.11</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Elsa and Olaf's Tea Party</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Super Heroes Lab</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Ariel's Undersea Castle</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Lightning McQueen's Race Day</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Playroom</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Bedroom</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Pizza Stand</td>
      <td>9.74</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Bakery</td>
      <td>38.98</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Modular Playhouse</td>
      <td>58.48</td>
    </tr>
  </tbody>
</table>
</div>



## Moving On (to the next page)

Now that we have established a patter of code that is able to collect the information we desire, it is time to make sure that we can collect the same information from each page of search results. It is typically insufficient to collect only one page of search results, so we want to be able to follow the links in our search from page to page in order to continue collecting data.

On the page, we can inspect the button that navigates from one page to the next. We find that the element is an `li` or list item tag, with a class of `next`. Using the `find` method, we can can then extract the `href` parameter from the `a` tag representing the link that takes us to the next page:


```python
nextPage = parsed.find('li', class_="next").a['href']

nextPage
```




    'https://brickset.com/sets/year-2020/page-2'



This link certainly looks like it will take us to the next page of results! Now, we can consolidate the code that we used above into a single code block, so that we can recycle our code to collect data from another page of search results. Below is the code that we have collected so far, applied to the second page of results.


```python
myPage = requests.get(nextPage)

parsed = BeautifulSoup(myPage.text)
a = [i for i in parsed.find_all('article')]

newData = []

for i in a:
    row = []
    row.append(i.h1.text)
    try:
        row.append(re.search(r'(\d+.\d+)(\u20AC)', i.find('dt', text="RRP").find_next_sibling().text, re.UNICODE).groups()[0])
    except:
        row.append('')
    newData.append(row)

newData = pd.DataFrame(newData, columns = ['Set', 'Price_Euro'])

newData
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
      <th>Set</th>
      <th>Price_Euro</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bulldozer</td>
      <td>9.74</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Truck &amp; Tracked Excavator</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wrecking Ball Demolition</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tower Crane &amp; Construction</td>
      <td>116.97</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Creative Animals</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Creative Blue Bricks</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Creative Green Bricks</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bricks and Houses</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bricks and Lights</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>9</th>
      <td>White Baseplate</td>
      <td>7.79</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bricks and Animals</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Bricks Bricks Plates</td>
      <td>68.23</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Robot</td>
      <td></td>
    </tr>
    <tr>
      <th>13</th>
      <td>Tokyo</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Dubai</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>15</th>
      <td>The White House</td>
      <td>97.47</td>
    </tr>
    <tr>
      <th>16</th>
      <td>BigFig Creeper and Ocelot</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>17</th>
      <td>BigFig Pig with Baby Zombie</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>18</th>
      <td>The Panda Nursery</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>19</th>
      <td>The Pillager Outpost</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>20</th>
      <td>The Illager Raid</td>
      <td>68.23</td>
    </tr>
    <tr>
      <th>21</th>
      <td>The Crafting Box 3.0</td>
      <td>77.97</td>
    </tr>
    <tr>
      <th>22</th>
      <td>The Taiga Adventure</td>
      <td>9.74</td>
    </tr>
    <tr>
      <th>23</th>
      <td>The Redstone Battle</td>
      <td>53.60</td>
    </tr>
    <tr>
      <th>24</th>
      <td>International Space Station</td>
      <td>68.23</td>
    </tr>
  </tbody>
</table>
</div>



Additionally, we can concatenate our Data Frames so that we have a single Data Frame containing all of the results from our scrape. After we concatenate our data, it is good practice to reset the index using the `.reset_index()` method. This will overwrite the index of the Data Frame so that it does not have any repeat values. Be sure to include the argument `drop=True`, so that the old index isn't added back into your Data Frame.


```python
data = pd.concat([data, newData], axis=0).reset_index(drop=True)

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
      <th>Set</th>
      <th>Price_Euro</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Basic Building Set with Storage Case</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bookshop</td>
      <td>155.96</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fiat 500</td>
      <td>77.97</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Old Trafford - Manchester United</td>
      <td>263.18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Haunted House</td>
      <td>224.19</td>
    </tr>
    <tr>
      <th>5</th>
      <td>{?}</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>{?}</td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <td>{?}</td>
      <td></td>
    </tr>
    <tr>
      <th>8</th>
      <td>Crocodile Locomotive</td>
      <td>97.47</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Heart Box</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Brick Box</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Deluxe Brick Box</td>
      <td>48.73</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Alphabet Truck</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Fire Truck</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Tow Truck</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Batcave</td>
      <td>34.11</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Elsa and Olaf's Tea Party</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Super Heroes Lab</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Ariel's Undersea Castle</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Lightning McQueen's Race Day</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Playroom</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Bedroom</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Pizza Stand</td>
      <td>9.74</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Bakery</td>
      <td>38.98</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Modular Playhouse</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Bulldozer</td>
      <td>9.74</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Truck &amp; Tracked Excavator</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Wrecking Ball Demolition</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Tower Crane &amp; Construction</td>
      <td>116.97</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Creative Animals</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Creative Blue Bricks</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Creative Green Bricks</td>
      <td>4.86</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Bricks and Houses</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Bricks and Lights</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>34</th>
      <td>White Baseplate</td>
      <td>7.79</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Bricks and Animals</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Bricks Bricks Plates</td>
      <td>68.23</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Robot</td>
      <td></td>
    </tr>
    <tr>
      <th>38</th>
      <td>Tokyo</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Dubai</td>
      <td>58.48</td>
    </tr>
    <tr>
      <th>40</th>
      <td>The White House</td>
      <td>97.47</td>
    </tr>
    <tr>
      <th>41</th>
      <td>BigFig Creeper and Ocelot</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>42</th>
      <td>BigFig Pig with Baby Zombie</td>
      <td>14.61</td>
    </tr>
    <tr>
      <th>43</th>
      <td>The Panda Nursery</td>
      <td>19.49</td>
    </tr>
    <tr>
      <th>44</th>
      <td>The Pillager Outpost</td>
      <td>29.23</td>
    </tr>
    <tr>
      <th>45</th>
      <td>The Illager Raid</td>
      <td>68.23</td>
    </tr>
    <tr>
      <th>46</th>
      <td>The Crafting Box 3.0</td>
      <td>77.97</td>
    </tr>
    <tr>
      <th>47</th>
      <td>The Taiga Adventure</td>
      <td>9.74</td>
    </tr>
    <tr>
      <th>48</th>
      <td>The Redstone Battle</td>
      <td>53.60</td>
    </tr>
    <tr>
      <th>49</th>
      <td>International Space Station</td>
      <td>68.23</td>
    </tr>
  </tbody>
</table>
</div>



## Functional Scraping Code

We talked about functions earlier in the term as an excellent way to make our code more reusable, and to eliminate the need to copy and paste code with the risk of creating more typos and places for code to be updated. Now that we know how to scrape useful information from a website, let's create a function to do the work for us, so that we don't have to copy and paste the code for each subsequent page of search results.

In order to make our code into a function, we will have to create a function that takes a starting URL (the URL for our search results), and returns a Data Frame after reading through each page of the search results. We will have to perform some abstraction to make our code work on each page, but the differences are pretty minor:

- Use `requests.get()` on the URL passed to the function
- Check whether or not a "next" page exists
    - If there IS a next page, we need to call the function on *that* page, then merge the results
    - If there is NOT a next page, we return the existing data as a Data Frame.
    
Take some time to examine the code below and how each of these changes is made:


```python
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import time

# A function to collect lego sets from search results on brickset.com
def collectLegoSets(startURL):
    # Add headers to imitate a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://www.google.com/'
    }
    # Retrieve starting URL
    myPage = requests.get(startURL)

    # Parse the website with Beautiful Soup
    parsed = BeautifulSoup(myPage.text)
    
    # Grab all sets from the page
    a = [i for i in parsed.find_all('article')]

    # Create and empty data set
    newData = []

    # Iterate over all sets on the page
    for i in a:
        row = []
        # Add the set name to the row of data
        row.append(i.h1.text)
        try:
            # Extract price and translate to a floating point number from string, append to row IF PRICE EXISTS
            row.append(float(re.search(r'(\d+.\d+)(\u20AC)', i.find('dt', text="RRP").find_next_sibling().text, re.UNICODE).groups()[0]))
        except:
            # Missing value for sets with no price, append to row IF NO PRICE EXISTS
            row.append(np.nan)
        
        # Add the row of data to the dataset
        newData.append(row)

    newData = pd.DataFrame(newData, columns = ['Set', 'Price_Euro'])
    
    # Check if there are more results on the "next" page
    try:
        nextPage = parsed.find('li', class_="next").a['href']
    except:
        nextPage = None
    
    # If there is another page of results, grab it and combine
    if nextPage:
        time.sleep(2)
        return pd.concat([newData, collectLegoSets(nextPage)], axis=0)
    # Otherwise return the current data
    else:
        return newData
```

*Note: We sometimes need to use **headers** (text telling the website what kind of browser we are "using") so that we are able to access the website we want to scrape. Mileage will vary by website*
(Shoutout to Kiran Best of Aalto University for finding the right header to keep this site working as an example)

Observe that we use several `try`-`except` blocks. These code blocks permit us to write code that *might* result in an error. This is the code that is indented beneath the `try` keyword. Then, we write code that should be executed whenever an error *does* occur under the `except` keyword. In this way, we prevent errors from breaking our function, and we can better control the data that is recorded in our Data Frame. Let's run the code now:


```python
lego2020 = collectLegoSets("https://brickset.com/sets/year-2020")

lego2020
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
      <th>Set</th>
      <th>Price_Euro</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Basic Building Set with Storage Case</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bookshop</td>
      <td>155.96</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Fiat 500</td>
      <td>77.97</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Old Trafford - Manchester United</td>
      <td>263.18</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Haunted House</td>
      <td>224.19</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Building LEGO Trains</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Porsche 911: Legends Made of LEGO</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Iconic Objects Made From LEGO Bricks</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Newsstand</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Valentine's Bear</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>663 rows × 2 columns</p>
</div>



There you have it! A single, easy-to-read function that will collect data on all Lego sets from the year 2020 into a Data Frame for us to analyze. We can even use this Data Frame to streamline calculations:


```python
lego2020['Price_Euro'].mean()
```




    40.550406504065045



Based on the data we have collected, the mean price (in Euros) of 2020 Lego sets is 40.61€.

Now, it's your turn to collect data!

**Solve it**:

Update the code used in this lesson to extract the following information regarding Lego sets from the year 2019:
- Name of the set
- Price of the set (in Euros)
- Number of pieces
- Number of minifigs

You should collect this information for ALL lego sets from 2019 (there are 820). Store your results in a Data Frame called `lego2019`. The columns should be labeled `Set`, `Price_Euro`, `Pieces`, `Minifigs`, respectively. The Data Frame should have the first page of results at the top, and the last page of results at the bottom (this order will enable comparison of your results with mine). You will receive points for the following:

- `lego2019` contains 820 entries [1 point]
- Columns are labeled `Set`, `Price_Euro`, `Pieces`, `Minifigs`, respectively [1 point]
- Column `Set` contains the correct names for each set [1 point]
- Column `Price_Euro` contains the correct price in Euros for each set (missing prices should be replaced with `np.nan`) [1 point]
- Column `Pieces` contains the correct number of pieces (replaced with `np.nan` where missing) [1 point]


*WARNING: This submission will be slow to grade, since it will take a while for your code to scrape the website and process the data! Be patient. The grading algorithm will give you 180 seconds before it stops grading.*

Please put ALL NECESSARY CODE into the cell below:


