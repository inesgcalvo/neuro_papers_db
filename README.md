<!-- README -->
##### README
<!-- PROJECT LOGO -->
<div align="center"><a>
  <img src="img/logo_neuro_papers_2.png" alt="neuropapers db" width="150"></a>
  <h1 align="center">neuropapers db</h1>
  <p align="center">2010 - 2023 Neuroscience Scientific Publications<br><br>
    <a href="https://github.com/inesgcalvo/neuro_papers">
    <strong>Explore the documents »</strong></a></p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol><li><a href="#about-the-project">About The Project</a></li>
      <ul><li><a href="#description">Description</a></li></ul>
      <ul><li><a href="#requirements">Requirements</a></li></ul>
      <li><a href="#extraction">Extraction</a></li>
      <li><a href="#transformation">Transformation</a></li>
      <li><a href="#loading">Loading</a></li>
      <li><a href="#visualization">Visualization</a></li>
      <li><a href="#modeling">Modeling</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a href="#acknowledgments">Acknowledgments</a></li></ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The idea is to gather data from PubMed publications and enrich them with information from other sources, like Crossref. 

<div align="center">
  <a><img src="img/db_schema.PNG" alt="neuropapers db" width="700"></a>
</div><br />

Also, collect data from biorxiv preprints. Lastly, to compile information regarding the availability of these publications on Sci-Hub.

<details>
  <summary>Project Creation Summary</summary>
  <ol><h4>Data Extraction:</h4></ol>
    <ol><ol>
    <h6><a href="https://www.scimagojr.com/">SCImago (SJR)</a></h6>
    <h6><a href="https://www.oecd.org/">OECD (© Organisation for Economic Co-operation and Development)</a></h6>
    <h6><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed®</a></h6>
    </ol></ol>
  <ol><h4>Data Transformation:</h4></ol>

    pandas, nltk, ...

  <ol><h4>Data Loading:</h4></ol>
  <ol><h4>Data Visualization:</h4></ol>
  <ol><h4>ML Modeling:</h4></ol>
</details>

<p align="right">(<a href="#readme">Back to top</a>)</p>



 <!-- DESCRIPTION -->
## Description
- **DOI (Digital Object Identifier):** For precise identification and referencing.
- **Title:** Clear and concise, reflecting the content of the study.
- **Authors:** List of individuals responsible for the research.
- **Affiliations:** Information about the affiliations of the authors.
- **Journal:** Information about the journal of publication, including name, publication year, and month.
- **Volume and Page Numbers:** Specific volume and page numbers where the article can be found.
- **PubMed ID (PMID):** Unique identifier for efficient retrieval in relevant databases.
- **PubMed Central ID (PMCID):** Another unique identifier for efficient retrieval.
- **Abstract:** A comprehensive summary of the main objectives, methodologies, findings, and implications of the study.
  
<p align="right">(<a href="#readme">Back to top</a>)</p>



<!-- REQUIREMENTS -->
## Requirements
Requirements from Ironhack Spain for the Final Project.

**Basic Knowledge:**
  -  Proficiency in Python
  -  Proficiency in Data Transformation

**Project Submission:**
  - [x]  README.md
  - [x]  Folder structure with all the necessary documentation for the project
  - [x]  Support material for the presentation

**Specific Criteria:**

Below is a table with 4 main sections. Each project must comply with the indication of at least 2 of the sections, as they fit each project:
  
  Extraction:
  - [x]  APIs
  - [x]  WebScraping
  - [ ]  Automated file download
  - [ ]  Queries to Mongo
  - [ ]  Queries to SQL

  Loading:
  - [ ]  Structured database creation (SQL) or Cloud creation
  - [ ]  Unstructured database creation (Mongo)
  - [ ]  API creation

  Visualization:
  - [ ]  Use of at least one Python visualization library
  - [ ]  Use of PowerBI or Tableau
  - [ ]  Use of Streamlit or Flask

  Machine Learning:
  - [ ]  Use of ML models to infer a numerical value
  - [ ]  Use of ML models to infer one or more categories
  - [ ]  Use of ML models for imputing null values

<p align="right">(<a href="#readme">Back to top</a>)</p>



<!-- EXTRACTION -->
## Extraction
For the creation of neuropapers database, a diverse range of sources has been utilized to ensure comprehensive and robust data compilation.

<div align="left">
  <h4 align="left">Data Extraction Methods:<br><br>
    - .csv archives from: 
    <a href="https://www.scimagojr.com/">SCImago</a> and 
    <a href="https://www.oecd.org/">OECD</a>.<br>
    - Web Scraping with <span style="font-family:Courier; color:orange">selenium</span> from:
  <a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a> and 
  <a href="https://search.crossref.org/">Crossref</a><br>
    - API data extraction with <span style="font-family:Courier; color:orange">requests</span> from:
    <a href="https://genderize.io/">genderize API</a>.<br>
  </h4></p></div>

<p align="right">(<a href="#readme">Back to top</a>)</p>



<!-- TRANSFORMATION -->
## Transformation
Data cleansing in pandas involves the process of detecting and rectifying any inconsistencies, inaccuracies, or anomalies within a dataset. Leveraging functionalities such as data filtering, handling missing values, and identifying outliers, data cleansing ensures the accuracy and reliability of the dataset.



<!-- LOADING -->
## Loading
Data Loading

<p align="right">(<a href="#readme">Back to top</a>)</p>



<!-- VISUALIZATION -->
## Visualization
Data Visualization

<p align="right">(<a href="#readme">Back to top</a>)</p>



<!-- MODELING -->
## Modeling
Machine Learning Modeling

<p align="right">(<a href="#readme">Back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [GitHub](https://github.com/inesgcalvo)
* [LinkedIn](https://www.linkedin.com/in/ines-g-calvo/)
* [Website](http://inesgcalvo.byethost31.com/)

<p align="right">(<a href="#readme">Back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
I am sincerely grateful for the support and guidance provided by my teachers: Yona, Carlos, JeanCha, Rosella, and Jaime. Their dedication to fostering an environment of learning and nurturing their students' intellectual growth has profoundly impacted my educational journey at [Ironhack](https://www.ironhack.com/es).

* 💡 [Yona](https://github.com/YonatanRA)
* 🏈 [Carlos](https://github.com/CharlyKill7)
* ⚡ [Jean-Cha](https://github.com/yamadajc)
* 🤖 [Rosella](https://github.com/rmanzi13)
* 😊 [Jaime](https://github.com/RCJaime)

<p align="right">(<a href="#readme">Back to top</a>)</p>
