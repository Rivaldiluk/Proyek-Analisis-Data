import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Update the file paths to reflect the new structure
rfm = pd.read_csv('submission/dashboard/rfm_analysis.csv')
category_revenue = pd.read_csv('submission/dashboard/category_revenue.csv')
review_analysis = pd.read_csv('submission/dashboard/review_analysis.csv')

# Add CSS for better layout
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

# Dashboard title
st.title("Dashboard Analisis Data E-Commerce")

# RFM Analysis section
st.header("RFM Analysis")
st.dataframe(rfm)

# Revenue by Product Category section
st.subheader("Revenue by Product Category")
st.bar_chart(category_revenue.set_index('product_category_name')['revenue'], use_container_width=True)

# Visualization of Top 10 Product Categories by Revenue
plt.figure(figsize=(10, 5))
top_products = category_revenue.head(10)
sns.barplot(x='revenue', y='product_category_name', data=top_products, palette='viridis', hue='product_category_name', legend=False)
plt.title('Top 10 Product Categories by Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Product Category')
st.pyplot(plt)
plt.close()

# Review Analysis section
st.header("Review Analysis")
st.dataframe(review_analysis)

# Visualization of Review Scores vs. Purchase Count
plt.figure(figsize=(10, 5))
sns.scatterplot(x='review_score', y='purchase_count', data=review_analysis, color='blue')
plt.title('Relationship between Review Scores and Purchase Volume')
plt.xlabel('Review Score')
plt.ylabel('Number of Purchases')
st.pyplot(plt)
plt.close()
