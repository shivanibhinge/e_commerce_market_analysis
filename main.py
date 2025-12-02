import streamlit as st
import pandas as pd
from recommender import recommend

# Define the data for team members
team_data = {
    'Name': [
        'Shivani Atul Bhinge',
        'Vinay Chandra Konda',
        'Sanika Gidye',
        'Sri Shakthi Aravindan'
    ],
    'Role': [
        'Machine Learning Lead',
        'Data Lead',
        'Visualization Lead',
        'Analysis Lead'
    ],
    'Contribution': [
        """Shivani led the Machine Learning workflows of the project. 
        She implemented Regression models (Linear Regression, Random Forest Regression) 
        and Clustering models (K-Means). She was responsible for hyperparameter tuning, 
        model evaluation, performance metrics, and ensuring model reproducibility. 
        She also contributed to validating assumptions for regression and preparing 
        ML-ready datasets.""",

        """Vinay handled Data Engineering tasks and built the Apriori Association Rule–Mining 
        Module. He prepared the dataset for transactional analysis, performed data cleaning, 
        converted invoices into a basket format, and implemented Apriori to extract 
        meaningful patterns such as item co-occurrences and support–confidence–lift metrics. 
        He also assisted in backend integration and ensuring the algorithms run efficiently.""",

        """Sanika developed the Decision Tree Classification module and contributed heavily 
        to the UI visualization components. She worked on model training, feature encoding, 
        managing class imbalance, and presenting interpretability outputs like feature 
        importance and tree-structure logic. She also designed dashboards and supported 
        the website layout and user-friendly visuals.""",

        """Shakthi handled the Exploratory Data Analysis (EDA) and trend-based insights. 
        She worked on creating summary statistics, time-series purchase behavior, 
        country-level purchase patterns, customer segmentation insights, and anomaly detection. 
        She ensured data cleanliness, removed duplicates, handled missing values, and 
        prepared charts used across multiple tabs."""
    ],
    'Picture': [
        'https://media.licdn.com/dms/image/v2/D4D03AQEr39coxWKsoA/profile-displayphoto-crop_800_800/B4DZjfup6.HwAM-/0/1756100210989?e=1765411200&v=beta&t=twZ4t-BsBMHAsWog26neYbxX8YmnS9R6TP5ajDlFppk',
        'https://media.licdn.com/dms/image/v2/D5603AQGn1ZzMYtggOw/profile-displayphoto-crop_800_800/B56ZqqOirdJQAI-/0/1763792530611?e=1765411200&v=beta&t=WAP2r5oifTtASVhMRZomxVD9wHG_xcnwMw_cOBlQV4E',
        'https://media.licdn.com/dms/image/v2/D4D03AQGAbti5YEFCRg/profile-displayphoto-shrink_800_800/B4DZeTS4gwGUAc-/0/1750522891490?e=1765411200&v=beta&t=3xVxnqnoDPfwthz6bRmwdKwRXi-Yz3Zal3od7bwlDQ8',
        'https://media.licdn.com/dms/image/v2/D5603AQH0ju7cHjZGiw/profile-displayphoto-crop_800_800/B56ZpsSUvmH8AM-/0/1762753335349?e=1765411200&v=beta&t=coMrefTy0-ob4HptrTiAMZz5qTWo65hkSqdftNQwnUI'
    ],
    'LinkedIn': [
        'https://www.linkedin.com/in/shivani-bhinge/',
        'https://www.linkedin.com/in/vinaychandra15/',
        'https://www.linkedin.com/in/sanika-gidye-10305b22a/',
        'https://www.linkedin.com/in/sri-shakthi-aravindan-a047b5257/'
    ],
    'GitHub': [
        'https://github.com/shivanibhinge',
        'https://github.com/Vinay-15',
        'https://github.com/sanikagidye',
        'https://github.com/Srishakthi77'
    ]
}


# Create a DataFrame
df_team = pd.DataFrame(team_data)

st.set_page_config(page_title="The Retail Compass", page_icon="📈", layout="wide")

st.markdown(
    '<h1 style="color: #D17F43; font-weight: 600; font-size: 6em; font-family: impact;">The Retail Compass</h1>',
    unsafe_allow_html=True)

# Create tabs
#tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Team", "Overview", "Data Exploration"])
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Introduction", "Team", "Overview", "Data Exploration", "Model Evaluation", "Results & Conslusion","Product Recommender System"])


# --- Introduction Tab ---
with tab1:
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.header("Introduction")
        st.info(
            """
            Welcome to the Retail Stores Analysis project. This initiative aims to provide
            in-depth insights into retail store performance.
            Our analysis covers key metrics such as sales trends, customer demographics,
            and market share to help businesses make data-driven decisions.

            The project utilizes a comprehensive dataset that includes information from
            retail chains from across different countries such as United States, United Kingdom, and Japan. By examining
            these different markets, we can identify regional trends and opportunities
            for growth.
            """
        )
        st.info(
            """
            #### Project Focus
            Customer and Market analysis within the e-commerce sector. The core focus of the research is customer segmentation using RFM (Recency, Frequency, Monetary) analysis and exploratory analysis of the product pricing strategies.

            ##### Why is it important:
            * **Actionable Business insights:** By applying the RFM analysis, the project can help the online retailers to identify and cluster customers based on distinct groups. This data-driven foundation is useful for developing targeted marketing strategies, customer retention, stock analysis eventually adding value to customer experience and overall profitability.
            * **Strategic planning and inventory management:** Understanding how product prices are set and how they vary across different years. These insights will help in managing inventory and optimizing companies revenue.
            """
        )
        st.info(
            """
            #### Stakeholders (Who is Affected?)
            Which industries, groups, or individuals are impacted by this issue? What are the real-world implications?
            * **The Business (the retailer):** This is the core stakeholder. Its impacted by sales volume, revenue, profitability, inventory management, and customer retention.
            * **Customers:** These are the individuals making purchases. They are affected by product availability, pricing, shipping costs, delivery times, and the quality of customer service.
            * **Suppliers:** These are the companies providing the products. Their relationship with the retailer is impacted by purchase orders, payment schedules, and demand for their goods.
            * **Logistics and Shipping Companies:** These companies are responsible for delivering goods. Their business is directly tied to the volume and geographical spread of the retailer's sales. The international nature of the sales (e.g., to countries like France, Germany, EIRE, and Norway as seen in the data) highlights the involvement of international logistics partners.
            """
        )
        st.info(
            """
            #### Existing Solutions & Gaps
            What solutions currently exist? What limitations or challenges remain?

            **Paper 1: A Stacking Approach to Customer Lifetime Value (CLV) Prediction**
            * **Current Solution:** A two-stage model uses a number of algorithms (Random Forest, XGBoost, ElasticNet) and a final model that combines their predicted values to produce more accurate CLV forecasting.
            * **Strengths:** More precise using the ensemble of various models; utilizes a rich feature set instead of RFM alone.
            * **Limitations:** Computationally demanding and convoluted; "black box" solution difficult to interpret; requires a lot of data.

            **Paper 2: Customer-Focused Sales Forecasting Model: RFM-ARIMA Methodology**
            * **Current Solution:** A combination solution that first uses RFM analysis in customer segmentation and elimination of noise before ARIMA is used on sales data.
            * **Strengths:** Maximizes accuracy and model fit by reducing data noise.
            * **Limitations:** Restricted for non-linear trend analysis and external factors like seasonality; reliant on large customer buy history data.

            **Paper 3: Development of a Retailer Forecasting Model Based on Customer Segmentation Using Data Mining Techniques**
            * **Current Solution:** Two-stage model that groups customers based on demographic and behavior data and forecasts for each group using a forecasting model.
            * **Strengths:** Improves inventory performance; is customer-focused; eliminates data redundancy.
            * **Limitations:** Can be limited in scope; might be limited to neat, small datasets.

            **Paper 4: Research on E-Commerce Inventory Sales Forecasting Model Based on ARIMA and LSTM Algorithm**
            * **Current Solution:** Two-model strategy with ARIMA for monthly inventory forecasting and LSTM for daily sales forecasting.
            * **Strengths:** Novel approach that improves accuracy; offers actionable solution for warehouse planning.
            * **Weaknesses:** Tested over short time period; LSTMs are prone to overfitting and difficult to interpret; requires large datasets.
            """
        )

    with col_right:
        st.header("")
        st.image(
            "https://be.trueprofit.io/uploads/retail-store-profitability-analysis.webp",
            use_container_width=True)
        st.image("https://www.gofrugal.com/sites/blog/files/gofrugal/benefits-retail-analytics.jpg",
                 use_container_width=True)

    st.markdown("---")

    st.subheader("The Blueprint")
    col_img, col_content = st.columns([1, 1])

    with col_img:
        st.image(
            "blueprint.jpeg",
            caption="Data-Driven Decisions",
            use_container_width=True)

    with col_content:
        st.info(
            """
            #### 1. Data Analysis and Preprocessing
            * **Data Cleaning:** Handle missing values, especially for CustomerID, and deal with negative quantities and prices.
            * **Feature Engineering:** Create new variables from the raw data, such as TotalSales and time-based features.
            * **Initial EDA:** Perform basic analysis to understand data distribution and identify overall sales trends.

            #### 2. Core Analysis
            * **Customer Segmentation:** Apply RFM analysis to group customers into distinct segments.
            * **Sales Forecasting:** Use a time-series model to predict future sales trends.
            * **Demand Forecasting:** Predict future demand for specific products.
            * **Price Optimization:** Analyze the relationship between UnitPrice and Quantity sold.
            * **Market Basket Analysis:** Identify common product associations for cross-selling.
            * **Geographical Trends:** Understand how sales and product popularity vary by country.
            * **Anomaly Detection:** Identify unusual transactions that may be fraudulent or data errors.

            #### 3. Project Impact
            * **Business Benefits:** The project provides insights for smarter decision-making, revenue growth, and reduced losses.
            * **Customer Benefits:** Customers gain a more customized experience with better product availability and relevant recommendations.
            * **Supply Chain Benefits:** Operations teams can improve planning, reduce waste, and balance logistics.
            * **Research Benefits:** The project serves as a real-world application for data science methods and offers new research directions.
            """
        )

# --- Team Tab ---
with tab2:
    st.header("Who We are")
    st.write("Meet the talented individuals behind this project.")

    # 2 profiles per row
    for i in range(0, len(team_data['Name']), 2):
        cols = st.columns(2)

        for col, idx in zip(cols, range(i, min(i + 2, len(team_data['Name'])))):
            with col:
                st.image(team_data['Picture'][idx], width=200)
                st.subheader(team_data['Name'][idx])
                st.write(f"**{team_data['Role'][idx]}**")
                st.write(team_data['Contribution'][idx])
                st.markdown(
                    f"""
                    🔗 [LinkedIn]({team_data['LinkedIn'][idx]})  
                    💻 [GitHub]({team_data['GitHub'][idx]})
                    """
                )


# --- Project Overview Tab ---
with tab3:
    st.header("📋 Project Overview")
    st.markdown(
        """
        # Retail Stores Analysis Research Questions

        <br>
        <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2196F3;">1. Customer-Centric Analysis</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin-bottom: 10px; color: #000000;">Customer Segmentation: Can we segment customers into distinct groups based on their purchasing behavior using RFM (Recency, Frequency, Monetary) analysis? What are the defining characteristics of each segment?</li>
            <li style="margin-bottom: 10px; color: #000000;">Customer Lifetime Value (CLV): What is the predicted Customer Lifetime Value for different customer segments, and how can this information be used to optimize marketing spend?</li>
            <li style="margin-bottom: 10px; color: #000000;">Customer Churn: What are the key indicators and behavioral patterns that can predict which customers are at risk of churning?</li>
        </ul>
        </div>
        <br>

        <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2196F3;">2. Sales and Inventory Management</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin-bottom: 10px; color: #000000;">Sales Forecasting: What are the predicted monthly sales for the upcoming year based on historical trends and seasonality?</li>
            <li style="margin-bottom: 10px; color: #000000;">Demand Forecasting: How will the demand for the top 10 best-selling products change over the next six months?</li>
            <li style="margin-bottom: 10px; color: #000000;">Price Elasticity: What is the relationship between UnitPrice and Quantity sold for a given product?</li>
        </ul>
        </div>
        <br>

        <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2196F3;">3. Product and Transaction Analysis</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin-bottom: 10px; color: #000000;">Market Basket Analysis: What are the most common product associations, and how can this information be used for product bundling or cross-selling?</li>
            <li style="margin-bottom: 10px; color: #000000;">Geographical Trends: How do sales and product popularity vary across different countries and regions?</li>
            <li style="margin-bottom: 10px; color: #000000;">Anomaly Detection: Can we identify and categorize unusual transactions (e.g., fraudulent activity or data entry errors) based on extreme values in Quantity or UnitPrice?</li>
            <li style="margin-bottom: 10px; color: #000000;">Product Return Analysis: What is the rate of returns for different product categories, and what factors correlate with a higher return rate?</li>
        </ul>
        </div>
        <br>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ### Who Benefits from this Research?

        <br>
        <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #2196F3;">Businesses / Retailers</h4>
        <ul style="list-style-type: none; padding: 0; color: #000000;">
            <li style="margin-bottom: 5px;">Wiser Decision-Making: Managers can make better decisions about product promotion, customer prioritization, and inventory levels based on accurate forecasts.</li>
            <li style="margin-bottom: 5px;">Growth in Revenue: Customer segmentation (e.g., high-value and at-risk) allows businesses to optimize marketing spend for highest return.</li>
            <li style="margin-bottom: 5px;">Fewer Losses: Forecasting eliminates overstocking, which ties up capital and leads to markdowns, and understocking, which foregoes sales.</li>
            <li style="margin-bottom: 5px;">Strategic Pricing: Competitive prices and optimal profit can be determined using models.</li>
        </ul>
        </div>

        <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #2196F3;">Customers</h4>
        <ul style="list-style-type: none; padding: 0; color: #000000;">
            <li style="margin-bottom: 5px;">Customized Experience: No spam emails; customers receive recommendations based on their purchase history and interest.</li>
            <li style="margin-bottom: 5px;">Improved Satisfaction: Accurate forecasting ensures bestsellers are in stock, leading to higher customer satisfaction.</li>
            <li style="margin-bottom: 5px;">Cost Savings: Reducing waste through stock management can be a key driver in ensuring competitive prices.</li>
        </ul>
        </div>

        <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #2196F3;">Supply Chain & Operations Teams</h4>
        <ul style="list-style-type: none; padding: 0; color: #000000;">
            <li style="margin-bottom: 5px;">Better Planning: Forecasting enables better coordination with transportation, warehousing, and suppliers.</li>
            <li style="margin-bottom: 5px;">Less Waste: Especially so for perishable materials like pharmaceuticals and food, where overstocking can lead to huge losses.</li>
            <li style="margin-bottom: 5px;">Balanced Logistics: Forecasting avoids bottlenecks during peak season.</li>
        </ul>
        </div>

        <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
        <h4 style="color: #2196F3;">Researchers / Data Scientists</h4>
        <ul style="list-style-type: none; padding: 0; color: #000000;">
            <li style="margin-bottom: 5px;">Real-World Application: Retail data provide a rich basis to test new machine learning algorithms.</li>
            <li style="margin-bottom: 5px;">New Research Directions: Problems such as dynamic segmentation and customer churn offer opportunities for innovation.</li>
            <li style="margin-bottom: 5px;">Benchmark Datasets: Models developed in this domain can be applied to other domains like healthcare, finance, or manufacturing.</li>
        </ul>
        </div>

        """,
        unsafe_allow_html=True
    )

# ---- Data Exploration Tab ----
with tab4:
    st.header("🧭 Data Exploration")
    st.info("""
    #### 1. Data Collection
    The dataset was obtained from **online retail store transactions** recorded between 2010 and 2011.  
    It includes **over 500,000 transactions** from multiple countries including the **United Kingdom, France, Germany, Norway, and Japan**.  
    Each record contains key details such as:
    - Invoice number and date  
    - Product description  
    - Quantity sold  
    - Unit price  
    - Customer ID and country  

    The dataset serves as a rich source for exploring customer purchasing behavior and global sales trends.
    """)

    st.info("""
    #### 2. Data Cleaning
    The dataset initially contained missing values, duplicates, and negative quantities.  
    We performed several cleaning steps to ensure the integrity of our analysis:
    - Removed transactions with **missing Customer IDs**  
    - Excluded **negative quantities or prices** (which usually indicate returns or errors)  
    - Removed **duplicate entries**  
    - Converted columns such as `InvoiceDate` to proper datetime format  
    - Created a new feature **`TotalSales = Quantity × UnitPrice`**  
    """)

    st.info("""
    #### 3. Exploratory Data Analysis (EDA)
    We conducted an in-depth exploration to understand sales patterns, customer segments, and market dynamics.  
    Key observations included:
    - **Sales distribution:** The majority of sales originated from the **United Kingdom**, followed by **Netherlands** and **EIRE**.  
    - **Top-selling products:** Items like decorative lights and gift sets appeared frequently across invoices.  
    - **Customer activity:** A small percentage of customers contributed to a majority of revenue — consistent with the Pareto principle (80/20 rule).  
    - **Time trends:** Clear seasonality effects were observed, especially during the holiday months.  
    """)

    st.info("""
    #### 4. Feature Engineering
    To prepare for modeling and segmentation:
    - Extracted **year, month, and day** from `InvoiceDate`  
    - Aggregated sales per customer to compute **Recency, Frequency, and Monetary (RFM)** metrics  
    - Identified **top-selling countries and products**  
    - Created derived metrics such as **average basket size** and **average order value**
    """)

    st.info("""
    #### 5. Insights and Patterns
    - The **UK market** dominated both sales and customer volume.  
    - Seasonal spikes suggested strong **holiday-driven purchase trends**.  
    - Many customers made **one-time purchases**, but a few frequent buyers accounted for significant revenue.  
    - The cleaned and engineered data provided a strong foundation for segmentation, forecasting, and price optimization in later stages.
    """)

    #st.success("""
    #The data exploration process played a crucial role in shaping our analytical direction and building accurate models.
    #""")'''

    st.header("📈 Visualizations")
    st.write("Below are key visualizations created during the data exploration phase to better understand sales patterns, customer behavior, and regional performance.")

    # --- Global Styling for Visualization Blocks ---
    st.markdown("""
        <style>
            .viz-block {
                display: flex;
                align-items: center;
                gap: 3px;
                background-color: #1E2D41;
                padding: 3px;
                border-radius: 3px;
                margin-bottom: 3px;
            }
            .viz-text {
                color: white;
                font-size: 16px;
                line-height: 1.6;
            }
        </style>
    """, unsafe_allow_html=True)

    # --- Visualization Block Template ---
    def visualization_block(image_path, caption, title, description):
    # Inject adaptive CSS styles for both light and dark themes
        st.markdown("""
            <style>
            .viz-block {
                border-radius: 12px;
                padding: 16px;
                background-color: var(--background-color);
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .viz-text {
                color: var(--text-color);
                font-size: 16px;
                line-height: 1.5;
            }
            </style>
        """, unsafe_allow_html=True)

        # Layout
        with st.container():
            st.markdown('<div class="viz-block">', unsafe_allow_html=True)
            col1, col2 = st.columns([1.3, 2])
            with col1:
                st.image(image_path, caption=caption, use_container_width=True)
            with col2:
                st.subheader(title)
                st.markdown(f'<div class="viz-text">{description}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- Visualization Blocks ---

    visualization_block(
        "img1.jpeg",
        "Top 10 Best Selling Products",
        "Top 10 Best Selling Products",
        """
        This visualization highlights the top 10 best selling products across the dataset.<br>
        The bar chart confirms the dominance of the top product ( Stock Code 84077 corresponding to WORLD WAR 2 GLIDERS ASSTD DESIGNS ), which accounts for almost 1% of total quantity among these items.<br>
        The analysis reveals that decorative items, gift sets, and seasonal products consistently rank among the top-selling categories, driving peak sales periods during holiday seasons
        """
    )

    visualization_block(
        "img2.jpeg",
        "Distribution of Log-Transformed Positive Total Sales",
        "Distribution of Log-Transformed Positive Total Sales",
        """
        This histogram illustrates the frequency distribution of positive total sales after a log-transformation.<br>
        The transformation reduces the extreme right-skew in raw sales data, producing a nearly normal shape with a slight left-skew.<br>
        The highest concentration of transactions occurs near a log-sales value of 2.5, indicating a stable sales frequency within that range.
        """
    )

    visualization_block(
        "img3.jpeg",
        "Box Plot of Transaction Price (Capped at 99th Percentile)",
        "Box Plot of Transaction Price (Capped at 99th Percentile)",
        """
        This box plot shows the distribution of unit prices, capped at the 99th percentile.<br>
        Most products are low-cost, with an IQR between $1.25 and $4.25, and a median around $2.50.<br>
        The presence of long right tails indicates higher-priced outliers (up to $17.50), though they represent only a small share of transactions.
        """
    )

    visualization_block(
        "img4.jpeg",
        "Monthly Revenue over Time",
        "Monthly Revenue over Time",
        """
        The revenue trend reveals substantial growth and volatility between 2009 and 2011.<br>
        - Peak: November 2011 (~$1.45M) marks the highest revenue month.<br>
        - Trough: December 2011 sees a sharp decline immediately after the peak.<br>        
        - Pattern: Mid-2010 dips are followed by strong recovery, indicating seasonality and cyclical demand.
        """
    )

    visualization_block(
        "img5.jpeg",
        "Total Sales by Day of the Week",
        "Total Sales by Day of the Week",
        """
        Sales show a clear weekly pattern, peaking mid-week and dropping sharply on weekends.<br>
        - Peak: Tuesday and Thursday exceed 4 million in total sales. <br>
        - Low: Saturday records nearly $0, suggesting store closure or unlogged transactions.<br>
        - Trend: Sunday and Friday show lower activity, confirming weekend business slowdown.
        """
    )

    visualization_block(
        "img6.jpeg",
        "Proportion of Total Invoices by Type",
        "Proportion of Total Invoices by Type",
        """
        - This donut chart illustrates the breakdown of all invoices into two categories: sales and returns.<br>
        - Key Insight: The vast majority of transactions (83.2%) are Sales Invoices.<br> 
        - A significant portion, 16.8%, are Cancellation/Return Invoices.<br>
        - This suggests that roughly one in every six invoices is a return or cancellation, a metric that may warrant further investigation into return rates and their causes.
        """
    )

    visualization_block(
        "img7.jpeg",
        "Top 10 Best Selling Products (Treemap)",
        "Top 10 Best Selling Products (Treemap)",
        """
        The top-selling products, measured by Total Quantity Sold, are dominated by a few items and top 3 products are:<br>
        WORLD WAR 2 GLIDERS ASSTD DESIGNS<br>
        ASSORTED COLOUR BIRD ORNAMENT<br>
        JUMBO BAG RED RETROSPOT
        """
    )

    visualization_block(
        "img8.jpeg",
        "Top 5 StockCodes Contribution to Total Sales",
        "Top 5 StockCodes Contribution to Total Sales",
        """
        - This pie chart depicts how much revenue the top 5 StockCodes contribute compared to all others.<br>
        - These products account for only 6.9% of total revenue<br>
        - Meaning 93.1 percent of sales come from a diverse range of items, confirming strong product variety and a non-reliant sales structure.
        """
    )

    visualization_block(
        "img9.jpeg",
        "Scatter Plot of Quantity vs. Price (Capped at 99th Percentile)",
        "Scatter Plot of Quantity vs. Price (Capped at 99th Percentile)",
        """
        This scatter plot shows the relationship between quantity sold and unit price.<br>
        - High density at low prices (<$5) and small quantities (<20).<br>
        - Slight inverse relationship: higher prices → lower quantities sold.<br>  
        - Repetitive lines indicate standard batch sizes (12, 24, 48) and fixed price points.
        """
    )

    visualization_block(
        "img10.jpeg",
        "QQ Plot of Log-Transformed Positive Total Sales",
        "QQ Plot of Log-Transformed Positive Total Sales",
        """
        This QQ plot tests the normality of log-transformed sales data.<br>
        - Most data points align with the red theoretical line, confirming near-normal distribution in the center.<br>
        - The S-shaped deviation at the tails suggests leptokurtic behavior with more extreme highs and lows than expected in a perfect normal distribution.
        """
    )


with tab5:
    st.header("🔎 Model Evaluation")
    st.write("Below we summarize the performance and insights of the different models applied in this project.")

    # ------------------ K-Means Clustering ------------------
    st.subheader("1️⃣ K-Means Clustering")
    st.write("""
    **Purpose:** Cluster customers based on historical behavior to predict **Next Purchase Day**.  
    **Why chosen:** Good for grouping customers with similar patterns, easy to interpret, works well with numeric features.  
    **Assumptions:** Euclidean distance metric, features are scaled, clusters are convex/spherical.  
    **Hyperparameter tuning:** Optimized `k` using the Elbow method.  
    **Challenges & Solutions:** Sensitive to outliers → applied scaling and removed extreme anomalies.
    """)

    kmeans_metrics_df = pd.DataFrame({
        "Metric": ["Silhouette Score", "Davies-Bouldin Index", "Inertia (WCSS)"],
        "Value": [0.62, 0.48, 1200.34]
    })
    st.write("#### Evaluation Metrics")
    st.write(kmeans_metrics_df)

    # ------------------ Random Forest Classifier ------------------
    st.subheader("2️⃣ Random Forest Classifier")
    st.write("""
    **Purpose:** Predict **delivery/response time** or customer segments based on features.  
    **Why chosen:** Handles non-linear data well, reduces overfitting compared to a single tree, often increases accuracy, F1-score, and ROC-AUC.  
    **Assumptions:** Features are relevant; model can handle multicollinearity.  
    **Hyperparameter tuning:** Number of trees (`n_estimators`), maximum depth (`max_depth`).  
    **Challenges & Solutions:** High-dimensional data → reduced features using feature selection.
    """)

    rf_metrics_df = pd.DataFrame({
        "Metric": ["MAE (days)", "MSE", "RMSE (days)", "R²-score"],
        "Value": [21.43, 686.81, 26.21, 0.88]
    })
    st.write("#### Evaluation Metrics")
    st.write(rf_metrics_df)

    rf_fi_df = pd.DataFrame({
        "Feature": ["Recency", "Revenue", "Frequency"],
        "Importance": [0.9750, 0.0128, 0.0122]
    })
    st.write("#### Feature Importance")
    st.write(rf_fi_df)

    # ------------------ Decision Tree Classifier ------------------
    st.subheader("3️⃣ Decision Tree Classifier")
    st.write("""
    **Purpose:** Classify customers into segments using **RFM features**.  
    **Why chosen:** Interpretable decision rules, handles categorical and numeric data, low preprocessing.  
    **Assumptions:** No strong assumptions about data distribution.  
    **Hyperparameter tuning:** `max_depth`, `min_samples_split`, `min_samples_leaf`.  
    **Challenges & Solutions:** Imbalanced classes → applied class weighting and stratified split.
    """)

    dt_metrics_df = pd.DataFrame({
        "Metric": ["Accuracy", "Precision", "Recall", "F1-score", "ROC-AUC"],
        "Value": [0.88, 0.80, 0.83, 0.81, 0.948]
    })
    st.write("#### Evaluation Metrics")
    st.write(dt_metrics_df)

    st.write("""
    The Decision Tree model performs efficiently based on **ROC-AUC score of 0.948**, showing the ability to distinguish retained vs non-retained customers.  
    Although precision for retained customers is lower, the recall is high — the model will successfully identify most customers who are at risk, which is crucial for retention strategies.
    """)

    # ------------------ Apriori / Frequent Pattern Mining ------------------
    st.subheader("4️⃣ Apriori Algorithm (Frequent Pattern Mining)")
    st.write("""
    **Purpose:** Identify frequent itemsets and associations in retail transactions.  
    **Why chosen:** Suitable for transactional data, interpretable, helps in cross-selling and promotion strategies.  
    **Assumptions:** Data is categorical (items purchased), sufficient transaction support exists.  
    **Hyperparameter tuning:** Minimum support (`min_support`) and confidence thresholds (`min_confidence`).  
    **Challenges & Solutions:** Large number of itemsets → filtered only top rules with high support and lift.
    """)

    apriori_rules_df = pd.DataFrame({
        "Rule": [
            "(ROSES REGENCY TEACUP AND SAUCER) → (GREEN REGENCY TEACUP AND SAUCER)",
            "(HEART OF WICKER LARGE) → (HEART OF WICKER SMALL)",
            "(JUMBO BAG RED RETROSPOT) → (JUMBO BAG PINK POLKADOT)"
        ],
        "Support": [0.0365, 0.043, 0.0268],
        "Confidence": [0.7085, 0.5081, 0.2919],
        "Lift": [24.51, 11.32, 9.67]
    })
    st.write("#### Sample Association Rules")
    st.write(apriori_rules_df)

    st.write("""
    In Apriori, a **lift of 10+** indicates very strong relationships between products — showing that certain items are frequently purchased together.  
    This model can be leveraged to **recommend products to users** based on items they select.
    """)

    # ------------------ Comparisons Between Models ------------------
    st.subheader("📊 Comparisons Between Models")
    st.write("""
    - **Decision Tree vs Random Forest:**  
      Random Forest improves upon a single Decision Tree by reducing overfitting, handling non-linear relationships, and often achieving higher Accuracy, F1-score, and ROC-AUC.  
      Both models are interpretable, but Random Forest provides more robust performance on unseen data.

    - **Classification vs Clustering:**  
      Classification models (Decision Tree, Random Forest) focus on predicting known labels (e.g., retained vs non-retained customers) using labeled data.  
      Clustering models (K-Means) identify patterns and group similar customers without prior labels.  
      Use case depends on business need: prediction vs segmentation.

    - **Classification vs Frequent Pattern Mining:**  
      Classification helps in targeted retention strategies, while Apriori uncovers cross-selling opportunities.  
      High recall in the Decision Tree ensures most at-risk customers are identified.  
      Apriori’s high lift (>10) shows strong item associations, enabling product recommendations.

    - **Key Insight:**  
      Each model addresses a specific aspect of the dataset:
        - **K-Means:** Customer segmentation  
        - **Random Forest:** Robust predictive performance  
        - **Decision Tree:** Interpretability and retention targeting  
        - **Apriori:** Market basket insights and product recommendations
    """)

    # --- Results Tab ---
with tab6:
    st.header("🏆 Results")
    st.write("Below are the results of each model implemented on our dataset.")
    st.info("""
        #### K-Means Clustering (Customer Segmentation & Next Purchase Prediction)

        - Identified clear customer groups such as high-value buyers, occasional shoppers and inactive users.  
        - The Elbow method and scaling improved the separation of clusters for more reliable segmentation.  
        - Helps businesses run targeted marketing and predict when a customer is likely to make their next purchase.  
        - Supports better customer engagement and stronger personalization strategies.
        """)

    st.info("""
        #### Random Forest Classifier (Response Time / Segment Prediction)

        - Delivered strong accuracy, recall and F1-score for predicting customer behavior.  
        - Feature importance revealed key factors such as Monetary value, Frequency and Country.  
        - Helps in prioritizing influential behavioral features for improved planning and decision-making.  
        - Useful for predicting customer segments or delivery response times with high reliability.
        """)

    st.info("""
        #### Decision Tree Classifier (RFM-Based Customer Classification)

        - Achieved a high ROC-AUC score of 0.948, showing excellent separation of retained vs non-retained customers.  
        - High recall for at-risk customers ensures early detection for churn-prevention programs.  
        - Simple if-else rules make the model easy to interpret and apply directly in business workflows.  
        - A strong tool for understanding how Recency, Frequency and Monetary metrics influence customer retention.
        """)

    st.info("""
        #### Apriori Algorithm (Market Basket Analysis)

        - Revealed strong product associations, with many rules showing lift values above 10.  
        - Helps retailers identify frequently purchased product pairs for bundling and cross-selling.  
        - Useful for optimizing store layout, running targeted promotions and offering personalized recommendations.  
        - Enhances understanding of purchasing patterns and product relationships across the catalog.
        """)

    st.header("📊 Conclusions")
    st.write("The Retail Stores Analysis project demonstrates how data-driven methods can significantly enhance decision-making across multiple areas of retail operations. By combining segmentation, prediction, classification, and association rule mining, the project delivers insights that are meaningful for several key stakeholders.")
    st.info("""
    #### Retail Impact

    - Better customer understanding: The segmentation and churn models help identify high-value customers, at-risk customers and inactive groups.  
    - Improved sales strategy: Insights from the Apriori model support effective product bundling and targeted promotions.  
    - Optimized inventory planning: Forecast trends and customer behavior help reduce understocking and overstocking issues.  
    - Efficient resource allocation: Random Forest and Decision Tree models highlight the most influential behavioral features for better decision-making.  
    - Higher profitability: Data-driven insights reduce waste, increase retention and improve marketing efficiency.  
    """)

    st.info("""
    #### Customer Experience

    - Personalized recommendations: Strong product associations enable more relevant suggestions instead of random recommendations.  
    - Better product availability: Forecasting and clustering ensure popular items stay in stock.  
    - Improved shopping experience: Pricing and promotions can be tailored based on purchasing patterns.  
    """)

    st.info("""
    #### Supply Chain & Logistics

    - Stronger planning: Demand patterns help teams coordinate better with warehouses and transport partners.  
    - Reduced waste: Especially helpful for items with expiration constraints or seasonal demand.  
    - Balanced logistics: Forecasting prevents sudden workload spikes and stockouts during peak seasons.  
    """)

    st.info("""
    #### Research & Data Science
            
    - Real-world experimentation: This project demonstrates practical use of RFM analysis, classification models, and association rule mining.  
    - Opportunity for innovation: Future work can involve dynamic segmentation, deep-learning forecasting, or ensemble hybrid models.  
    - Benchmark dataset: Retail data can be repurposed for similar studies in healthcare, finance, or manufacturing.  
    """)

    st.info("""
    #### Final Summary

    This project highlights how combining segmentation, forecasting, classification, and association mining provides a complete understanding of retail behavior.  
    These insights support better business decisions, improved customer satisfaction, stronger supply chains, and new opportunities for research and innovation.
    """)


    # --- Global Styling for Visualization Blocks ---
    st.markdown("""
        <style>
            .viz-block {
                display: flex;
                align-items: center;
                gap: 3px;
                background-color: #1E2D41;
                padding: 3px;
                border-radius: 3px;
                margin-bottom: 3px;
            }
            .viz-text {
                color: white;
                font-size: 16px;
                line-height: 1.6;
            }
        </style>
    """, unsafe_allow_html=True)

    # --- Visualization Block Template ---
    def visualization_block(image_path, caption, title, description):
    # Inject adaptive CSS styles for both light and dark themes
        st.markdown("""
            <style>
            .viz-block {
                border-radius: 12px;
                padding: 16px;
                background-color: var(--background-color);
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .viz-text {
                color: var(--text-color);
                font-size: 16px;
                line-height: 1.5;
            }
            </style>
        """, unsafe_allow_html=True)

        # Layout
        with st.container():
            st.markdown('<div class="viz-block">', unsafe_allow_html=True)
            col1, col2 = st.columns([1.3, 2])
            with col1:
                st.image(image_path, caption=caption, use_container_width=True)
            with col2:
                st.subheader(title)
                st.markdown(f'<div class="viz-text">{description}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)




with tab7:
    st.header("🪄 Product Recommender System")
    st.write('''
             This recommendation system analyzes the item a user selects and predicts other products they are likely to buy based on past purchasing patterns. By learning which items are frequently bought together and how customers behave, the system suggests relevant, complementary products to improve the shopping experience and guide smarter purchasing decisions.
             ''')

    query = st.text_input("Enter a product keyword (e.g., mug, toy, bag)")

    if st.button("Get Recommendations"):
        if query.strip() != "":
            result = recommend(query)
            st.write(result)
        else:
            st.warning("Please enter a product name.")

