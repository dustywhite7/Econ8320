# Natural Language Processing


## Defining Natural Language Processing

As we continue further into our content this semester, you have probably noticed that each tool takes us to a new level of being able to conduct analysis with less code. As we progress, we move toward what are called "higher level" programming tools. Python itself is a high-level programming language, meaning that it is written in a way that is easier for humans to read than computers, with lots of translation happening behind the scenes. 

Tools like `pandas` remove a lot of the manual work from data processing. `numpy` and `scipy` handle much of the mathematical and statistical work that we want to do with our data. Natural Language Processing (NLP) is a tool similar to regex, but allowing us to take our text analytics to entirely new levels.

Where regex allows us to look for text-based patterns in our words or string content, we want to go further. We want to look for **meaning**-based content. How do I find content that reflects anger? What words are most common in those contexts? What about when the content reflects joy? Sadness? Regex is not enough in these cases, and so we build to an even more powerful tool.

NLP is a broad set of tools designed in order to enable users to work with text in ways that a human might work with text. When we work with text, we look for structures like sentences, and within those sentences we look for nouns to tell us who or what is the focus of the content. We look for verbs to understand what is happening. Adjectives and other descriptors help us to better understand the nuances of context. NLP models are trained to recognize these elements in text, and to be able to leverage that content to break text down and provide human users valuable information at a larger scale than would be possible if the document were simply read (slowly) by a human.

| Regex | NLP |
| --- | --- |
| Create patterns to match in text | Identify the structure of text and use that to refine information|
| Used to verify or find data | Used to analyze data |
| Applies user-defined rules | Relies heavily on ML-based (or other) models |


## What NLP can do

So what can NLP do for us?

### Identify parts of speech

When we pass a document (really a string, but typically we provide a fairly large string to an NLP algorithm) to an NLP model, it is able to identify parts of speech (nouns, verbs, etc.). This enables us to quickly break down our text to find various kinds of keywords, and is the first step in many more complex pipelines.

### Iterate over sentences

NLP can identify sentences within a document. This makes for a powerful iterative tool, as we will be able to define a processing pipeline for each sentence, and then apply that pipeline to as many sentences as exist within our document, without having to write complex code to try and recognize where each sentence starts and ends (this is MUCH harder than it sounds).

### Find words used to describe various nouns (or anything else!)

Beyond simply identifying parts of speech, NLP models can be used to build a structural dependency tree of each sentence. This structure allows us to associate adjectives with their respective nouns, or adverbs to the verb that they modify. We can explore how various entities are described in our document based on word associations. We can even visualize the structure of the sentence using simple mapping functions.

### Filter text for analysis

We can use NLP to filter our text. We can look for sentences about a specific entity, or explore other ways of filtering our text in order to create a better understanding of overall patterns in the document.

### Conduct sentiment analysis

One of the most powerful capabilities resulting from NLP models is the ability to analyze sentiment within the text. Words have the ability to convey literal meanings, as well as the more subtle capacity to convey emotion. By looking for word combinations in our text, NLP models can provide sentiment measurements at the word, sentence, or document level. This provides the ability to sort through texts for specific sentiments to learn about the way in which emotion affects the outcomes we are examining in text. One example might be looking through descriptions for negative emotions, and being able to respond to unhappy customers by flagging negative descriptions.


## Implementing NLP models

To get started with NLP models, we need to install the right libraries (and a corpus!). The library that we will use is `spacy`, although there are multiple other options available to us. One other common NLP library is `nltk`, the Natural Language Toolkit (NLTK). In my experience NLTK is more commonly employed when someone wants to create their own model from scratch, rather than implement pre-built and optimized NLP models. 

In addition to a library to conduct NLP, we also rely on a **corpus**. A corpus is essentially a model of a specific language that is built to enable the actual analysis. `spacy` as a library is a general structure that can be implemented on ANY language. The corpus allows us to select a specific language, and a model of that language built on a specific set of information. 

When we install `spacy`, we will also download the `en_core_web_sm` corpus. This corpus is a small-sized model of the english language, and was trained on web-based data. That means that it will perform best on data drawn from websites, and is not as strong a model for other contexts (like analyzing Pride and Prejudice). That doesn't mean that we can't use in other contexts, but it does suggest that results will not be as refined or accurate.


```python
# Load the SpaCy library

!pip install spacy
!python -m spacy download en_core_web_sm
```

    Collecting spacy
      Downloading spacy-3.2.3-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.0 MB)
    [K     |████████████████████████████████| 6.0 MB 4.4 MB/s eta 0:00:01     |███████████████████████████▌    | 5.1 MB 4.4 MB/s eta 0:00:01
    [?25hCollecting catalogue<2.1.0,>=2.0.6
      Downloading catalogue-2.0.6-py3-none-any.whl (17 kB)
    Collecting langcodes<4.0.0,>=3.2.0
      Downloading langcodes-3.3.0-py3-none-any.whl (181 kB)
    [K     |████████████████████████████████| 181 kB 84.7 MB/s eta 0:00:01
    [?25hCollecting cymem<2.1.0,>=2.0.2
      Downloading cymem-2.0.6-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (35 kB)
    Collecting wasabi<1.1.0,>=0.8.1
      Downloading wasabi-0.9.0-py3-none-any.whl (25 kB)
    Collecting spacy-loggers<2.0.0,>=1.0.0
      Downloading spacy_loggers-1.0.1-py3-none-any.whl (7.0 kB)
    Collecting pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4
      Downloading pydantic-1.8.2-cp37-cp37m-manylinux2014_x86_64.whl (10.1 MB)
    [K     |████████████████████████████████| 10.1 MB 13.5 MB/s eta 0:00:01    |██████████████████▋             | 5.9 MB 13.5 MB/s eta 0:00:01
    [?25hCollecting preshed<3.1.0,>=3.0.2
      Downloading preshed-3.0.6-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (125 kB)
    [K     |████████████████████████████████| 125 kB 49.9 MB/s eta 0:00:01
    [?25hRequirement already satisfied: numpy>=1.15.0 in /opt/conda/lib/python3.7/site-packages (from spacy) (1.18.5)
    Requirement already satisfied: packaging>=20.0 in /opt/conda/lib/python3.7/site-packages (from spacy) (20.9)
    Collecting spacy-legacy<3.1.0,>=3.0.8
      Downloading spacy_legacy-3.0.9-py2.py3-none-any.whl (20 kB)
    Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/conda/lib/python3.7/site-packages (from spacy) (4.40.0)
    Requirement already satisfied: typing-extensions<4.0.0.0,>=3.7.4 in /opt/conda/lib/python3.7/site-packages (from spacy) (3.7.4.3)
    Collecting typer<0.5.0,>=0.3.0
      Downloading typer-0.4.0-py3-none-any.whl (27 kB)
    Requirement already satisfied: setuptools in /opt/conda/lib/python3.7/site-packages (from spacy) (42.0.2.post20191201)
    Collecting murmurhash<1.1.0,>=0.28.0
      Downloading murmurhash-1.0.6-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (21 kB)
    Collecting blis<0.8.0,>=0.4.0
      Downloading blis-0.7.6-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (9.9 MB)
    [K     |████████████████████████████████| 9.9 MB 7.9 MB/s eta 0:00:01     |█▉                              | 552 kB 7.9 MB/s eta 0:00:02     |██████▎                         | 1.9 MB 7.9 MB/s eta 0:00:02     |██████████████████████▎         | 6.9 MB 7.9 MB/s eta 0:00:01     |████████████████████████▍       | 7.5 MB 7.9 MB/s eta 0:00:01
    [?25hRequirement already satisfied: jinja2 in /opt/conda/lib/python3.7/site-packages (from spacy) (2.10.3)
    Collecting srsly<3.0.0,>=2.4.1
      Downloading srsly-2.4.2-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (451 kB)
    [K     |████████████████████████████████| 451 kB 23.0 MB/s eta 0:00:01
    [?25hRequirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/conda/lib/python3.7/site-packages (from spacy) (2.23.0)
    Collecting pathy>=0.3.5
      Downloading pathy-0.6.1-py3-none-any.whl (42 kB)
    [K     |████████████████████████████████| 42 kB 3.0 MB/s eta 0:00:01
    [?25hCollecting thinc<8.1.0,>=8.0.12
      Downloading thinc-8.0.14-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (652 kB)
    [K     |████████████████████████████████| 652 kB 7.7 MB/s eta 0:00:01
    [?25hRequirement already satisfied: zipp>=0.5 in /opt/conda/lib/python3.7/site-packages (from catalogue<2.1.0,>=2.0.6->spacy) (0.6.0)
    Requirement already satisfied: pyparsing>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from packaging>=20.0->spacy) (2.4.7)
    Collecting smart-open<6.0.0,>=5.0.0
      Downloading smart_open-5.2.1-py3-none-any.whl (58 kB)
    [K     |████████████████████████████████| 58 kB 7.2 MB/s  eta 0:00:01
    [?25hRequirement already satisfied: chardet<4,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy) (3.0.4)
    Requirement already satisfied: idna<3,>=2.5 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy) (2.8)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy) (1.25.11)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy) (2019.11.28)
    Collecting click<9.0.0,>=7.1.1
      Downloading click-8.0.4-py3-none-any.whl (97 kB)
    [K     |████████████████████████████████| 97 kB 2.8 MB/s  eta 0:00:01
    [?25hRequirement already satisfied: importlib-metadata in /opt/conda/lib/python3.7/site-packages (from click<9.0.0,>=7.1.1->typer<0.5.0,>=0.3.0->spacy) (1.2.0)
    Requirement already satisfied: more-itertools in /opt/conda/lib/python3.7/site-packages (from zipp>=0.5->catalogue<2.1.0,>=2.0.6->spacy) (8.0.2)
    Requirement already satisfied: MarkupSafe>=0.23 in /opt/conda/lib/python3.7/site-packages (from jinja2->spacy) (1.1.1)
    Installing collected packages: murmurhash, cymem, click, catalogue, wasabi, typer, srsly, smart-open, pydantic, preshed, blis, thinc, spacy-loggers, spacy-legacy, pathy, langcodes, spacy
    Successfully installed blis-0.7.6 catalogue-2.0.6 click-8.0.4 cymem-2.0.6 langcodes-3.3.0 murmurhash-1.0.6 pathy-0.6.1 preshed-3.0.6 pydantic-1.8.2 smart-open-5.2.1 spacy-3.2.3 spacy-legacy-3.0.9 spacy-loggers-1.0.1 srsly-2.4.2 thinc-8.0.14 typer-0.4.0 wasabi-0.9.0
    [33mWARNING: You are using pip version 21.0.1; however, version 22.0.4 is available.
    You should consider upgrading via the '/opt/conda/bin/python3 -m pip install --upgrade pip' command.[0m
    Collecting en-core-web-sm==3.2.0
      Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.2.0/en_core_web_sm-3.2.0-py3-none-any.whl (13.9 MB)
    [K     |████████████████████████████████| 13.9 MB 6.1 MB/s eta 0:00:01    |▌                               | 235 kB 6.1 MB/s eta 0:00:03     |██                              | 911 kB 6.1 MB/s eta 0:00:03     |██████████▉                     | 4.7 MB 6.1 MB/s eta 0:00:02
    [?25hRequirement already satisfied: spacy<3.3.0,>=3.2.0 in /opt/conda/lib/python3.7/site-packages (from en-core-web-sm==3.2.0) (3.2.3)
    Requirement already satisfied: srsly<3.0.0,>=2.4.1 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2.4.2)
    Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2.0.6)
    Requirement already satisfied: packaging>=20.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (20.9)
    Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.8 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (3.0.9)
    Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (1.0.1)
    Requirement already satisfied: setuptools in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (42.0.2.post20191201)
    Requirement already satisfied: blis<0.8.0,>=0.4.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (0.7.6)
    Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (3.0.6)
    Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2.0.6)
    Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (1.8.2)
    Requirement already satisfied: jinja2 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2.10.3)
    Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (1.0.6)
    Requirement already satisfied: numpy>=1.15.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (1.18.5)
    Requirement already satisfied: typing-extensions<4.0.0.0,>=3.7.4 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (3.7.4.3)
    Requirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2.23.0)
    Requirement already satisfied: thinc<8.1.0,>=8.0.12 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (8.0.14)
    Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (3.3.0)
    Requirement already satisfied: wasabi<1.1.0,>=0.8.1 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (0.9.0)
    Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (4.40.0)
    Requirement already satisfied: typer<0.5.0,>=0.3.0 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (0.4.0)
    Requirement already satisfied: pathy>=0.3.5 in /opt/conda/lib/python3.7/site-packages (from spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (0.6.1)
    Requirement already satisfied: zipp>=0.5 in /opt/conda/lib/python3.7/site-packages (from catalogue<2.1.0,>=2.0.6->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (0.6.0)
    Requirement already satisfied: pyparsing>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from packaging>=20.0->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2.4.7)
    Requirement already satisfied: smart-open<6.0.0,>=5.0.0 in /opt/conda/lib/python3.7/site-packages (from pathy>=0.3.5->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (5.2.1)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2019.11.28)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (1.25.11)
    Requirement already satisfied: chardet<4,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (3.0.4)
    Requirement already satisfied: idna<3,>=2.5 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (2.8)
    Requirement already satisfied: click<9.0.0,>=7.1.1 in /opt/conda/lib/python3.7/site-packages (from typer<0.5.0,>=0.3.0->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (8.0.4)
    Requirement already satisfied: importlib-metadata in /opt/conda/lib/python3.7/site-packages (from click<9.0.0,>=7.1.1->typer<0.5.0,>=0.3.0->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (1.2.0)
    Requirement already satisfied: more-itertools in /opt/conda/lib/python3.7/site-packages (from zipp>=0.5->catalogue<2.1.0,>=2.0.6->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (8.0.2)
    Requirement already satisfied: MarkupSafe>=0.23 in /opt/conda/lib/python3.7/site-packages (from jinja2->spacy<3.3.0,>=3.2.0->en-core-web-sm==3.2.0) (1.1.1)
    Installing collected packages: en-core-web-sm
    Successfully installed en-core-web-sm-3.2.0
    [33mWARNING: You are using pip version 21.0.1; however, version 22.0.4 is available.
    You should consider upgrading via the '/opt/conda/bin/python -m pip install --upgrade pip' command.[0m
    [38;5;2m✔ Download and installation successful[0m
    You can now load the package via spacy.load('en_core_web_sm')


Now we need to get ourselves some text to analyze before we jump into the NLP world. In true form, here is another favorite old book. We will take a look at the first three chapters of Jane Eyre from [Project Gutenberg](https://www.gutenberg.org/browse/scores/top).


```python
import requests

jane = requests.get(
"https://github.com/dustywhite7/Econ8320/raw/master/AssignmentData/janeEyreCh1to3.txt"
).text

```

You can take a look at the text to get an idea of what we will be working with. Once you're ready, we will go ahead and import the `spacy` library. The very first thing we do once we import `spacy` is to load the coprus, so that we are able to use its language models to parse our document. Let's run the code, and then discuss what is happening.


```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(jane)
```

### The structure of a parsed document

When we create an `nlp` object based on our corpus, we are creating our pipeline for working with text. Our corpus contains all of the information necessary to prepare our data for analysis. When we create our `doc` object, we are passing our document through the processing pipeline. Our new parsed document (`doc` in this case), has some important **attributes**:

- `sents` - a generator function to iterate over each sentence in the document
- `token` - each individual element of the document
    - Elements exist at the word/punctuation level

After being processed, our document has been broken down into tokens, and then (to some extent) reconstructed into sentences. Additionally, each token is mapped out in relation to the other tokens within a sentence, and is described using various attributes to inform how that token relates to the text around it.


```python
test = [i.text.replace('\n', ' ') for i in doc.sents][:10] # print first 10 sentences, replacing newlines with spaces

test
```




    ['CHAPTER I   There was no possibility of taking a walk that day.',
     'We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question.',
     '  I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.',
     '  The said Eliza, John, and Georgiana were now clustered round their mama in the drawing-room: she lay reclined on a sofa by the fireside, and with her darlings about her (for the time neither quarrelling nor crying) looked perfectly happy.',
     'Me, she had dispensed from joining the group; saying, “She regretted to be under the necessity of keeping me at a distance; but that until she heard from Bessie, and could discover by her own observation, that I was endeavouring in good earnest to acquire a more sociable and childlike disposition, a more attractive and sprightly manner—something lighter, franker, more natural, as it were—she really must exclude me from privileges intended only for contented, happy, little children.”',
     '  “What does Bessie say I have done?”',
     'I asked.',
     '  “Jane, I don’t like cavillers or questioners; besides, there is something truly forbidding in a child taking up her elders in that manner.',
     'Be seated somewhere; and until you can speak pleasantly, remain silent.”',
     '  A breakfast-room adjoined the drawing-room, I slipped in there.']



### Understanding tokens

Recall that each word is represented as a token in the processed document. These tokens are immensely powerful. They are the word, but also more than that. Words in the English language are often modified based on context. Verbs are conjugated, nouns may be plural, among many possibilities. Each word is **tokenized** through our corpus in order to identify the underlying word.

This is important, because we might want to look for each instance of a single word in our corpus. Let's say that we want to find every instance of "eat". If we look for "eat", we want to make sure that "eats" and "ate", as well as "eating" and other forms are all considered. This is where tokenization becomes critical. Each token contains the text value from the original document, but also the **lemmatized** word. The lemma is the base form of the word, allowing us to search for lemmas rather than the text word. This streamlines our ability to analyze text by focusing on lemmas rather than unprocessed text.

Other valuable attributes are also associated with our tokens:
- `lemma_` - the "root word" from which a token/word is derived
- `pos_` - the part of speech of a token/word
- `dep_` - the relationship of dependent tokens to the parent token (adjectives to nouns, etc.)
- `like_email`/`like_num`/`like_url` - check if a token is like an email, number, or url (unlikely in Jane Eyre)

Let's look at the first 100 non-space, non-punctuation lemmas in Jane Eyre:


```python
lemmas100 = [(i.lemma_, i.text) for i in doc if (not i.is_punct) and (not i.is_space)][:100]

print(lemmas100) # The lemma comes first, followed by the actual word in the text.
```

    [('chapter', 'CHAPTER'), ('I', 'I'), ('there', 'There'), ('be', 'was'), ('no', 'no'), ('possibility', 'possibility'), ('of', 'of'), ('take', 'taking'), ('a', 'a'), ('walk', 'walk'), ('that', 'that'), ('day', 'day'), ('we', 'We'), ('have', 'had'), ('be', 'been'), ('wandering', 'wandering'), ('indeed', 'indeed'), ('in', 'in'), ('the', 'the'), ('leafless', 'leafless'), ('shrubbery', 'shrubbery'), ('an', 'an'), ('hour', 'hour'), ('in', 'in'), ('the', 'the'), ('morning', 'morning'), ('but', 'but'), ('since', 'since'), ('dinner', 'dinner'), ('Mrs.', 'Mrs.'), ('Reed', 'Reed'), ('when', 'when'), ('there', 'there'), ('be', 'was'), ('no', 'no'), ('company', 'company'), ('dine', 'dined'), ('early', 'early'), ('the', 'the'), ('cold', 'cold'), ('winter', 'winter'), ('wind', 'wind'), ('have', 'had'), ('bring', 'brought'), ('with', 'with'), ('it', 'it'), ('cloud', 'clouds'), ('so', 'so'), ('sombre', 'sombre'), ('and', 'and'), ('a', 'a'), ('rain', 'rain'), ('so', 'so'), ('penetrating', 'penetrating'), ('that', 'that'), ('further', 'further'), ('outdoor', 'outdoor'), ('exercise', 'exercise'), ('be', 'was'), ('now', 'now'), ('out', 'out'), ('of', 'of'), ('the', 'the'), ('question', 'question'), ('I', 'I'), ('be', 'was'), ('glad', 'glad'), ('of', 'of'), ('it', 'it'), ('I', 'I'), ('never', 'never'), ('like', 'liked'), ('long', 'long'), ('walk', 'walks'), ('especially', 'especially'), ('on', 'on'), ('chilly', 'chilly'), ('afternoon', 'afternoons'), ('dreadful', 'dreadful'), ('to', 'to'), ('I', 'me'), ('be', 'was'), ('the', 'the'), ('come', 'coming'), ('home', 'home'), ('in', 'in'), ('the', 'the'), ('raw', 'raw'), ('twilight', 'twilight'), ('with', 'with'), ('nip', 'nipped'), ('finger', 'fingers'), ('and', 'and'), ('toe', 'toes'), ('and', 'and'), ('a', 'a'), ('heart', 'heart'), ('sadden', 'saddened'), ('by', 'by'), ('the', 'the')]


We can also filter words by part of speech using the `pos_` attribute of our tokens. Let's look for the first 100 nouns in the text.


```python
nouns = [i.text for i in doc if i.pos_=='NOUN'][:100]

print(nouns) # The lemma comes first, followed by the actual word in the text.
```

    ['CHAPTER', 'possibility', 'walk', 'day', 'shrubbery', 'hour', 'morning', 'dinner', 'company', 'winter', 'wind', 'clouds', 'rain', 'so', 'penetrating', 'exercise', 'question', 'walks', 'afternoons', 'home', 'twilight', 'fingers', 'toes', 'heart', 'chidings', 'nurse', 'consciousness', 'inferiority', 'drawing', 'room', 'sofa', 'fireside', 'darlings', 'time', 'crying', 'group', 'necessity', 'distance', 'observation', 'earnest', 'disposition', 'franker', 'privileges', 'children', 'cavillers', 'questioners', 'child', 'elders', 'manner', 'breakfast', 'room', 'drawing', 'room', 'bookcase', 'volume', 'care', 'pictures', 'window', 'seat', 'feet', 'moreen', 'curtain', 'retirement', 'Folds', 'drapery', 'view', 'hand', 'panes', 'glass', 'drear', 'day', 'intervals', 'leaves', 'book', 'aspect', 'winter', 'afternoon', 'blank', 'mist', 'cloud', 'scene', 'lawn', 'storm', 'beat', 'shrub', 'rain', 'blast', 'book', 'History', 'letterpress', 'pages', 'child', 'blank', 'haunts', 'sea', 'fowl', 'rocks', 'promontories', 'coast', 'isles']


Pretty cool! If you look through that list, you'll see that there are a lot of different kinds of nouns. Two that stood out to me are "drawing" and "room"... oh wait... that's ONE NOUN that is two words! And leads us right into **noun chunks**. ;)

Sometimes, you want to be able to see a "complete" noun, and noun chunks are the tool to use!


```python
nouns = [i.text.replace('\n', ' ') for i in doc.noun_chunks][:100] # getting rid of new lines in our noun chunks

print(nouns)
```

    ['I', 'no possibility', 'a walk', 'We', 'the leafless shrubbery', 'the morning', 'dinner', '(Mrs. Reed', 'no company', 'the cold winter wind', 'it', 'clouds', 'a rain', 'further outdoor exercise', 'the question', 'I', 'it', 'I', 'long walks', 'chilly afternoons', 'me', 'the coming home', 'the raw twilight', 'nipped fingers', 'toes', 'a heart', 'the chidings', ' Bessie', 'the nurse', 'the consciousness', 'my physical inferiority', 'Eliza', 'John', 'Georgiana Reed', 'The', 'Eliza', 'John', 'Georgiana', 'the drawing-room', 'she', 'a sofa', 'the fireside', 'her darlings', 'her', 'the time', 'crying', 'she', 'the group', 'She', 'the necessity', 'me', 'a distance', 'she', 'Bessie', 'her own observation', 'I', 'good earnest', 'a more sociable and childlike disposition', 'a more attractive and sprightly manner', 'something', 'it', 'she', 'me', 'privileges', 'contented, happy, little children', 'Bessie', 'I', 'I', 'I', 'cavillers', 'questioners', 'something', 'a child', 'her elders', 'that manner', 'you', 'A breakfast-room', 'the drawing-room', 'I', 'It', 'a bookcase', 'I', 'myself', 'a volume', 'care', 'it', 'pictures', 'I', 'the window-seat', 'my feet', 'I', 'a Turk', 'the red moreen curtain', 'I', ' double retirement', 'Folds', 'scarlet drapery', 'my view', 'the right hand', 'the clear panes']


That's better. Noun chunks include all of the modifiers for a given noun, and make it easier to build a more complete understanding of the references being made. Why do we care? Because "the red moreen curtain" is the object, and we want to be sure to understand the implication of the full object, rather than only the word within the noun chunk that is actually a noun.

If we want to understand more about the nature of the relationships between words within a sentence, we can plot a dependency tree.

**NOTE: When you run the following code, be sure to click the STOP button when you're done, or no other code will run! The renderer for the dependency tree will keep running until you terminate it!**


```python
from spacy import displacy

sent = [i for i in doc.sents][100]
displacy.serve(sent, style="dep")
```

    /opt/conda/lib/python3.7/site-packages/spacy/displacy/__init__.py:98: UserWarning: [W011] It looks like you're calling displacy.serve from within a Jupyter notebook or a similar environment. This likely means you're already running a local web server, so there's no need to make displaCy start another one. Instead, you should be able to replace displacy.serve with displacy.render to show the visualization.
      warnings.warn(Warnings.W011)



<span class="tex2jax_ignore"><!DOCTYPE html>
<html lang="en">
    <head>
        <title>displaCy</title>
    </head>

    <body style="font-size: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; padding: 4rem 2rem; direction: ltr">
<figure style="margin-bottom: 6rem">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:lang="en" id="711a6b156bc64d97b55e852c621c77aa-0" class="displacy" width="7400" height="837.0" direction="ltr" style="max-width: none; height: 837.0px; color: #000000; background: #ffffff; font-family: Arial; direction: ltr">
<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="50">

</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="50">SPACE</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="225">They</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="225">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="400">had</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="400">AUX</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="575">got</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="575">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="750">me</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="750">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="925">by</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="925">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="1100">this</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1100">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="1275">time</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1275">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="1450">into</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1450">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="1625">the</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1625">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="1800">apartment</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1800">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="1975">indicated</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="1975">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="2150">by</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2150">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="2325">Mrs.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2325">PROPN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="2500">Reed,</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2500">PROPN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="2675">
</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2675">SPACE</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="2850">and</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="2850">CCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="3025">had</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3025">AUX</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="3200">thrust</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3200">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="3375">me</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3375">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="3550">upon</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3550">SCONJ</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="3725">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3725">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="3900">stool:</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="3900">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="4075">my</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4075">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="4250">impulse</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4250">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="4425">was</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4425">AUX</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="4600">to</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4600">PART</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="4775">rise</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4775">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="4950">from</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="4950">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="5125">it</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5125">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="5300">like</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5300">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="5475">a</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5475">DET</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="5650">
</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5650">SPACE</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="5825">spring;</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="5825">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="6000">their</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="6000">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="6175">two</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="6175">NUM</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="6350">pair</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="6350">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="6525">of</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="6525">ADP</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="6700">hands</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="6700">NOUN</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="6875">arrested</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="6875">VERB</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="7050">me</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="7050">PRON</tspan>
</text>

<text class="displacy-token" fill="currentColor" text-anchor="middle" y="747.0">
    <tspan class="displacy-word" fill="currentColor" x="7225">instantly.</tspan>
    <tspan class="displacy-tag" dy="2em" fill="currentColor" x="7225">ADV</tspan>
</text>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-0" stroke-width="2px" d="M70,702.0 C70,439.5 550.0,439.5 550.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-0" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M70,704.0 L62,692.0 78,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-1" stroke-width="2px" d="M245,702.0 C245,527.0 545.0,527.0 545.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-1" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M245,704.0 L237,692.0 253,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-2" stroke-width="2px" d="M420,702.0 C420,614.5 540.0,614.5 540.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-2" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M420,704.0 L412,692.0 428,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-3" stroke-width="2px" d="M595,702.0 C595,2.0 4425.0,2.0 4425.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-3" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M595,704.0 L587,692.0 603,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-4" stroke-width="2px" d="M595,702.0 C595,614.5 715.0,614.5 715.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-4" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M715.0,704.0 L723.0,692.0 707.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-5" stroke-width="2px" d="M595,702.0 C595,527.0 895.0,527.0 895.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-5" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M895.0,704.0 L903.0,692.0 887.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-6" stroke-width="2px" d="M1120,702.0 C1120,614.5 1240.0,614.5 1240.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-6" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1120,704.0 L1112,692.0 1128,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-7" stroke-width="2px" d="M945,702.0 C945,527.0 1245.0,527.0 1245.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-7" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1245.0,704.0 L1253.0,692.0 1237.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-8" stroke-width="2px" d="M595,702.0 C595,352.0 1430.0,352.0 1430.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-8" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1430.0,704.0 L1438.0,692.0 1422.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-9" stroke-width="2px" d="M1645,702.0 C1645,614.5 1765.0,614.5 1765.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-9" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1645,704.0 L1637,692.0 1653,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-10" stroke-width="2px" d="M1470,702.0 C1470,527.0 1770.0,527.0 1770.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-10" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1770.0,704.0 L1778.0,692.0 1762.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-11" stroke-width="2px" d="M1820,702.0 C1820,614.5 1940.0,614.5 1940.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-11" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">acl</textPath>
    </text>
    <path class="displacy-arrowhead" d="M1940.0,704.0 L1948.0,692.0 1932.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-12" stroke-width="2px" d="M1995,702.0 C1995,614.5 2115.0,614.5 2115.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-12" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">agent</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2115.0,704.0 L2123.0,692.0 2107.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-13" stroke-width="2px" d="M2345,702.0 C2345,614.5 2465.0,614.5 2465.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-13" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">compound</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2345,704.0 L2337,692.0 2353,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-14" stroke-width="2px" d="M2170,702.0 C2170,527.0 2470.0,527.0 2470.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-14" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2470.0,704.0 L2478.0,692.0 2462.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-15" stroke-width="2px" d="M2520,702.0 C2520,614.5 2640.0,614.5 2640.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-15" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2640.0,704.0 L2648.0,692.0 2632.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-16" stroke-width="2px" d="M595,702.0 C595,264.5 2835.0,264.5 2835.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-16" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">cc</textPath>
    </text>
    <path class="displacy-arrowhead" d="M2835.0,704.0 L2843.0,692.0 2827.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-17" stroke-width="2px" d="M3045,702.0 C3045,614.5 3165.0,614.5 3165.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-17" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3045,704.0 L3037,692.0 3053,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-18" stroke-width="2px" d="M595,702.0 C595,89.5 3195.0,89.5 3195.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-18" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">conj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3195.0,704.0 L3203.0,692.0 3187.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-19" stroke-width="2px" d="M3220,702.0 C3220,614.5 3340.0,614.5 3340.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-19" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3340.0,704.0 L3348.0,692.0 3332.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-20" stroke-width="2px" d="M3220,702.0 C3220,527.0 3520.0,527.0 3520.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-20" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3520.0,704.0 L3528.0,692.0 3512.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-21" stroke-width="2px" d="M3745,702.0 C3745,614.5 3865.0,614.5 3865.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-21" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3745,704.0 L3737,692.0 3753,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-22" stroke-width="2px" d="M3570,702.0 C3570,527.0 3870.0,527.0 3870.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-22" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M3870.0,704.0 L3878.0,692.0 3862.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-23" stroke-width="2px" d="M4095,702.0 C4095,614.5 4215.0,614.5 4215.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-23" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4095,704.0 L4087,692.0 4103,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-24" stroke-width="2px" d="M4270,702.0 C4270,614.5 4390.0,614.5 4390.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-24" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4270,704.0 L4262,692.0 4278,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-25" stroke-width="2px" d="M4445,702.0 C4445,177.0 6865.0,177.0 6865.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-25" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">ccomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4445,704.0 L4437,692.0 4453,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-26" stroke-width="2px" d="M4620,702.0 C4620,614.5 4740.0,614.5 4740.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-26" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">aux</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4620,704.0 L4612,692.0 4628,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-27" stroke-width="2px" d="M4445,702.0 C4445,527.0 4745.0,527.0 4745.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-27" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">xcomp</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4745.0,704.0 L4753.0,692.0 4737.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-28" stroke-width="2px" d="M4795,702.0 C4795,614.5 4915.0,614.5 4915.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-28" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M4915.0,704.0 L4923.0,692.0 4907.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-29" stroke-width="2px" d="M4970,702.0 C4970,614.5 5090.0,614.5 5090.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-29" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5090.0,704.0 L5098.0,692.0 5082.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-30" stroke-width="2px" d="M4795,702.0 C4795,439.5 5275.0,439.5 5275.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-30" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5275.0,704.0 L5283.0,692.0 5267.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-31" stroke-width="2px" d="M5495,702.0 C5495,527.0 5795.0,527.0 5795.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-31" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">det</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5495,704.0 L5487,692.0 5503,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-32" stroke-width="2px" d="M5670,702.0 C5670,614.5 5790.0,614.5 5790.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-32" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5670,704.0 L5662,692.0 5678,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-33" stroke-width="2px" d="M5320,702.0 C5320,439.5 5800.0,439.5 5800.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-33" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M5800.0,704.0 L5808.0,692.0 5792.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-34" stroke-width="2px" d="M6020,702.0 C6020,527.0 6320.0,527.0 6320.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-34" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">poss</textPath>
    </text>
    <path class="displacy-arrowhead" d="M6020,704.0 L6012,692.0 6028,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-35" stroke-width="2px" d="M6195,702.0 C6195,614.5 6315.0,614.5 6315.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-35" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nummod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M6195,704.0 L6187,692.0 6203,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-36" stroke-width="2px" d="M6370,702.0 C6370,439.5 6850.0,439.5 6850.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-36" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">nsubj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M6370,704.0 L6362,692.0 6378,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-37" stroke-width="2px" d="M6370,702.0 C6370,614.5 6490.0,614.5 6490.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-37" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">prep</textPath>
    </text>
    <path class="displacy-arrowhead" d="M6490.0,704.0 L6498.0,692.0 6482.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-38" stroke-width="2px" d="M6545,702.0 C6545,614.5 6665.0,614.5 6665.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-38" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">pobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M6665.0,704.0 L6673.0,692.0 6657.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-39" stroke-width="2px" d="M6895,702.0 C6895,614.5 7015.0,614.5 7015.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-39" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">dobj</textPath>
    </text>
    <path class="displacy-arrowhead" d="M7015.0,704.0 L7023.0,692.0 7007.0,692.0" fill="currentColor"/>
</g>

<g class="displacy-arrow">
    <path class="displacy-arc" id="arrow-711a6b156bc64d97b55e852c621c77aa-0-40" stroke-width="2px" d="M6895,702.0 C6895,527.0 7195.0,527.0 7195.0,702.0" fill="none" stroke="currentColor"/>
    <text dy="1.25em" style="font-size: 0.8em; letter-spacing: 1px">
        <textPath xlink:href="#arrow-711a6b156bc64d97b55e852c621c77aa-0-40" class="displacy-label" startOffset="50%" side="left" fill="currentColor" text-anchor="middle">advmod</textPath>
    </text>
    <path class="displacy-arrowhead" d="M7195.0,704.0 L7203.0,692.0 7187.0,692.0" fill="currentColor"/>
</g>
</svg>
</figure>
</body>
</html></span>


    
    Using the 'dep' visualizer
    Serving on http://0.0.0.0:5000 ...
    
    Shutting down server on port 5000.


Using this mapping, we can see each of the clauses of the sentence, and how words within the sentence relate to one another. The mapping can help us to understand whether or not we have correctly identified parts of speech that are associated with the topics we are trying to uncover in our code.


## Sentiment Analysis

My personal favorite part of NLP, sentiment analysis is a very powerful instrument for understanding text and creating actionable items. Many firms use sentiment analysis in combination with their social media accounts to measure engagement and understand how successful marketing campaigns or other interactions are with target audiences.

In order to conduct sentiment analysis using spacy, we are going to use a library called `spacytextblob`. This library includes supplemental material that expands the english corpus' ability to process our data. When utilized, `spacytextblob` is going to add sentiment analysis models to the general pipeline created through `spacy`. We can install the library with the following command:


```python
! pip install pip install spacytextblob
# Note: only use the `!` characters if installing from inside of jupyter notebook or other python interpreter (not when installing from shell/command prompt)
```

    Requirement already satisfied: pip in /opt/conda/lib/python3.7/site-packages (21.0.1)
    Collecting install
      Downloading install-1.3.5-py3-none-any.whl (3.2 kB)
    Collecting spacytextblob
      Downloading spacytextblob-4.0.0-py3-none-any.whl (4.5 kB)
    Collecting textblob<0.16.0,>=0.15.3
      Downloading textblob-0.15.3-py2.py3-none-any.whl (636 kB)
    [K     |████████████████████████████████| 636 kB 4.8 MB/s eta 0:00:01
    [?25hRequirement already satisfied: spacy<4.0,>=3.0 in /opt/conda/lib/python3.7/site-packages (from spacytextblob) (3.2.3)
    Requirement already satisfied: typer<0.5.0,>=0.3.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (0.4.0)
    Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (3.0.6)
    Requirement already satisfied: packaging>=20.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (20.9)
    Requirement already satisfied: wasabi<1.1.0,>=0.8.1 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (0.9.0)
    Requirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (2.23.0)
    Requirement already satisfied: pathy>=0.3.5 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (0.6.1)
    Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (1.8.2)
    Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (3.3.0)
    Requirement already satisfied: typing-extensions<4.0.0.0,>=3.7.4 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (3.7.4.3)
    Requirement already satisfied: setuptools in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (42.0.2.post20191201)
    Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (4.40.0)
    Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (1.0.6)
    Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (2.0.6)
    Requirement already satisfied: thinc<8.1.0,>=8.0.12 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (8.0.14)
    Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (1.0.1)
    Requirement already satisfied: numpy>=1.15.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (1.18.5)
    Requirement already satisfied: jinja2 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (2.10.3)
    Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.8 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (3.0.9)
    Requirement already satisfied: srsly<3.0.0,>=2.4.1 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (2.4.2)
    Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (2.0.6)
    Requirement already satisfied: blis<0.8.0,>=0.4.0 in /opt/conda/lib/python3.7/site-packages (from spacy<4.0,>=3.0->spacytextblob) (0.7.6)
    Requirement already satisfied: zipp>=0.5 in /opt/conda/lib/python3.7/site-packages (from catalogue<2.1.0,>=2.0.6->spacy<4.0,>=3.0->spacytextblob) (0.6.0)
    Requirement already satisfied: pyparsing>=2.0.2 in /opt/conda/lib/python3.7/site-packages (from packaging>=20.0->spacy<4.0,>=3.0->spacytextblob) (2.4.7)
    Requirement already satisfied: smart-open<6.0.0,>=5.0.0 in /opt/conda/lib/python3.7/site-packages (from pathy>=0.3.5->spacy<4.0,>=3.0->spacytextblob) (5.2.1)
    Requirement already satisfied: chardet<4,>=3.0.2 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0,>=3.0->spacytextblob) (3.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0,>=3.0->spacytextblob) (2019.11.28)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0,>=3.0->spacytextblob) (1.25.11)
    Requirement already satisfied: idna<3,>=2.5 in /opt/conda/lib/python3.7/site-packages (from requests<3.0.0,>=2.13.0->spacy<4.0,>=3.0->spacytextblob) (2.8)
    Requirement already satisfied: nltk>=3.1 in /opt/conda/lib/python3.7/site-packages (from textblob<0.16.0,>=0.15.3->spacytextblob) (3.4.1)
    Requirement already satisfied: six in /opt/conda/lib/python3.7/site-packages (from nltk>=3.1->textblob<0.16.0,>=0.15.3->spacytextblob) (1.13.0)
    Requirement already satisfied: click<9.0.0,>=7.1.1 in /opt/conda/lib/python3.7/site-packages (from typer<0.5.0,>=0.3.0->spacy<4.0,>=3.0->spacytextblob) (8.0.4)
    Requirement already satisfied: importlib-metadata in /opt/conda/lib/python3.7/site-packages (from click<9.0.0,>=7.1.1->typer<0.5.0,>=0.3.0->spacy<4.0,>=3.0->spacytextblob) (1.2.0)
    Requirement already satisfied: more-itertools in /opt/conda/lib/python3.7/site-packages (from zipp>=0.5->catalogue<2.1.0,>=2.0.6->spacy<4.0,>=3.0->spacytextblob) (8.0.2)
    Requirement already satisfied: MarkupSafe>=0.23 in /opt/conda/lib/python3.7/site-packages (from jinja2->spacy<4.0,>=3.0->spacytextblob) (1.1.1)
    Installing collected packages: textblob, spacytextblob, install
    Successfully installed install-1.3.5 spacytextblob-4.0.0 textblob-0.15.3
    [33mWARNING: You are using pip version 21.0.1; however, version 22.0.4 is available.
    You should consider upgrading via the '/opt/conda/bin/python3 -m pip install --upgrade pip' command.[0m


Next, we can incorporate the `SpacyTextBlob` process into our pipeline:


```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import requests

jane = requests.get(
"https://github.com/dustywhite7/Econ8320/raw/master/AssignmentData/janeEyreCh1to3.txt"
).text

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

blob = nlp(jane)

sents = [i for i in blob.sents]

for sentence in sents[:10]:
    print("Polarity: {0:3.2f}, Subjectivity: {1:3.2f}".format(sentence._.polarity, sentence._.subjectivity))
```

    Polarity: 0.00, Subjectivity: 0.00
    Polarity: -0.17, Subjectivity: 0.60
    Polarity: -0.30, Subjectivity: 0.69
    Polarity: 0.13, Subjectivity: 0.67
    Polarity: 0.41, Subjectivity: 0.66
    Polarity: 0.00, Subjectivity: 0.00
    Polarity: 0.00, Subjectivity: 0.00
    Polarity: 0.00, Subjectivity: 0.00
    Polarity: 0.37, Subjectivity: 0.53
    Polarity: 0.00, Subjectivity: 0.00


We can add code to our processing pipeline using the `nlp.add_pipe()` method on our `nlp` object. In this case, we are adding the sentiment analysis information created through `SpacyTextBlob`, but this can be literally anything. We can create any kind of function that we want to implement on our code, and can add that functionality to our pipeline in the same way. More examples are available in the `spacy` [documentation](https://spacy.io/usage/processing-pipelines#pipelines).

If you want to get more in-depth with NLP, I highly recommend that you explore the course material available through `spacy`'s own NLP curriculum (freely available!): https://course.spacy.io/en/

## Solve it!

In this project, you will use the text from chapters 44 and 45 of *Pride and Prejudice*. Please find the following information:

- The number of sentences (store as `int` in a variable named `sentences`)
- A list of all proper nouns used across the two chapters (stored as strings in the `names` variable)
- A DataFrame containing a count of the top 20 adjectives used in the text (stored in the `adjectives` variable)
    - Be sure to make all words lower case ONLY!
- A bar chart of the top 20 adjectives used in the text
    - Put this into the second graded cell
    
#### Note: Because SpaCy is not installed on the grading machines, I will have to grade this assignment manually. Thus, you will not be able to get feedback on multiple submissions. I will still be happy to provide feedback on Slack!

### NLP Code here $\downarrow$$\downarrow$$\downarrow$

