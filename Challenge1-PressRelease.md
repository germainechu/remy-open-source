
<img src="https://github.com/germainechu/remy-open-source/assets/45610419/7a931e95-f4d5-4d03-a740-c1eefd9f2708" width="60" height="60">
<h1> SummarAIze: Intelligent News Summarization </h1></img>


## 🗺️ Overview

The project focuses on understanding and summarizing daily press releases from newswires. The goal is to create a system that can automatically extract essential words and phrases, summarize the key points, and generate a daily report/news article from those findings to post on a mining media/news website.

## 🎯 Objectives

### Data Collection
- **Feature**: Collect daily press releases from newswires for mining press releases.
- **Additional Information**:
  - Example news wires include:
    - [MiningNewsWire](https://miningnewswire.com/)
    - [Mining Journal](https://www.mining-journal.com/)
    - [Mining and Metals News | Press Releases from Mining and Metals Companies | Newsfile](https://www.newsfilecorp.com/news/mining)
    - [All Mining News and Press Releases from PR Newswire](https://www.prnewswire.com/news-releases/mining-metals-latest-news/)
    <br>

`Dev Notes `
  - This is a must-have. Daily press release is text data that must be collected.
  - Web scraping is the manual solution. What could be a more automated approach to retrieve press releases in a given area?


### 🔍 Keyword and Phrase Extraction
- **Feature**: Identify and extract essential words and phrases from the press releases.
- **Additional Information**:
  - Examples include "drill results," "financings," and "copper," "copper percentages."
  - Use natural language processing (NLP) techniques to determine the significance of these words and phrases, extracting those most relevant to drill results, financings, and copper percentage.
  - Utilize machine learning to summarize key points.

### 📆 Daily Report Generation
- **Feature**: Compile the summaries into a cohesive daily report.
- **Additional Information**:
  - Present the report in a clear and concise format.

### 📊 Performance Evaluation
- **Feature**: Implement metrics to evaluate the performance of keyword extraction and summarization models.
- **Additional Information**:
  - Use benchmarks and comparisons to existing summarization tools.
<br>

`Dev Notes`
  - This is a nice-to-have. Go for simplicity.

### 🙋🏻‍♂️ User Interface Development
- **Feature**: Develop a simple web-based user interface for users to view daily reports.
- **Additional Information**:
  - Allow users to input their own press releases and get summaries in real-time.
<br>

`Dev Notes  `
  - This is a nice-to-have. Go for simplicity.
  - The simplest solution is to generate a report, then send it to the user's email address, or to generate a JSON file that's saved locally on the client side.
