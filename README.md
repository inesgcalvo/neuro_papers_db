<!-- README -->
### README
<!-- PROJECT LOGO -->
<div align="center"><a>
  <img src="img/logo_neuro_papers_2.png" alt="Logo" width="150"></a>
  <h1 align="center">neuro papers db</h1>
  <p align="center">
    2022 - 2023 Neuroscience Scientific Publications<br><br>
    <a href="https://github.com/inesgcalvo/neuro_papers">
    <strong>Explore the docs »</strong></a></p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#description">Description</a>
    </li>
    <li><a href="#extraction">Extraction</a></li>
      <ul>
        <li><a href="#pubmed">PubMed</a></li>
        <li><a href="#biorxiv-api">biorXiv API</a></li>
        <li><a href="#sci-hub">sci-hub</a></li>
        <li><a href="#crossref">Crossref</a></li>
        <li><a href="#genderize-api">genderize API</a></li>
      </ul>
    <li><a href="#transformation">Transformation</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The development of a comprehensive database for scientific publications in neuroscience is of utmost importance. With the rapid expansion of research in this field, a centralized repository can serve as a valuable resource for scholars, educators, and students alike. This initiative not only consolidates the existing knowledge but also paves the way for new discoveries and breakthroughs. 
<div align="center">
  <a>
    <img src="img/db_schema.PNG" alt="neuro papers db" width="700">
  </a>
</div>
   <br />

The idea is to gather data from PubMed publications and enrich them with information from other sources, like Crossref. Also, collect data from biorxiv preprints. Lastly, to compile information regarding the availability of these publications on Sci-Hub.

<p align="right">(<a href="#readme">Back to top</a>)</p>

### Built With

The following Python libraries have been used for this project: 

* ``requests`` -- HTTP for Humans
* ``pymongo`` -- written for MongoDB
* ``selenium`` -- automates browsers
* ``nltk`` -- Natural Language Toolkit

<p align="right">(<a href="#readme">Back to top</a>)</p>

 <!-- DESCRIPTION -->
## Description
A scientific article often contains several key elements that contribute to its credibility and accessibility. These elements include a Digital Object Identifier (<span style="color:#FF0000">**DOI**</span>) for precise identification and referencing, a clear and concise <span style="color:#FF0000">**title**</span> that succinctly reflects the content of the study, a list of <span style="color:#FF0000">**authors**</span> indicating the individuals responsible for the research, their <span style="color:#FF0000">**affiliations**</span>, and their respective institutional or organizational affiliations. The article also typically includes information about the <span style="color:#FF0000">**journal**</span> in which it is published, such as the journal's name, publication <span style="color:#FF0000">**year**</span>, and <span style="color:#FF0000">**month**</span>, along with the specific <span style="color:#FF0000">**volume**</span> and <span style="color:#FF0000">**page**</span> numbers where the article can be found. In addition, some articles may include unique identifiers such as PubMed ID (<span style="color:#FF0000">**PMID**</span>) and PubMed Central ID (<span style="color:#FF0000">**PMCID**</span>) for efficient retrieval in relevant databases. Moreover, a comprehensive <span style="color:#FF0000">**abstract**</span> summarizing the main objectives, methodologies, findings, and implications of the study is often provided to give readers a quick overview of the research's key points.

_The words marked in <span style="color:#FF0000">**bold**</span> indicate the elements I have collected for each article._

<p align="right">(<a href="#readme">Back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Extraction
For the creation of this database, a diverse range of sources has been utilized to ensure comprehensive and robust data compilation. These sources encompass various reliable online repositories, and authoritative databases within the field.

<div align="left">
  <h4 align="left">Methods:<br>
    - Web Scraping with <span style="font-family:Courier; color:orange">selenium</span><br>
    - API data extraction with <span style="font-family:Courier; color:orange">requests</span><br>
    - Archives from <a href="https://sci-hub.se/database">https://sci-hub.se/database</a>
  </h4></p></div>

### PubMed
PubMed is a free-access database that houses a vast collection of bibliographic references and abstracts of research articles in the fields of biomedicine and health.

https://pubmed.ncbi.nlm.nih.gov/

### biorXiv API
bioRxiv is a free online archive and distribution service for unpublished preprints in the life sciences. bioRxiv provides an API (Application Programming Interface) that allows developers to access and retrieve data programmatically from the bioRxiv server, enabling seamless integration of preprint information into various applications and workflows.

1. Read the documentation [https://api.biorxiv.org/](https://api.biorxiv.org/)
2. Prepare the url:
   ```
    https://api.biorxiv.org/details/[server]/[interval]/[cursor]/[format]
   ```
    - Server: ``biorxiv``
    - Intervals: 
    ```
    ['2022-01-01/2022-12-31',
    '2023-01-01/2023-12-31']
    ```
    - Format: ``json``

### sci-Hub
Sci-Hub is a controversial online repository that provides free access to a vast collection of academic articles, including those behind paywalls, bypassing traditional copyright and subscription barriers.

https://sci-hub.se/database 

### Crossref
Crossref is a not-for-profit organization providing a comprehensive metadata infrastructure that facilitates the discovery and linking of scholarly content. Through its extensive network, Crossref collects and distributes rich metadata, including bibliographic information, citations, and persistent identifiers, thereby enhancing the visibility, accessibility, and interoperability of academic and professional research publications.

https://search.crossref.org/

### genderize API
Determine the gender of a name. A simple API to predict the gender of a person given their name. The API is free for up to 1000 names/day. No sign up or API key needed.

```
https://api.genderize.io?name=peter

{
  "name": "peter",
  "gender": "male",
  "probability": 0.99,
  "count": 165452
}
```
https://genderize.io/

<p align="right">(<a href="#readme">Back to top</a>)</p>

<!-- TRANSFORMATION -->
## Transformation
Data cleansing in pandas involves the process of detecting and rectifying any inconsistencies, inaccuracies, or anomalies within a dataset. Leveraging functionalities such as data filtering, handling missing values, and identifying outliers, data cleansing ensures the accuracy and reliability of the dataset.

<div align="center">
  <a><img src="img/article.PNG" alt="mongo" width="700"></a>
  <span>Example of Extracted, Transformed, and Loaded data into MongoDB from a preprint via the biorxiv API.</span>
</div><br />

<p align="right">(<a href="#readme">Back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
Neuro Papers DB project roadmap outlines a series of essential tasks conducted as part of my ETL & data analysis pipeline:

- [x] 01_pubmed.ipynb\
Articles data was extracted from **PubMed** using `selenium`
- [x] 02_biorxiv.ipynb\
Preprints data was extracted from the biorXiv API with `requests`
- [x] 03_crossref.ipynb\
Crossref's 'href' and 'json_href' columns extraction with `selenium`
- [x] 04_data_cleansing.ipynb\
Data Cleansing with `pandas`
- [ ] 05_genderize.ipynb\
Genderize the first and the last authors with genderize API using `requests`
    - [x] First authors
    - [ ] Last authors
- [x] 06_feeding_mongodb.ipynb\
Feeding my MongoDB with DataFrames.
- [x] 07_analysis.ipynb\
Initial exploratory analysis of the extracted data with `matplotlib.pyplot`
- [ ] 08_queries.ipynb\
Queries for MongoDB with `pymongo`

<p align="right">(<a href="#readme">Back to top</a>)</p>

<!-- CONTACT -->
## Contact

* [My GitHub](https://github.com/inesgcalvo)
* [My LinkedIn](https://www.linkedin.com/in/ines-g-calvo/)
* [My Website](http://inesgcalvo.byethost31.com/)

<p align="right">(<a href="#readme">Back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I am sincerely grateful for the unwavering support and guidance provided by my esteemed professors: Yona, Carlos, JeanCha, Rosella and Jaime. Their dedication to nurturing their students' intellectual growth and fostering an environment of learning has profoundly impacted my educational journey. With their mentorship, I have not only gained invaluable knowledge but also developed a deeper appreciation for the subjects they taught. I extend my heartfelt appreciation to them for their commitment and passion for education.

* [Yona](https://github.com/YonatanRA)
* [Carlos](https://github.com/CharlyKill7)
* [Jean-Cha](https://github.com/yamadajc)
* [Rosella](https://github.com/rmanzi13)
* [Jaime](https://github.com/RCJaime)

<p align="right">(<a href="#readme">Back to top</a>)</p>
