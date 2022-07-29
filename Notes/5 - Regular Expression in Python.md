# Regular Expression: Analyzing Text in Python

## What is Regular Expression?

Working with text is HARD. Do we consider "dog" to be different from "dogs"? How do we explain to a computer if we want those words to be considered the same word? In written language, most rules are not really rules, but patterns within text. Regular expression is a paradigm for describing patterns in text in order to accomodate the flexibility of written language and our attempts to find information within larger bodies of text.

For example, I might want to find a series of keywords within a body of text in order to determine whether or not the topic of the text has been correctly identified (or even in order to determine what the topic of the text actually is!). Regular expression has the ability to help express patterns in text that we may want to examine, and the flexibility to determine exactly how we want to capture it. Some common uses of regular expression:

- Validating emails, phone numbers, addresses, and other text blocks
- Finding subsets of a document
- Determining the presence or count of particular words, phrases or patterns
- Web Scraping
- Grammar suggestions

There are, of course many more ways to use regular expression. Let's start looking at how we can use it in our personal data analysis.

## Basics of Regular Expression

Remember, regular expression is way to describe patterns. Below, we will explore how to create various kinds of patterns. To get started, we need to import our regular expression library, called `re`. We can import `re` just like any other library by including the following line of code:

```python
import re
```

The first function that we will utilize is `re.search`. This function will allow us to search through a string of text in order to try and find patterns of interest. Let's begin by importing some text. We will utilize two chapters (44 and 45) from the Jane Austen novel "Pride and Prejudice" (one of my favorites). Below is the code to import these chapters as a (very long) string:


```python
import requests
url = "https://raw.githubusercontent.com/dustywhite7/pythonMikkeli/master/exampleData/prideAndPrejudiceChapters.txt"
document = requests.get(url).text

print(document)
```

    Chapter 44
    
    
    Elizabeth had settled it that Mr. Darcy would bring his sister to visit
    her the very day after her reaching Pemberley; and was consequently
    resolved not to be out of sight of the inn the whole of that morning.
    But her conclusion was false; for on the very morning after their
    arrival at Lambton, these visitors came. They had been walking about the
    place with some of their new friends, and were just returning to the inn
    to dress themselves for dining with the same family, when the sound of a
    carriage drew them to a window, and they saw a gentleman and a lady in
    a curricle driving up the street. Elizabeth immediately recognizing
    the livery, guessed what it meant, and imparted no small degree of her
    surprise to her relations by acquainting them with the honour which she
    expected. Her uncle and aunt were all amazement; and the embarrassment
    of her manner as she spoke, joined to the circumstance itself, and many
    of the circumstances of the preceding day, opened to them a new idea on
    the business. Nothing had ever suggested it before, but they felt that
    there was no other way of accounting for such attentions from such a
    quarter than by supposing a partiality for their niece. While these
    newly-born notions were passing in their heads, the perturbation of
    Elizabeth's feelings was at every moment increasing. She was quite
    amazed at her own discomposure; but amongst other causes of disquiet,
    she dreaded lest the partiality of the brother should have said too much
    in her favour; and, more than commonly anxious to please, she naturally
    suspected that every power of pleasing would fail her.
    
    She retreated from the window, fearful of being seen; and as she walked
    up and down the room, endeavouring to compose herself, saw such looks of
    inquiring surprise in her uncle and aunt as made everything worse.
    
    Miss Darcy and her brother appeared, and this formidable introduction
    took place. With astonishment did Elizabeth see that her new
    acquaintance was at least as much embarrassed as herself. Since her
    being at Lambton, she had heard that Miss Darcy was exceedingly proud;
    but the observation of a very few minutes convinced her that she was
    only exceedingly shy. She found it difficult to obtain even a word from
    her beyond a monosyllable.
    
    Miss Darcy was tall, and on a larger scale than Elizabeth; and, though
    little more than sixteen, her figure was formed, and her appearance
    womanly and graceful. She was less handsome than her brother; but there
    was sense and good humour in her face, and her manners were perfectly
    unassuming and gentle. Elizabeth, who had expected to find in her as
    acute and unembarrassed an observer as ever Mr. Darcy had been, was much
    relieved by discerning such different feelings.
    
    They had not long been together before Mr. Darcy told her that Bingley
    was also coming to wait on her; and she had barely time to express her
    satisfaction, and prepare for such a visitor, when Bingley's quick
    step was heard on the stairs, and in a moment he entered the room. All
    Elizabeth's anger against him had been long done away; but had she still
    felt any, it could hardly have stood its ground against the unaffected
    cordiality with which he expressed himself on seeing her again. He
    inquired in a friendly, though general way, after her family, and looked
    and spoke with the same good-humoured ease that he had ever done.
    
    To Mr. and Mrs. Gardiner he was scarcely a less interesting personage
    than to herself. They had long wished to see him. The whole party before
    them, indeed, excited a lively attention. The suspicions which had just
    arisen of Mr. Darcy and their niece directed their observation towards
    each with an earnest though guarded inquiry; and they soon drew from
    those inquiries the full conviction that one of them at least knew
    what it was to love. Of the lady's sensations they remained a little
    in doubt; but that the gentleman was overflowing with admiration was
    evident enough.
    
    Elizabeth, on her side, had much to do. She wanted to ascertain the
    feelings of each of her visitors; she wanted to compose her own, and
    to make herself agreeable to all; and in the latter object, where she
    feared most to fail, she was most sure of success, for those to whom she
    endeavoured to give pleasure were prepossessed in her favour. Bingley
    was ready, Georgiana was eager, and Darcy determined, to be pleased.
    
    In seeing Bingley, her thoughts naturally flew to her sister; and, oh!
    how ardently did she long to know whether any of his were directed in
    a like manner. Sometimes she could fancy that he talked less than on
    former occasions, and once or twice pleased herself with the notion
    that, as he looked at her, he was trying to trace a resemblance. But,
    though this might be imaginary, she could not be deceived as to his
    behaviour to Miss Darcy, who had been set up as a rival to Jane. No look
    appeared on either side that spoke particular regard. Nothing occurred
    between them that could justify the hopes of his sister. On this point
    she was soon satisfied; and two or three little circumstances occurred
    ere they parted, which, in her anxious interpretation, denoted a
    recollection of Jane not untinctured by tenderness, and a wish of saying
    more that might lead to the mention of her, had he dared. He observed
    to her, at a moment when the others were talking together, and in a tone
    which had something of real regret, that it “was a very long time since
    he had had the pleasure of seeing her;” and, before she could reply,
    he added, “It is above eight months. We have not met since the 26th of
    November, when we were all dancing together at Netherfield.”
    
    Elizabeth was pleased to find his memory so exact; and he afterwards
    took occasion to ask her, when unattended to by any of the rest, whether
    _all_ her sisters were at Longbourn. There was not much in the question,
    nor in the preceding remark; but there was a look and a manner which
    gave them meaning.
    
    It was not often that she could turn her eyes on Mr. Darcy himself;
    but, whenever she did catch a glimpse, she saw an expression of general
    complaisance, and in all that he said she heard an accent so removed
    from _hauteur_ or disdain of his companions, as convinced her that
    the improvement of manners which she had yesterday witnessed however
    temporary its existence might prove, had at least outlived one day. When
    she saw him thus seeking the acquaintance and courting the good opinion
    of people with whom any intercourse a few months ago would have been a
    disgrace--when she saw him thus civil, not only to herself, but to the
    very relations whom he had openly disdained, and recollected their last
    lively scene in Hunsford Parsonage--the difference, the change was
    so great, and struck so forcibly on her mind, that she could hardly
    restrain her astonishment from being visible. Never, even in the company
    of his dear friends at Netherfield, or his dignified relations
    at Rosings, had she seen him so desirous to please, so free from
    self-consequence or unbending reserve, as now, when no importance
    could result from the success of his endeavours, and when even the
    acquaintance of those to whom his attentions were addressed would draw
    down the ridicule and censure of the ladies both of Netherfield and
    Rosings.
    
    Their visitors stayed with them above half-an-hour; and when they arose
    to depart, Mr. Darcy called on his sister to join him in expressing
    their wish of seeing Mr. and Mrs. Gardiner, and Miss Bennet, to dinner
    at Pemberley, before they left the country. Miss Darcy, though with a
    diffidence which marked her little in the habit of giving invitations,
    readily obeyed. Mrs. Gardiner looked at her niece, desirous of knowing
    how _she_, whom the invitation most concerned, felt disposed as to its
    acceptance, but Elizabeth had turned away her head. Presuming however,
    that this studied avoidance spoke rather a momentary embarrassment than
    any dislike of the proposal, and seeing in her husband, who was fond of
    society, a perfect willingness to accept it, she ventured to engage for
    her attendance, and the day after the next was fixed on.
    
    Bingley expressed great pleasure in the certainty of seeing Elizabeth
    again, having still a great deal to say to her, and many inquiries to
    make after all their Hertfordshire friends. Elizabeth, construing all
    this into a wish of hearing her speak of her sister, was pleased, and on
    this account, as well as some others, found herself, when their
    visitors left them, capable of considering the last half-hour with some
    satisfaction, though while it was passing, the enjoyment of it had been
    little. Eager to be alone, and fearful of inquiries or hints from her
    uncle and aunt, she stayed with them only long enough to hear their
    favourable opinion of Bingley, and then hurried away to dress.
    
    But she had no reason to fear Mr. and Mrs. Gardiner's curiosity; it was
    not their wish to force her communication. It was evident that she was
    much better acquainted with Mr. Darcy than they had before any idea of;
    it was evident that he was very much in love with her. They saw much to
    interest, but nothing to justify inquiry.
    
    Of Mr. Darcy it was now a matter of anxiety to think well; and, as far
    as their acquaintance reached, there was no fault to find. They could
    not be untouched by his politeness; and had they drawn his character
    from their own feelings and his servant's report, without any reference
    to any other account, the circle in Hertfordshire to which he was known
    would not have recognized it for Mr. Darcy. There was now an interest,
    however, in believing the housekeeper; and they soon became sensible
    that the authority of a servant who had known him since he was four
    years old, and whose own manners indicated respectability, was not to be
    hastily rejected. Neither had anything occurred in the intelligence of
    their Lambton friends that could materially lessen its weight. They had
    nothing to accuse him of but pride; pride he probably had, and if not,
    it would certainly be imputed by the inhabitants of a small market-town
    where the family did not visit. It was acknowledged, however, that he
    was a liberal man, and did much good among the poor.
    
    With respect to Wickham, the travellers soon found that he was not held
    there in much estimation; for though the chief of his concerns with the
    son of his patron were imperfectly understood, it was yet a well-known
    fact that, on his quitting Derbyshire, he had left many debts behind
    him, which Mr. Darcy afterwards discharged.
    
    As for Elizabeth, her thoughts were at Pemberley this evening more than
    the last; and the evening, though as it passed it seemed long, was not
    long enough to determine her feelings towards _one_ in that mansion;
    and she lay awake two whole hours endeavouring to make them out. She
    certainly did not hate him. No; hatred had vanished long ago, and she
    had almost as long been ashamed of ever feeling a dislike against him,
    that could be so called. The respect created by the conviction of his
    valuable qualities, though at first unwillingly admitted, had for some
    time ceased to be repugnant to her feeling; and it was now heightened
    into somewhat of a friendlier nature, by the testimony so highly in
    his favour, and bringing forward his disposition in so amiable a light,
    which yesterday had produced. But above all, above respect and esteem,
    there was a motive within her of goodwill which could not be overlooked.
    It was gratitude; gratitude, not merely for having once loved her,
    but for loving her still well enough to forgive all the petulance and
    acrimony of her manner in rejecting him, and all the unjust accusations
    accompanying her rejection. He who, she had been persuaded, would avoid
    her as his greatest enemy, seemed, on this accidental meeting, most
    eager to preserve the acquaintance, and without any indelicate display
    of regard, or any peculiarity of manner, where their two selves only
    were concerned, was soliciting the good opinion of her friends, and bent
    on making her known to his sister. Such a change in a man of so much
    pride exciting not only astonishment but gratitude--for to love, ardent
    love, it must be attributed; and as such its impression on her was of a
    sort to be encouraged, as by no means unpleasing, though it could not be
    exactly defined. She respected, she esteemed, she was grateful to him,
    she felt a real interest in his welfare; and she only wanted to know how
    far she wished that welfare to depend upon herself, and how far it would
    be for the happiness of both that she should employ the power, which her
    fancy told her she still possessed, of bringing on her the renewal of
    his addresses.
    
    It had been settled in the evening between the aunt and the niece, that
    such a striking civility as Miss Darcy's in coming to see them on the
    very day of her arrival at Pemberley, for she had reached it only to a
    late breakfast, ought to be imitated, though it could not be equalled,
    by some exertion of politeness on their side; and, consequently, that
    it would be highly expedient to wait on her at Pemberley the following
    morning. They were, therefore, to go. Elizabeth was pleased; though when
    she asked herself the reason, she had very little to say in reply.
    
    Mr. Gardiner left them soon after breakfast. The fishing scheme had been
    renewed the day before, and a positive engagement made of his meeting
    some of the gentlemen at Pemberley before noon.
    
    
    
    Chapter 45
    
    
    Convinced as Elizabeth now was that Miss Bingley's dislike of her had
    originated in jealousy, she could not help feeling how unwelcome her
    appearance at Pemberley must be to her, and was curious to know with how
    much civility on that lady's side the acquaintance would now be renewed.
    
    On reaching the house, they were shown through the hall into the saloon,
    whose northern aspect rendered it delightful for summer. Its windows
    opening to the ground, admitted a most refreshing view of the high woody
    hills behind the house, and of the beautiful oaks and Spanish chestnuts
    which were scattered over the intermediate lawn.
    
    In this house they were received by Miss Darcy, who was sitting there
    with Mrs. Hurst and Miss Bingley, and the lady with whom she lived in
    London. Georgiana's reception of them was very civil, but attended with
    all the embarrassment which, though proceeding from shyness and the fear
    of doing wrong, would easily give to those who felt themselves inferior
    the belief of her being proud and reserved. Mrs. Gardiner and her niece,
    however, did her justice, and pitied her.
    
    By Mrs. Hurst and Miss Bingley they were noticed only by a curtsey; and,
    on their being seated, a pause, awkward as such pauses must always be,
    succeeded for a few moments. It was first broken by Mrs. Annesley, a
    genteel, agreeable-looking woman, whose endeavour to introduce some kind
    of discourse proved her to be more truly well-bred than either of the
    others; and between her and Mrs. Gardiner, with occasional help from
    Elizabeth, the conversation was carried on. Miss Darcy looked as if she
    wished for courage enough to join in it; and sometimes did venture a
    short sentence when there was least danger of its being heard.
    
    Elizabeth soon saw that she was herself closely watched by Miss Bingley,
    and that she could not speak a word, especially to Miss Darcy, without
    calling her attention. This observation would not have prevented her
    from trying to talk to the latter, had they not been seated at an
    inconvenient distance; but she was not sorry to be spared the necessity
    of saying much. Her own thoughts were employing her. She expected every
    moment that some of the gentlemen would enter the room. She wished, she
    feared that the master of the house might be amongst them; and whether
    she wished or feared it most, she could scarcely determine. After
    sitting in this manner a quarter of an hour without hearing Miss
    Bingley's voice, Elizabeth was roused by receiving from her a cold
    inquiry after the health of her family. She answered with equal
    indifference and brevity, and the other said no more.
    
    The next variation which their visit afforded was produced by the
    entrance of servants with cold meat, cake, and a variety of all the
    finest fruits in season; but this did not take place till after many
    a significant look and smile from Mrs. Annesley to Miss Darcy had been
    given, to remind her of her post. There was now employment for the whole
    party--for though they could not all talk, they could all eat; and the
    beautiful pyramids of grapes, nectarines, and peaches soon collected
    them round the table.
    
    While thus engaged, Elizabeth had a fair opportunity of deciding whether
    she most feared or wished for the appearance of Mr. Darcy, by the
    feelings which prevailed on his entering the room; and then, though but
    a moment before she had believed her wishes to predominate, she began to
    regret that he came.
    
    He had been some time with Mr. Gardiner, who, with two or three other
    gentlemen from the house, was engaged by the river, and had left him
    only on learning that the ladies of the family intended a visit to
    Georgiana that morning. No sooner did he appear than Elizabeth wisely
    resolved to be perfectly easy and unembarrassed; a resolution the more
    necessary to be made, but perhaps not the more easily kept, because she
    saw that the suspicions of the whole party were awakened against them,
    and that there was scarcely an eye which did not watch his behaviour
    when he first came into the room. In no countenance was attentive
    curiosity so strongly marked as in Miss Bingley's, in spite of the
    smiles which overspread her face whenever she spoke to one of its
    objects; for jealousy had not yet made her desperate, and her attentions
    to Mr. Darcy were by no means over. Miss Darcy, on her brother's
    entrance, exerted herself much more to talk, and Elizabeth saw that he
    was anxious for his sister and herself to get acquainted, and forwarded
    as much as possible, every attempt at conversation on either side. Miss
    Bingley saw all this likewise; and, in the imprudence of anger, took the
    first opportunity of saying, with sneering civility:
    
    “Pray, Miss Eliza, are not the ----shire Militia removed from Meryton?
    They must be a great loss to _your_ family.”
    
    In Darcy's presence she dared not mention Wickham's name; but Elizabeth
    instantly comprehended that he was uppermost in her thoughts; and the
    various recollections connected with him gave her a moment's distress;
    but exerting herself vigorously to repel the ill-natured attack, she
    presently answered the question in a tolerably detached tone. While
    she spoke, an involuntary glance showed her Darcy, with a heightened
    complexion, earnestly looking at her, and his sister overcome with
    confusion, and unable to lift up her eyes. Had Miss Bingley known what
    pain she was then giving her beloved friend, she undoubtedly would
    have refrained from the hint; but she had merely intended to discompose
    Elizabeth by bringing forward the idea of a man to whom she believed
    her partial, to make her betray a sensibility which might injure her in
    Darcy's opinion, and, perhaps, to remind the latter of all the follies
    and absurdities by which some part of her family were connected
    with that corps. Not a syllable had ever reached her of Miss Darcy's
    meditated elopement. To no creature had it been revealed, where secrecy
    was possible, except to Elizabeth; and from all Bingley's connections
    her brother was particularly anxious to conceal it, from the very
    wish which Elizabeth had long ago attributed to him, of their becoming
    hereafter her own. He had certainly formed such a plan, and without
    meaning that it should affect his endeavour to separate him from Miss
    Bennet, it is probable that it might add something to his lively concern
    for the welfare of his friend.
    
    Elizabeth's collected behaviour, however, soon quieted his emotion; and
    as Miss Bingley, vexed and disappointed, dared not approach nearer to
    Wickham, Georgiana also recovered in time, though not enough to be able
    to speak any more. Her brother, whose eye she feared to meet, scarcely
    recollected her interest in the affair, and the very circumstance which
    had been designed to turn his thoughts from Elizabeth seemed to have
    fixed them on her more and more cheerfully.
    
    Their visit did not continue long after the question and answer above
    mentioned; and while Mr. Darcy was attending them to their carriage Miss
    Bingley was venting her feelings in criticisms on Elizabeth's person,
    behaviour, and dress. But Georgiana would not join her. Her brother's
    recommendation was enough to ensure her favour; his judgement could not
    err. And he had spoken in such terms of Elizabeth as to leave Georgiana
    without the power of finding her otherwise than lovely and amiable. When
    Darcy returned to the saloon, Miss Bingley could not help repeating to
    him some part of what she had been saying to his sister.
    
    “How very ill Miss Eliza Bennet looks this morning, Mr. Darcy,” she
    cried; “I never in my life saw anyone so much altered as she is since
    the winter. She is grown so brown and coarse! Louisa and I were agreeing
    that we should not have known her again.”
    
    However little Mr. Darcy might have liked such an address, he contented
    himself with coolly replying that he perceived no other alteration than
    her being rather tanned, no miraculous consequence of travelling in the
    summer.
    
    “For my own part,” she rejoined, “I must confess that I never could
    see any beauty in her. Her face is too thin; her complexion has no
    brilliancy; and her features are not at all handsome. Her nose
    wants character--there is nothing marked in its lines. Her teeth are
    tolerable, but not out of the common way; and as for her eyes,
    which have sometimes been called so fine, I could never see anything
    extraordinary in them. They have a sharp, shrewish look, which I do
    not like at all; and in her air altogether there is a self-sufficiency
    without fashion, which is intolerable.”
    
    Persuaded as Miss Bingley was that Darcy admired Elizabeth, this was not
    the best method of recommending herself; but angry people are not always
    wise; and in seeing him at last look somewhat nettled, she had all the
    success she expected. He was resolutely silent, however, and, from a
    determination of making him speak, she continued:
    
    “I remember, when we first knew her in Hertfordshire, how amazed we all
    were to find that she was a reputed beauty; and I particularly recollect
    your saying one night, after they had been dining at Netherfield, '_She_
    a beauty!--I should as soon call her mother a wit.' But afterwards she
    seemed to improve on you, and I believe you thought her rather pretty at
    one time.”
    
    “Yes,” replied Darcy, who could contain himself no longer, “but _that_
    was only when I first saw her, for it is many months since I have
    considered her as one of the handsomest women of my acquaintance.”
    
    He then went away, and Miss Bingley was left to all the satisfaction of
    having forced him to say what gave no one any pain but herself.
    
    Mrs. Gardiner and Elizabeth talked of all that had occurred during their
    visit, as they returned, except what had particularly interested them
    both. The look and behaviour of everybody they had seen were discussed,
    except of the person who had mostly engaged their attention. They talked
    of his sister, his friends, his house, his fruit--of everything but
    himself; yet Elizabeth was longing to know what Mrs. Gardiner thought of
    him, and Mrs. Gardiner would have been highly gratified by her niece's
    beginning the subject.
    
    


### Finding text

Now that we have our text imported, we can begin to explore it. We will start by looking for the word "Elizabeth" (she is the main character of the novel, and is also sometimes called "Lizzy" or "Eliza"). In order to look for the word "Elizabeth", we will use the `re.search` function mentioned earlier. This function takes two arguments: a regular expression, and a string in which to search for matches to that pattern. Regular expression patterns will be stored as strings, as well, but we will use **raw strings**. To create a raw string, we prepend the string with a single letter `r`, so that our string looks something like this: `r''`. 

By using raw strings, we allow ourselves to use escape characters (character sequences beginning with `\` such as `\n` or `\r`) within our string to describe possible patterns that we would like to match.

Once we have created our regular expression pattern, we can call the `re.search` function. It will look for the first match to your pattern. Here is what happens when we look for a match to "Elizabeth":


```python
import re

re.search(r'Elizabeth', document)
```




    <re.Match object; span=(13, 22), match='Elizabeth'>



This is a successful search! The document does mention Elizabeth, and we see that a match to the expression `r'Elizabeth'` happened. The result of the function is an `re.Match` object, which contains information about where the match was found, as well as the text that matched our stated pattern. When we include a string like `r'Elizabeth'` as our pattern, we are telling regular expression to find a **capital** "E", followed by lower case "l", followed by lower case "i", followed by lower case "z", followed by lower case "a", followed by lower case "b", followed by lower case "e", followed by lower case "t", followed by lower case "h". No other text will match this pattern.

We will often want to be more expressive than this. For example, if we read the document, we can see that some characters mention Elizabeth as Eliza. We can of course search for Eliza separately, or we can try to combine Eliza into our expression pattern, so that we can detect all matches of either Elizabeth or Eliza. To see the difference, we will use the `re.finditer` function to look for all matches to our pattern:


```python
# Number of results for only Elizabeth 
print("Number of results for only Elizabeth")
print(len([i for i in re.finditer(r'Elizabeth', document)]))

# Number of results for Elizabeth OR Eliza
print("Number of results for only Elizabeth OR Eliza")
print(len([i for i in re.finditer(r'Eliza(beth)?', document)]))
```

    Number of results for only Elizabeth
    32
    Number of results for only Elizabeth OR Eliza
    34


What did we just do? A couple things. First, we used the `re.finditer` function, which generates an **iterable**. In order to get back all of our results, we need to create a list by iterating over the results. We used a list comprehension to do that. (Remember that list comprehensions are statements like `[i for i in some_iterable]`). At that point, we had a list of results. We then checked the length of the list for each of two different regular expressions. One for just Elizabeth, and one for Eliza/Elizabeth. 

Now let's break down the difference in the regular expressions. There are two differences between our first and second expressions. First, we used `()` to encapsulate a portion of the word Elizabeth that may not be present in some cases. Parens (`()`) create **groups** in regular expression. Sometimes we will want to capture groups from within an expression, and other times we will only want to indicate that a group may or may not be present. In this case, we indicate that the sequence `beth` is not strictly required for a match by using a `?` character after the group. This doesn't mean that our text needs to include a `?`. The `?` symbol says "I want either 1 or 0 matches to the "beth" sequence.

In other words, "beth" may be present (have one match) or not present (have zero matches) while still allowing us to have a successful match to our regular expression pattern. There are several similar expressions:

| Symbol | Meaning |
| --- | :---: |
| `?` | 1 or 0 repetitions|
| `+` | 1 or more repetitions | 
| `*` | 0 or more repetitions |
|`{n}` | exactly `n` repetitions|
|`{m,n}` | between `m` and `n` repetitions|

We can use these expressions with groups, or with single characters. What if we wanted to find the end of sentences in our text? Let's try and express that:


```python
[i for i in re.finditer(r'[.?!][ ]*', document)]
```




    [<re.Match object; span=(45, 47), match='. '>,
     <re.Match object; span=(221, 222), match='.'>,
     <re.Match object; span=(328, 330), match='. '>,
     <re.Match object; span=(611, 613), match='. '>,
     <re.Match object; span=(798, 800), match='. '>,
     <re.Match object; span=(1017, 1019), match='. '>,
     <re.Match object; span=(1199, 1201), match='. '>,
     <re.Match object; span=(1332, 1334), match='. '>,
     <re.Match object; span=(1616, 1617), match='.'>,
     <re.Match object; span=(1829, 1830), match='.'>,
     <re.Match object; span=(1912, 1914), match='. '>,
     <re.Match object; span=(2019, 2021), match='. '>,
     <re.Match object; span=(2191, 2193), match='. '>,
     <re.Match object; span=(2268, 2269), match='.'>,
     <re.Match object; span=(2430, 2432), match='. '>,
     <re.Match object; span=(2573, 2575), match='. '>,
     <re.Match object; span=(2667, 2669), match='. '>,
     <re.Match object; span=(2740, 2741), match='.'>,
     <re.Match object; span=(2784, 2786), match='. '>,
     <re.Match object; span=(3017, 3019), match='. '>,
     <re.Match object; span=(3229, 3231), match='. '>,
     <re.Match object; span=(3371, 3372), match='.'>,
     <re.Match object; span=(3379, 3381), match='. '>,
     <re.Match object; span=(3388, 3390), match='. '>,
     <re.Match object; span=(3459, 3461), match='. '>,
     <re.Match object; span=(3492, 3494), match='. '>,
     <re.Match object; span=(3557, 3559), match='. '>,
     <re.Match object; span=(3601, 3603), match='. '>,
     <re.Match object; span=(3815, 3817), match='. '>,
     <re.Match object; span=(3948, 3949), match='.'>,
     <re.Match object; span=(3989, 3991), match='. '>,
     <re.Match object; span=(4291, 4293), match='. '>,
     <re.Match object; span=(4368, 4369), match='.'>,
     <re.Match object; span=(4440, 4441), match='!'>,
     <re.Match object; span=(4525, 4527), match='. '>,
     <re.Match object; span=(4712, 4714), match='. '>,
     <re.Match object; span=(4850, 4852), match='. '>,
     <re.Match object; span=(4912, 4914), match='. '>,
     <re.Match object; span=(4986, 4988), match='. '>,
     <re.Match object; span=(5267, 5269), match='. '>,
     <re.Match object; span=(5530, 5532), match='. '>,
     <re.Match object; span=(5624, 5625), match='.'>,
     <re.Match object; span=(5805, 5807), match='. '>,
     <re.Match object; span=(5929, 5930), match='.'>,
     <re.Match object; span=(5983, 5985), match='. '>,
     <re.Match object; span=(6343, 6345), match='. '>,
     <re.Match object; span=(6815, 6817), match='. '>,
     <re.Match object; span=(7251, 7252), match='.'>,
     <re.Match object; span=(7339, 7341), match='. '>,
     <re.Match object; span=(7417, 7419), match='. '>,
     <re.Match object; span=(7426, 7428), match='. '>,
     <re.Match object; span=(7507, 7509), match='. '>,
     <re.Match object; span=(7620, 7622), match='. '>,
     <re.Match object; span=(7625, 7627), match='. '>,
     <re.Match object; span=(7798, 7800), match='. '>,
     <re.Match object; span=(8090, 8091), match='.'>,
     <re.Match object; span=(8275, 8277), match='. '>,
     <re.Match object; span=(8590, 8592), match='. '>,
     <re.Match object; span=(8783, 8784), match='.'>,
     <re.Match object; span=(8818, 8820), match='. '>,
     <re.Match object; span=(8827, 8829), match='. '>,
     <re.Match object; span=(8899, 8901), match='. '>,
     <re.Match object; span=(8959, 8961), match='. '>,
     <re.Match object; span=(9054, 9056), match='. '>,
     <re.Match object; span=(9113, 9114), match='.'>,
     <re.Match object; span=(9121, 9123), match='. '>,
     <re.Match object; span=(9244, 9246), match='. '>,
     <re.Match object; span=(9505, 9507), match='. '>,
     <re.Match object; span=(9512, 9514), match='. '>,
     <re.Match object; span=(9767, 9769), match='. '>,
     <re.Match object; span=(9883, 9885), match='. '>,
     <re.Match object; span=(10067, 10069), match='. '>,
     <re.Match object; span=(10158, 10159), match='.'>,
     <re.Match object; span=(10458, 10460), match='. '>,
     <re.Match object; span=(10487, 10488), match='.'>,
     <re.Match object; span=(10765, 10767), match='. '>,
     <re.Match object; span=(10797, 10799), match='. '>,
     <re.Match object; span=(10935, 10937), match='. '>,
     <re.Match object; span=(11291, 11293), match='. '>,
     <re.Match object; span=(11405, 11406), match='.'>,
     <re.Match object; span=(11642, 11644), match='. '>,
     <re.Match object; span=(12002, 12004), match='. '>,
     <re.Match object; span=(12270, 12272), match='. '>,
     <re.Match object; span=(12628, 12629), match='.'>,
     <re.Match object; span=(13063, 13065), match='. '>,
     <re.Match object; span=(13092, 13094), match='. '>,
     <re.Match object; span=(13194, 13195), match='.'>,
     <re.Match object; span=(13199, 13201), match='. '>,
     <re.Match object; span=(13240, 13242), match='. '>,
     <re.Match object; span=(13386, 13387), match='.'>,
     <re.Match object; span=(13687, 13688), match='.'>,
     <re.Match object; span=(13818, 13820), match='. '>,
     <re.Match object; span=(14024, 14025), match='.'>,
     <re.Match object; span=(14105, 14107), match='. '>,
     <re.Match object; span=(14173, 14175), match='. '>,
     <re.Match object; span=(14426, 14428), match='. '>,
     <re.Match object; span=(14431, 14433), match='. '>,
     <re.Match object; span=(14497, 14498), match='.'>,
     <re.Match object; span=(14506, 14508), match='. '>,
     <re.Match object; span=(14671, 14673), match='. '>,
     <re.Match object; span=(14699, 14701), match='. '>,
     <re.Match object; span=(14887, 14889), match='. '>,
     <re.Match object; span=(14967, 14969), match='. '>,
     <re.Match object; span=(15127, 15128), match='.'>,
     <re.Match object; span=(15295, 15297), match='. '>,
     <re.Match object; span=(15495, 15497), match='. '>,
     <re.Match object; span=(15532, 15534), match='. '>,
     <re.Match object; span=(15607, 15609), match='. '>,
     <re.Match object; span=(15754, 15756), match='. '>,
     <re.Match object; span=(15932, 15934), match='. '>,
     <re.Match object; span=(16010, 16011), match='.'>,
     <re.Match object; span=(16253, 16255), match='. '>,
     <re.Match object; span=(16319, 16321), match='. '>,
     <re.Match object; span=(16520, 16521), match='.'>,
     <re.Match object; span=(16646, 16648), match='. '>,
     <re.Match object; span=(16826, 16827), match='.'>,
     <re.Match object; span=(16858, 16860), match='. '>,
     <re.Match object; span=(17057, 17059), match='. '>,
     <re.Match object; span=(17420, 17422), match='. '>,
     <re.Match object; span=(17665, 17667), match='. '>,
     <re.Match object; span=(17694, 17696), match='. '>,
     <re.Match object; span=(17933, 17935), match='. '>,
     <re.Match object; span=(18136, 18137), match='?'>,
     <re.Match object; span=(18180, 18181), match='.'>,
     <re.Match object; span=(18526, 18528), match='. '>,
     <re.Match object; span=(18711, 18713), match='. '>,
     <re.Match object; span=(19171, 19173), match='. '>,
     <re.Match object; span=(19244, 19246), match='. '>,
     <re.Match object; span=(19521, 19523), match='. '>,
     <re.Match object; span=(19744, 19745), match='.'>,
     <re.Match object; span=(19978, 19980), match='. '>,
     <re.Match object; span=(20215, 20216), match='.'>,
     <re.Match object; span=(20311, 20313), match='. '>,
     <re.Match object; span=(20451, 20453), match='. '>,
     <re.Match object; span=(20485, 20487), match='. '>,
     <re.Match object; span=(20576, 20578), match='. '>,
     <re.Match object; span=(20711, 20713), match='. '>,
     <re.Match object; span=(20844, 20845), match='.'>,
     <re.Match object; span=(20901, 20903), match='. '>,
     <re.Match object; span=(20995, 20997), match='. '>,
     <re.Match object; span=(21029, 21031), match='! '>,
     <re.Match object; span=(21097, 21098), match='.'>,
     <re.Match object; span=(21118, 21120), match='. '>,
     <re.Match object; span=(21323, 21324), match='.'>,
     <re.Match object; span=(21415, 21417), match='. '>,
     <re.Match object; span=(21513, 21515), match='. '>,
     <re.Match object; span=(21577, 21579), match='. '>,
     <re.Match object; span=(21746, 21748), match='. '>,
     <re.Match object; span=(21901, 21902), match='.'>,
     <re.Match object; span=(22142, 22144), match='. '>,
     <re.Match object; span=(22468, 22469), match='!'>,
     <re.Match object; span=(22509, 22510), match='.'>,
     <re.Match object; span=(22612, 22613), match='.'>,
     <re.Match object; span=(22817, 22818), match='.'>,
     <re.Match object; span=(22955, 22956), match='.'>,
     <re.Match object; span=(22961, 22963), match='. '>,
     <re.Match object; span=(23105, 23107), match='. '>,
     <re.Match object; span=(23232, 23234), match='. '>,
     <re.Match object; span=(23365, 23367), match='. '>,
     <re.Match object; span=(23399, 23401), match='. '>,
     <re.Match object; span=(23479, 23480), match='.'>]



This is a good start! We know that sentences can end with "?", "!", or ".", so we create a set of characters that can be matched: `[.?!]`. This expression says that a character can be a period, question mark, or exclamation mark and still match our pattern. We then use a character set including only the space character followed by a star (`[ ]*`) to indicate that there should be 0 or more spaces following each period.

We can use character sets where spelling is uncertain, or where there is a possibility of letters being upper or lower case. Let's look for the word "on", both with and without a character set to accomodate case ambiguity:


```python
# Number of results for "on"
print("Number of results for 'on'")
print(len([i for i in re.finditer(r'on', document)]))

# Number of results for "on" or "On"
print("Number of results for 'on' or 'On'")
print(len([i for i in re.finditer(r'[Oo]n', document)]))
```

    Number of results for 'on'
    219
    Number of results for 'on' or 'On'
    221


If we weren't careful, we would miss some matches to the word we are looking for!

### Finding numbers

We won't always be looking for words. Sometimes, we want to find or validate numbers. In the United States, phone numbers are commonly expressed with a three-digit area code, a hyphen (`-`), and a seven-digit phone number with the first three numbers separated from the final four by another hyphen. Let's try to detect this pattern in text that is provided by the user. Before we get started, let's talk about how we can identify numbers.

When we look for numbers, we typically are not looking for a single specific number (like 42). We are instead looking for **some** number. It might be 2, it might be 142, or it might be 1000. Let's look for a number in the following sentence:


```python
sentence = "My favorite number is 7"

re.search(r'7', sentence)
```




    <re.Match object; span=(22, 23), match='7'>



Okay, we can find an exact number. Can you think of a way that we have discussed above to find **any** single-digit number?

**Solve it (2 points)**:

The user will enter their favorite single-digit number. You need to make sure that there is a number in the sentence. Store the results of your `re.search` function in the variable `hasNumber` in the cell below:




When we want to find a number, we could use character sets: `[0123456789]`. This character set specifies that we will accept any number character as a match to our pattern. If we want to specify that it be a number that has more than one character, we could provide a pattern such as `[0123456789]+`. It will get really old, really fast to keep typing `[0123456789]`. Instead, we can use the shorthand `\d` representation for a **digit** or number. Now, if we want to find a number character, we can just write `\d` in place of `[0123456789]`. For one or more number characters, we write `\d+`.

Now, let's get back to trying to break down phone number validation. Using what we know about digit representation, combined with our knowledge of ways to express repeated patterns from before, we can express a phone number! If we rewrite our goal as words, we would end up with the following:

- Three numbers
- A hyphen
- Three numbers
- A hyphen
- Four numbers

Let's write this as a regular expression:


```python
# Ask user for phone number
myNumber = input("Please enter your phone number: ")

# Check if the phone number is valid
valid = re.search(r'\d{3}-\d{3}-\d{4}', myNumber)

# Print a boolean value indicating whether or not the string contains a valid phone number
print(bool(valid))
```

    Please enter your phone number: 123-456-7890 turtles
    True


Awesome! Try different valid and invalid phone numbers in the cell above to see if they work with our code.

### More general patterns

What other patterns might come in handy? Here is a short table of helpers for making your expressions easier to write:

| Pattern | Meaning | Pattern | Meaning |
| --- | --- | --- | --- |
| `\s` | any whitespace character | `\S` | any non-whitespace character |
| `\d` | any digit character | `\D` | any non-digit character | 
| `\w` | any word character (a number, a letter, or a `_`) | `\W` | non-word characters|
| `\b` | word boundaries (the start or end of a sequence of word characters) ||
| `^` | start of a string | `$` | end of a string

Going back to our phone number exercise, what happens if you provide the string `123-456-7890 turtles` as a phone number? Is it considered valid? **It is!** We can use our new patterns to protect against this:




```python
# Add start and end of string characters
valid = re.search(r'^\d{3}-\d{3}-\d{4}$', "123-456-7890 turtles")

# Print an improved boolean value indicating whether or not the string contains a valid phone number
print(bool(valid))
```

    True


Now we won't be fooled so easily! Our number has to be formatted correctly, AND our string cannot contain any other characters. Play with the code above and check for yourself!

When we think about how to create an expression to validate text or numbers, we should be particularly careful to think of any **possible** ways that a value might be invalid. It is not sufficient to think only of ways in which text is **likely** to be invalid. If we are not careful, our validation will not truly validate, and any work that we do with the "validated" text may be broken by cases we have not accounted for.

### Looking Behind

Speaking of not accounting for all the possibilities, we made this mistake earlier when we were looking for the ends of sentences earlier. We looked for all periods (`.`), question marks (`?`), and exclamation marks (`!`). Unfortunately, not all periods come at the end of sentences! In *Pride and Prejudice*, many characters are referred to as "Mr." or "Mrs.". Those periods are followed by spaces, and so would have counted as the end of a sentence.

#### Negative Lookbehind

In order to solve this problem, we need a new tool: the **negative lookbehind**. A negative lookbehind is a pattern that must be matched while simultaneously NOT being preceded by another pattern. In this case, we would want `[.?!]` wherever that character set is NOT preceded by `Mr` or `Mrs`. First, let's make sure that we can find `Mr` and `Mrs` with a single expression:


```python
[i for i in re.finditer(r'Mrs*', document)]
```




    [<re.Match object; span=(43, 45), match='Mr'>,
     <re.Match object; span=(2665, 2667), match='Mr'>,
     <re.Match object; span=(2782, 2784), match='Mr'>,
     <re.Match object; span=(3377, 3379), match='Mr'>,
     <re.Match object; span=(3385, 3388), match='Mrs'>,
     <re.Match object; span=(3599, 3601), match='Mr'>,
     <re.Match object; span=(5981, 5983), match='Mr'>,
     <re.Match object; span=(7337, 7339), match='Mr'>,
     <re.Match object; span=(7415, 7417), match='Mr'>,
     <re.Match object; span=(7423, 7426), match='Mrs'>,
     <re.Match object; span=(7622, 7625), match='Mrs'>,
     <re.Match object; span=(8816, 8818), match='Mr'>,
     <re.Match object; span=(8824, 8827), match='Mrs'>,
     <re.Match object; span=(8957, 8959), match='Mr'>,
     <re.Match object; span=(9119, 9121), match='Mr'>,
     <re.Match object; span=(9503, 9505), match='Mr'>,
     <re.Match object; span=(10456, 10458), match='Mr'>,
     <re.Match object; span=(13197, 13199), match='Mr'>,
     <re.Match object; span=(14102, 14105), match='Mrs'>,
     <re.Match object; span=(14428, 14431), match='Mrs'>,
     <re.Match object; span=(14503, 14506), match='Mrs'>,
     <re.Match object; span=(14696, 14699), match='Mrs'>,
     <re.Match object; span=(14884, 14887), match='Mrs'>,
     <re.Match object; span=(16250, 16253), match='Mrs'>,
     <re.Match object; span=(16644, 16646), match='Mr'>,
     <re.Match object; span=(16856, 16858), match='Mr'>,
     <re.Match object; span=(17663, 17665), match='Mr'>,
     <re.Match object; span=(20309, 20311), match='Mr'>,
     <re.Match object; span=(20899, 20901), match='Mr'>,
     <re.Match object; span=(21116, 21118), match='Mr'>,
     <re.Match object; span=(22958, 22961), match='Mrs'>,
     <re.Match object; span=(23362, 23365), match='Mrs'>,
     <re.Match object; span=(23396, 23399), match='Mrs'>]



So far, so good! Now that we can find all of the cases that we **don't** want to count as ends of sentences, let's use a negative lookbehind. The expression we want to avoid will be put in a group (between `()`), and we will put the character sequence `?<!` at the start of the group:


```python
# Count of sentences without negative lookbehind (incorrect)
print("Count of sentences without negative lookbehind (incorrect)")
print(len([i for i in re.finditer(r'[.!?]', document)]))

# Count of sentences with negative lookbehind (correct)
print("Count of sentences with negative lookbehind (correct)")
print(len([i for i in re.finditer(r'(?<!Mr)(?<!Mrs)[.!?]', document)]))

```

    Count of sentences without negative lookbehind (incorrect)
    161
    Count of sentences with negative lookbehind (correct)
    128


We have to use **two** negative lookbehinds to solve this problem, because we cannot allow for `Mr` or `Mrs` to precede our punctuation. You might have tried `(?<!Mrs*)` (as I did at first). Unfortunately, we cannot use this structure because we are not permitted to use a negative lookbehind that is of uncertain length (as is any pattern with `*`, `+`, `?`, or `{}`). Instead, we simply check for the first string, then check for the second string.

#### Positive Lookbehind

We can also use a positive lookbehind to **require** that our pattern be preceded by another pattern. For example, we may wish to determine which chapters are covered in a text document (we know it is Chapters 44 and 45, but we can use this as an exercise anyway). A positive lookbehind is indicated within parens (`()`) just like the negative lookbehind, but uses the character sequence `?<=`. Let's try to find numbers that are preceded by the pattern `Chapter `:


```python
[i for i in re.finditer(r'(?<=Chapter )\d+', document)]
```




    [<re.Match object; span=(8, 10), match='44'>,
     <re.Match object; span=(13399, 13401), match='45'>]



Excellent! Just as we know *should* be the case, we can see that we found the beginnings of both chapters 44 and 45.

## Options

When we are creating patterns, we sometimes will encounter multiple acceptable patterns that we wish to account for. With phone numbers, area codes in the United States are often written in parens rather than with hypens. Thus, we might need to account for two patterns:
- `xxx-xxx-xxxx`
- `(xxx) xxx-xxxx`

Let's try to write expressions for the second option (since we can already accomodate the first):


```python
# Ask user for phone number
myNumber = input("Please enter your phone number: ")

# Check if the phone number is valid
valid = re.search(r'^[(]\d{3}[)][ ]\d{3}-\d{4}$', myNumber)

# Print a boolean value indicating whether or not the string contains a valid phone number
print(bool(valid))
```

    Please enter your phone number: (425) 443-1880
    True


Our new rule is written `[(]\d{3}[)][ ]`. There are a lot of square brackets! In order to look for the `()` characters, we have to wrap them in a character set, so that our program knows that they are not there to indicate a group, but are instead literal characters. In between the parens, we have our `\d{3}` three-digit number set. Finally, at the end, we have a single space character `[ ]` that must separate the area code `(xxx)` from the rest of the phone number `xxx-xxxx`.

You can try various inputs to see if the code continues to validate phone numbers correctly. It should work on our new format with parens, but not on our original phone number format. Luckily, now that we have a validity check for both phone number formats, we can incorportate them into a single expression to accept either valid format:


```python
# Ask user for phone number
myNumber = input("Please enter your phone number: ")

# Check if the phone number is valid
valid = re.search(r'^([(]\d{3}[)][ ]|\d{3}-)\d{3}-\d{4}$', myNumber)

# Print a boolean value indicating whether or not the string contains a valid phone number
print(bool(valid))
```

    Please enter your phone number: (123) 456-7890
    True


In this case, we have taken the original area code rule (`\d{3}-`) as well as the new area code rule (`[(]\d{3}[)][ ]`), and we have put them inside of a group using parens `()`. They are separated inside this group by the `|` character. Just like it does in our boolean conditions, the `|` character represents the logical statement "or". Essentially, we are saying that our pattern must match `\d{3}-` OR `[(]\d{3}[)][ ]`, followed by `\d{3}-\d{4}`.

For good measure, we have wrapped the whole expression in string start and end characters (`^` and `$`) in order to disallow any other text in our valid phone numbers.

## Extracting results

When we use the `re.search` or `re.finditer` functions, matches are returned to us through an `re.Match` object. We can extract the text from a match object by using the `.string` attribute. 


```python
valid.string
```




    '(123) 456-7890'



Also useful is the `.span` function of the `re.Match` object, which returns to us the start and end points (within the original string) of the match to our pattern:


```python
valid.span()
```




    (0, 14)



Finally, we also have the ability to transform an `re.Match` object into a `bool`-type object, which is useful in various contexts such as text validation. To evaluate an `re.Match` object, we can simply convert the variable into which it is stored:


```python
bool(valid)
```




    True



If, on the other hand, we fail to find a match to our pattern, our `re.search` or `re.finditer` function will return a `None` object, and it's boolean value will be `False`:


```python
value = re.search(r'happy', "I am sad")

print(value)
print(bool(value))
```

    None
    False


**Solve it (2 points)**:

Write a function called `dateCheck` that will accept a string as an argument to determine whether or not that string contains ONLY a valid date. The date should be of the format DD-MM-YYYY. In other words, the day of the month should come first, followed by a hyphen (`-`), followed by the month itself, followed by another hyphen (`-`), and finally the year. Days and months should always have two digits, and years should have four digits.

For the purpose of this exercise, pretend that all months have 31 days, and remember that there are twelve months in any year.

When the string is a correctly formatted date, your function should return `True`. Where the string is not a valid date, your function should return `False`.

The blue cell below should contain ALL NECESSARY CODE, including import statements, for your function to work properly.



**Solve it (2 points)**:

Write a function called `emailCheck` that will accept a string as an argument, and determine whether or not that string is a valid email. Emails take the following form: a string that contains numbers, letters, and periods followed by the `@` symbol and a domain. We will accept domains that contain numbers and letters, ending in `.com`, `.edu`, or `.org`.

When the string is a correctly formatted email address, your function should return `True`. Where the string is not a valid email address, your function should return `False`.

The blue cell below should contain ALL NECESSARY CODE, including import statements, for your function to work properly.

