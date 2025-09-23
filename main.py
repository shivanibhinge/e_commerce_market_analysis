import streamlit as st
import pandas as pd

# Define the data for team members
team_data = {
    'Name': ['Shivani Bhinge', 'Vinay Chandra Konda', 'Sanika Gidye', 'Shakthi'],
    'Role': ['Data Lead', 'Visualization, WebDev', 'Modeling Lead', 'Developer'],
    'Contribution': [
        'Managed project timelines',
        'Developed analysis models',
        'Built the website and analysis',
        'Handled backend tasks and analysis'
    ],
    'Picture': [
        'https://media.licdn.com/dms/image/v2/D4D03AQEr39coxWKsoA/profile-displayphoto-crop_800_800/B4DZjfup6.HwAM-/0/1756100210989?e=1761177600&v=beta&t=-Yoi2WzXsCJMNxoKK0-cDwVdypoMuZlAYbYiTUaT63k',
        'https://media.licdn.com/dms/image/v2/D5603AQEvP3s_jFmc6A/profile-displayphoto-crop_800_800/B56ZlzwliwIAAI-/0/1758583740907?e=1761177600&v=beta&t=9uia_mxeDh9QYuOwUedEy63roW-bHaWQpV1uUvtgQas',
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
        'https://github.com/shakthi'
    ]
}

# Create a DataFrame
df_team = pd.DataFrame(team_data)

st.set_page_config(page_title="The Retail Compass", page_icon="📈", layout="wide")

st.markdown(
    '<h1 style="color: #D17F43; font-weight: 800; font-size: 5em; font-family: roboto;">The Retail Compass</h1>',
    unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Introduction", "Team", "Overview"])

# --- Introduction Tab ---
with tab1:
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.header("Introduction")
        st.markdown(
            """
            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
                <p style="color: #000000; margin-bottom: 20px;">
                Welcome to the Retail Stores Analysis project. This initiative aims to provide
                in-depth insights into retail store performance.
                Our analysis covers key metrics such as sales trends, customer demographics,
                and market share to help businesses make data-driven decisions.
                </p>
                <p style="color: #000000;">
                The project utilizes a comprehensive dataset that includes information from
                retail chains from across different countries such as United States, United Kingdom, and Japan. By examining
                these different markets, we can identify regional trends and opportunities
                for growth.
                </p>
            </div>
            <br>

            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
            <h4 style="color: #2196F3;">Project Focus</h4>
            <p style="color: #000000; margin-bottom: 20px;">Customer and Market analysis within the e-commerce sector. The core focus of the research is customer segmentation using RFM (Recency, Frequency, Monetary) analysis and exploratory analysis of the product pricing strategies.</p>
            <h5 style="color: #2196F3;">Why is it important:</h5>
            <ul style="list-style-type: none; padding: 0; color: #000000;">
                <li style="margin-bottom: 5px;">Actionable Business insights: By applying the RFM analysis, the project can help the online retailers to identify and cluster customers based on distinct groups. This data-driven foundation is useful for developing targeted marketing strategies, customer retention, stock analysis eventually adding value to customer experience and overall profitability.</li>
                <li style="margin-bottom: 5px;">Strategic planning and inventory management: Understanding how product prices are set and how they vary across different years. These insights will help in managing inventory and optimizing companies revenue.</li>
            </ul>
            </div>
            <br>

            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
            <h4 style="color: #2196F3;">Stakeholders (Who is Affected?)</h4>
            <p style="color: #000000;">Which industries, groups, or individuals are impacted by this issue? What are the real-world implications?</p>
            <ul style="list-style-type: none; padding: 0; color: #000000;">
                <li style="margin-bottom: 5px;">The Business (the retailer):This is the core stakeholder. Its impacted by sales volume, revenue, profitability, inventory management, and customer retention.</li>
                <li style="margin-bottom: 5px;">Customers: These are the individuals making purchases. They are affected by product availability, pricing, shipping costs, delivery times, and the quality of customer service.</li>
                <li style="margin-bottom: 5px;">Suppliers: These are the companies providing the products. Their relationship with the retailer is impacted by purchase orders, payment schedules, and demand for their goods.</li>
                <li style="margin-bottom: 5px;">Logistics and Shipping Companies: These companies are responsible for delivering goods. Their business is directly tied to the volume and geographical spread of the retailer's sales. The international nature of the sales (e.g., to countries like France, Germany, EIRE, and Norway as seen in the data) highlights the involvement of international logistics partners.</li>
            </ul>
            </div>
            <br>

            <div style="background-color: #e6f7ff; padding: 20px; border-radius: 10px;">
            <h4 style="color: #2196F3;">Existing Solutions & Gaps</h4>
            <p style="color: #000000;">What solutions currently exist? What limitations or challenges remain?</p>
            <br>
            <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #2196F3;">
                <h5 style="color: #2196F3;">Paper 1: A Stacking Approach to Customer Lifetime Value (CLV) Prediction</h5>
                <p style="color: #000000;">Link: <a href="https://arxiv.org/pdf/2308.08502" style="color: #000000;">https://arxiv.org/pdf/2308.08502</a></p>
                <p style="color: #000000;"><strong>Current Solution:</strong> A two-stage model uses a number of algorithms (Random Forest, XGBoost, ElasticNet) and a final model that combines their predicted values to produce more accurate CLV forecasting.</p>
                <p style="color: #000000;"><strong>Strengths:</strong> More precise using the ensemble of various models; utilizes a rich feature set instead of RFM alone.</p>
                <p style="color: #000000;"><strong>Limitations:</strong> Computationally demanding and convoluted; "black box" solution difficult to interpret; requires a lot of data.</p>
            </div>
            <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #2196F3;">
                <h5 style="color: #2196F3;">Paper 2: Customer-Focused Sales Forecasting Model: RFM-ARIMA Methodology</h5>
                <p style="color: #000000;">Link: <a href="https://sciendo.com/article/10.2478/bsrj-2022-0003?utm_" style="color: #000000;">https://sciendo.com/article/10.2478/bsrj-2022-0003</a></p>
                <p style="color: #000000;"><strong>Current Solution:</strong> A combination solution that first uses RFM analysis in customer segmentation and elimination of noise before ARIMA is used on sales data.</p>
                <p style="color: #000000;"><strong>Strengths:</strong> Maximizes accuracy and model fit by reducing data noise.</p>
                <p style="color: #000000;"><strong>Limitations:</strong> Restricted for non-linear trend analysis and external factors like seasonality; reliant on large customer buy history data.</p>
            </div>
            <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #2196F3;">
                <h5 style="color: #2196F3;">Paper 3: Development of a Retailer Forecasting Model Based on Customer Segmentation Using Data Mining Techniques</h5>
                <p style="color: #000000;">Link: <a href="https://www.ijtsrd.com/computer-science/data-miining/19127/developing-a-forecasting-model-for-retailers-based-on-customer-segmentation-using-data-mining-techniques/kayalvizhi-subramanian?utm_" style="color: #000000;">https://www.ijtsrd.com/computer-science/data-miining/19127/...</a></p>
                <p style="color: #000000;"><strong>Current Solution:</strong> Two-stage model that groups customers based on demographic and behavior data and forecasts for each group using a forecasting model.</p>
                <p style="color: #000000;"><strong>Strengths:</strong> Improves inventory performance; is customer-focused; eliminates data redundancy.</p>
                <p style="color: #000000;"><strong>Limitations:</strong> Can be limited in scope; might be limited to neat, small datasets.</p>
            </div>
            <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #2196F3;">
                <h5 style="color: #2196F3;">Paper 4: Research on E-Commerce Inventory Sales Forecasting Model Based on ARIMA and LSTM Algorithm</h5>
                <p style="color: #000000;">Link: <a href="https://www.mdpi.com/2227-7390/13/11/1838?utm_" style="color: #000000;">https://www.mdpi.com/2227-7390/13/11/1838</a></p>
                <p style="color: #000000;"><strong>Current Solution:</strong> Two-model strategy with ARIMA for monthly inventory forecasting and LSTM for daily sales forecasting.</p>
                <p style="color: #000000;"><strong>Strengths:</strong> Novel approach that improves accuracy; offers actionable solution for warehouse planning.</p>
                <p style="color: #000000;"><strong>Weaknesses:</strong> Tested over short time period; LSTMs are prone to overfitting and difficult to interpret; requires large datasets.</p>
            </div>
            </div>
            """
            , unsafe_allow_html=True)

    with col_right:
        st.header("")
        st.image(
            "https://trueprofit.io/_next/image?url=https%3A%2F%2Fbe.trueprofit.io%2Fuploads%2Fretail-store-profitability-analysis.webp&w=2560&q=75",
            use_container_width=True)
        st.image("https://www.gofrugal.com/sites/blog/files/gofrugal/benefits-retail-analytics.jpg",
                 use_container_width=True)
        # st.image("", use_container_width=True)

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
                <p style="font-size: 16px; margin-bottom: 15px; color: #000000;"><strong>Contribution :</strong> {df_team.loc[0, 'Contribution']}</p>
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
                <p style="font-size: 16px; margin-bottom: 15px; color: #000000;"><strong>Contribution :</strong> {df_team.loc[1, 'Contribution']}</p>
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
                <p style="font-size: 16px; margin-bottom: 15px; color: #000000;"><strong>Contribution :</strong> {df_team.loc[2, 'Contribution']}</p>
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
                <p style="font-size: 16px; margin-bottom: 15px; color: #000000;"><strong>Contribution :</strong> {df_team.loc[3, 'Contribution']}</p>
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