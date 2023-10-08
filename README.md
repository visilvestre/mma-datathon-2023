# mma-datathon-2023

Hello dear guest, this github was used to develop a solution for the 2023 MMA-Datathon for University of Toronto (UoT). 
The problem at hand was a case to select the top 1000 products to insert into a new aisle for instabasket company.

## 1- Dataset and baselines
UoT provided a dataset with approximately 987259 rows, in which the potential key was product_id + order_id. 

An initial study over data quality was done using pandas profiling (profiling.py) (updated to ydata_profilling). With it we created the file output.html with the statistics of the dataset to understand how usable it could be.

After understanding the dataset, UoT gave a Q&A session where they presented the mma_mart_template.ipynb, a file containing baselines for the metrics that were later used in the code.

## 2- Model development
The first target was to:
<ul>Maximize the metric of number of orders with the new aisle products used by instabasket personal shoppers. The second was to maximize the % of items in each order on average that were     from the new aisle. </ul>

The second target was to:
<ul> Find substitute products for lacking products, which can maximize the new aisle usage by the personal shoppers </ul>

We initially thought of going forward with the use of linear programming (LP) for the optimization, with that we modeled the problem on Datathon potential solution pptx. 

Then, after studying the relationships between the variables, we found out that Department to Aisle had a relationship 1-N , and Aisle to Department had a relationship 1-1. Also, we saw that majorly a product was member of one aisle 1-1, and one aisle had many products 1-N.

With that , we understood that probably the products in the same aisle ( in the same department ) would have similar characteristics. With that we decided to apply a clustering method that would divide the each aisle group of products into clusters based on their naming. From there, for each cluster we would decide the most frequent product as the substitute for all other products within the same cluster.

The number of clusters per aisle was decided after checking ~ 10 aisles elbow curves, where they showed a change in the curve near to approximately 1/5 of the curve. With that we decided to always have (number of products in aisle) / 5  as the number of clusters in each aisle. 

We used Natural language processing ( NLP ) to clean the names of the products prior to vectorizing and using in the K-Means clustering algorithm per aisle. 

Once the K-means model was ready and working generating substitutes per aisle/cluster, we moved back to the optimization problem. There we tried to use the Linear programming but the amount of variables was too big (~~ 35K) for Excel solver to handle. Given the learning curve for python solver solutions and that our team of 4 persons got shrinked to 2, we decided that our K-Means algorithm was a differential good enough for the amount of work hours we had at hand, and moved to a probabilistic approach selecting the most frequent products in the orders.

The "probability bag" approach we used takes into consideration the understanding that : P(x) is the number of times an event (x) occurs divided by the number of opportunities for it to occur. With this comprehension we used product_id frequency in the train order dataset per order as our measure of how likely the event would happen again in the future. With this we ordered all products ( Separating into general | frozen | refrigerated ) , and picked the top (general = 800 | frozen = 100 | refrigerated = 100). 

A second approach was to change all product_ids that had a substitute and calculate the frequency from there, order all again from max to min, and pick the top 1000 again. 

## 3- Results

The results showed that the best approach was the one considering the substitutes, specially when we translate the product_ids into substitutes showing the space of opportunity if the customers accept the substitutes indicated. 

The final results are in the presentation (MMA Datathon 2023.pptx).



