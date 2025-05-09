# Data Engineer VnExpress

## Project Description:
Developed an automated system to collect and analyze electronic newspaper data on disease interest levels,
providing an interactive dashboard on Power BI. Utilized Docker, Selenium, MongoDB, PostgreSQL, and
PySpark to automate the ETL process and analyze daily health information search trends.

## Folder Structure:
```
Data_Engineer_VnExpress/
├── vnexpress_data_warehouse/
│   ├── __pycache__/
│   ├── spiders/
│   ├── .DS_Store
│   ├── .dockerignore
│   ├── CSV_to_Json.ipynb
│   ├── DataFinal_CacBenh_cleaned.csv
│   ├── Dockerfile
│   ├── ETL.ipynb
│   ├── Jenkinsfile
│   ├── __init__.py
│   ├── docker-compose.debug.yml
│   ├── docker-compose.yml
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── requirements.txt
│   ├── scrapy.cfg
│   └── settings.py
├── .DS_Store
├── Final_product.pbix
└── README.md
```

## 📊 Insights from Media Spread Analysis Dashboard
![Image 1](https://github.com/user-attachments/assets/36a78d4f-e3a4-4032-a3d4-6afc25cf97ca)

- **Musculoskeletal** and **dermatological diseases** received the highest engagement (likes and comments), indicating strong public interest in these health topics.
- **Ho Chi Minh City (TP.HCM)** showed the highest level of interaction with health-related articles, while **Hanoi** and **Phu Yen** had significantly lower engagement.
- A large proportion of posts (**77.83%**) lacked specific location tagging (**N/A**), suggesting room for improvement in geo-tagging data to enable more detailed regional analysis.
- Across **997 posts**, there were a total of **3,335 likes** and **2,060 comments**, showing high user engagement with online health content, especially for common and relatable diseases.
- Certain disease topics such as **neonatal care**, **cancer**, and **urological health** received much less attention, highlighting potential gaps in media coverage and areas for increasing public health awareness.

---

## 📊 Insights from Reader Engagement by Author Dashboard

![Image 2](https://github.com/user-attachments/assets/da366add-33a2-4d89-8810-ceb703daf9bd)

- **Anh Ngọc** is the most prominent author in terms of both **post volume and audience engagement**, with 43 articles (18.79% of total posts), an average of **2.65 likes per post**, and **0.35 comments per post**.
- Other authors such as **Phi Hồng, Kim Uyên, and Mai Cát** contributed fewer articles and had lower interaction metrics, suggesting that Anh Ngọc's content is significantly more engaging or better targeted to readers.
- The **month of May** saw the highest spike in **total likes**, even though the number of posts did not increase drastically — indicating strong content quality or a timely topic.
- From **May to July**, there was a consistent rise in **likes per post**, showing a period of high reader engagement. However, interaction dropped sharply after **August**, possibly due to changes in content themes or seasonal trends.
- Most other authors contributed only 1–7 articles each, making it difficult to draw strong comparative insights, but the disproportionate engagement with Anh Ngọc's content highlights a clear **audience preference**.

---

## 📊 Insights from Analysis of Community Interest in Online News Articles about Diseases

![Image 3](https://github.com/user-attachments/assets/17b52fc8-0575-4adb-990b-fa945e027edf)

- **"Nhi So sinh" (congenital heart defects)** is currently the most prominent topic, capturing the highest audience attention with **22.85% of the total comments and likes**. This indicates a significant interest or a high demand for information regarding this specific condition.
- Other topics such as **"Ung thư" (cancer) at 16.45% and "Tim mạch" (cardiovascular diseases) at 14.51%** also receive substantial engagement, suggesting these are top health concerns within this news-reading community.
- Although the **total number of likes (3297)** significantly outweighs the **total number of comments (2020)**, the average **comment/like rate (0.61)** suggests that readers tend to express their support or interest by liking articles rather than actively participating in discussions through comments.
- The line chart illustrates the fluctuation in engagement levels (comments and likes) across different disease categories. Further analysis is needed to pinpoint **specific times when certain diseases experienced a surge in attention**, potentially linked to medical events, seasons, or information trends.
- The scatter plot reveals the correlation between the **average number of comments and the total number of likes** for each disease. Diseases located in the upper right quadrant (e.g., seemingly "Ung thư" and "Tim mạch") indicate a combination of a large interested audience and a higher propensity for discussion.
- The **average content length of articles** on various diseases also differs (represented by the "Avg of count content word" line). Comparing this length with engagement metrics could suggest the **preferred content format** of readers for specific health topics. For instance, do more complex subjects require longer articles that still maintain audience interaction?

---

## 📊 Insights Analysis of Disease Prevalence Across 4 Seasons in a Year

![Image 4](https://github.com/user-attachments/assets/f93e611e-bb83-4273-9ae4-5ffe2776befc)

- **Summer and Winter see the most reported diseases**. Summer has the highest count (35.90%), closely followed by Winter (35.41%). Spring has the lowest (27.1%).
- **Disease occurrences change over time and by season**. The stacked area chart shows how different diseases fluctuate within each season across the years. Some diseases likely spike during specific seasons.
- **Overall disease counts vary over time**. The line chart shows periods with more or fewer total reported illnesses. These peaks might align with specific seasons.
- **Different diseases likely have different seasonal patterns**. We need to look at individual disease trends to see which ones are more common in which seasons (e.g., winter for respiratory issues, summer for digestive problems).
  
  **Key takeaway:** Disease prevalence appears to be influenced by the seasons, with Summer and Winter having the highest numbers. Further analysis of individual disease trends is needed to understand specific seasonal patterns.

---

### Link Power BI: [Final Product](https://github.com/thanhthao2004/Data_Engineer_VnExpress/blob/main/Final_product.pbix)
