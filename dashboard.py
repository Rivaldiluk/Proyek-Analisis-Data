import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gc
import os

rfm = pd.read_csv('rfm_analysis.csv')
category_revenue = pd.read_csv('category_revenue.csv')
review_analysis = pd.read_csv('review_analysis.csv')

st.markdown(
    """
    <style>
    .reportview-container {
        flex-direction: row;
    }
    .sidebar .sidebar-content {
        width: 100%;
    }
    .block-container {
        padding: 1rem;
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Dashboard Analisis Data E-Commerce")

st.header("RFM Analysis")
st.dataframe(rfm)

st.subheader("Revenue by Product Category")
st.bar_chart(category_revenue.set_index('product_category_name')['revenue'], use_container_width=True)

plt.figure(figsize=(10, 5)) 
top_products = category_revenue.head(10) 
sns.barplot(x='revenue', y='product_category_name', data=top_products, palette='viridis')
plt.title('Top 10 Product Categories by Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Product Category')
plt.savefig('/content/drive/MyDrive/E-Commerce Public Dataset/top_product_categories.png')
st.pyplot(plt)
plt.close()


st.header("Review Analysis")
st.dataframe(review_analysis)


plt.figure(figsize=(10, 5))
sns.scatterplot(x='review_score', y='purchase_count', data=review_analysis, color='blue')
plt.title('Relationship between Review Scores and Purchase Volume')
plt.xlabel('Review Score')
plt.ylabel('Number of Purchases')
plt.savefig('/content/drive/MyDrive/E-Commerce Public Dataset/review_score_vs_purchases.png')
st.pyplot(plt)
plt.close()
