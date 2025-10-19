import streamlit as st
import pandas as pd

# Define the data for team members
team_data = {
    'Name': ['Shivani Atul Bhinge', 'Vinay Chandra Konda', 'Sanika Gidye', 'Sri Shakthi Aravindan'],
    'Role': ['Machine Learning Lead', 'Data Lead', 'Visualization Lead', 'Analysis Lead'],
    # 'Contribution': [
    #     '',
    #     'Developed analysis models',
    #     'Built the website and analysis',
    #     'Handled backend tasks and analysis'
    # ],
    'Picture': [
        'https://media.licdn.com/dms/image/v2/D4D03AQEr39coxWKsoA/profile-displayphoto-crop_800_800/B4DZjfup6.HwAM-/0/1756100210989?e=1761177600&v=beta&t=-Yoi2WzXsCJMNxoKK0-cDwVdypoMuZlAYbYiTUaT63k',
        'https://media.licdn.com/dms/image/v2/D5603AQGbbo-WEFmKNg/profile-displayphoto-crop_800_800/B56Znv5zNHHIAM-/0/1760666530996?e=1762387200&v=beta&t=LGNxCtoaZNilhqiaKsvAOaPmXP74flOCi78cNSjb91w',
        'https://media.licdn.com/dms/image/v2/D4D03AQGAbti5YEFCRg/profile-displayphoto-shrink_800_800/B4DZeTS4gwGUAc-/0/1750522891490?e=1761177600&v=beta&t=jEt5MuZNDty7R0IA23erpcsZ6wExVzKsucOO3uqiqzg',
        'https://media.licdn.com/dms/image/v2/D5635AQFJBK7NRwLpzw/profile-framedphoto-shrink_800_800/B56ZkHUjm2HUAg-/0/1756764453599?e=1759186800&v=beta&t=bVhV6Y6LzfG2y9GXKA1ev1QXGSv-XYfnzYBnNpJlnY0'
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
tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Team", "Overview", "Data Exploration"])

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
            "https://trueprofit.io/_next/image?url=https%3A%2F%2Fbe.trueprofit.io%2Fuploads%2Fretail-store-profitability-analysis.webp&w=2560&q=75",
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

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px; text-align: center;">
                <h4 style="color: #2196F3; margin-bottom: 10px;">{df_team.loc[0, 'Name']}</h4>
                <img src="{df_team.loc[0, 'Picture']}" style="width: 150px; border-radius: 50%; margin-bottom: 10px;">
                <p style="font-size: 16px; margin-bottom: 5px; color: #000000;"><strong>Role :</strong> {df_team.loc[0, 'Role']}</p>
                <a href="{df_team.loc[0, 'LinkedIn']}" style="background-color: #0077B5; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none; margin-right: 10px;">LinkedIn</a>
                <a href="{df_team.loc[0, 'GitHub']}" style="background-color: #554444; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none;">GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px; text-align: center;">
                <h4 style="color: #2196F3; margin-bottom: 10px;">{df_team.loc[1, 'Name']}</h4>
                <img src="{df_team.loc[1, 'Picture']}" style="width: 150px; border-radius: 50%; margin-bottom: 10px;">
                <p style="font-size: 16px; margin-bottom: 5px; color: #000000;"><strong>Role :</strong> {df_team.loc[1, 'Role']}</p>
                <a href="{df_team.loc[1, 'LinkedIn']}" style="background-color: #0077B5; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none; margin-right: 10px;">LinkedIn</a>
                <a href="{df_team.loc[1, 'GitHub']}" style="background-color: #554444; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none;">GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            f"""
            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px; text-align: center;">
                <h4 style="color: #2196F3; margin-bottom: 10px;">{df_team.loc[2, 'Name']}</h4>
                <img src="{df_team.loc[2, 'Picture']}" style="width: 150px; border-radius: 50%; margin-bottom: 10px;">
                <p style="font-size: 16px; margin-bottom: 5px; color: #000000;"><strong>Role :</strong> {df_team.loc[2, 'Role']}</p>
                <a href="{df_team.loc[2, 'LinkedIn']}" style="background-color: #0077B5; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none; margin-right: 10px;">LinkedIn</a>
                <a href="{df_team.loc[2, 'GitHub']}" style="background-color: #554444; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none;">GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            f"""
            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px; text-align: center;">
                <h4 style="color: #2196F3; margin-bottom: 10px;">{df_team.loc[3, 'Name']}</h4>
                <img src="{df_team.loc[3, 'Picture']}" style="width: 150px; border-radius: 50%; margin-bottom: 10px;">
                <p style="font-size: 16px; margin-bottom: 5px; color: #000000;"><strong>Role :</strong> {df_team.loc[3, 'Role']}</p>
                <a href="{df_team.loc[3, 'LinkedIn']}" style="background-color: #0077B5; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none; margin-right: 10px;">LinkedIn</a>
                <a href="{df_team.loc[3, 'GitHub']}" style="background-color: #554444; color: #ffffff; padding: 8px 12px; border-radius: 5px; text-decoration: none;">GitHub</a>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Project Overview Tab ---
with tab3:
    st.header("Project Overview")
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
