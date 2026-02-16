import streamlit as st
import psycopg2
import pandas as pd

# Page Title
st.set_page_config(layout="wide")

st.title("📊 Adhaar Enrollment Analytics Dashboard")
st.markdown("### Interactive analysis of enrollment trends and demographics for the year 2025. \n This dataset originates from the Central Identities Data Repository (CIDR), which is a centralized database maintained by the Unique Identification Authority of India (UIDAI)")
st.markdown("---")




# Database connection function
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Adhaar_enrollment",
        user="postgres",
        password="postgresql@123"
    )

# Connect
conn = get_connection()

# Query for displaying total state enrollment
query = "SELECT * FROM v_state_total_enrollment"
df_state = pd.read_sql(query, conn)


# --------------------------------------
#  SIDEBAR

st.sidebar.markdown("## Filters")
st.sidebar.markdown("---")


# Load list of states
states = pd.read_sql(
    "SELECT DISTINCT state FROM enrollment ORDER BY state",
    conn
)

selected_state = st.sidebar.selectbox(
    "Select State",
    options=["All"] + states["state"].tolist()
)

# ------------------------------------------
# If 'all' is selected then what to show

if selected_state == "All":

    # Key Performance Insights - KPI
    enrollments = df_state["enrollments"].sum()
    st.metric("Total Enrollments in 2025", f"{enrollments:,.0f} ✔")
    st.markdown("---")


    # Insights
    st.subheader("📌 Key Insights")

    st.info("📅 September recorded the highest enrollments during the year.")
    st.success("🏆 Uttar Pradesh contributed the highest enrollments in 2025.")
    st.info("🚀 July showed the strongest month-over-month growth.")
    st.success("👶 The 0-5 age segment dominates overall enrollments.")


    st.markdown("---")

    # Show data
    # show state ranking chart
    st.subheader("State-wise Total Enrollment")
    st.markdown("##### 📈 Trend Analysis")

    st.bar_chart(df_state.set_index("state")["enrollments"])

    # --------------------------------------

    #  Loading Month over Month growth rate
    df_mom = pd.read_sql("SELECT * FROM v_monthly_growth", conn)

    # --------------------------------------
    # calculates percentage growth rate
    df_mom["growth_pct"] = (
        (df_mom["total"] - df_mom["prev_month"])
        / df_mom["prev_month"]
    ) * 100
    df_mom["growth_pct"] = df_mom["growth_pct"].round(4)

    st.markdown("---")

    # ----------------------------------------
    #  2 column layout for monthly growth rate and trend analysis
 
    col1, col2 = st.columns([2,1])
    with col1:
        # Line chart for current and prev month data
        st.subheader("📈 Monthly Growth Rate")
        st.line_chart(df_mom.set_index("month")[["prev_month", "total"]])

    with col2:
        #  Graph for month over month growth 
        st.subheader("📈 Trend Analysis")
        st.line_chart(df_mom.set_index("month")["growth_pct"])

    
    # --------------------------------------------
    #  KPI for monthly growth rate
    col1, col2, col3 = st.columns(3)

    latest = df_mom.iloc[-1]

    col1.metric("✅ Current Month Total", f"{latest['total']:,}")
    col2.metric("✅ Previous Month", f"{latest['prev_month']:,}")
    col3.metric("✅ Growth %", f"{latest['growth_pct']}%")

    # ---------------------------------------------
    

    st.markdown("---")
    

    # --------------------------------------------------


        #  Age Wise distribution
    if selected_state == "All":
        query_age = """
            SELECT '0-5' AS age_group, SUM(age_0_5) AS total FROM enrollment
            UNION ALL
            SELECT '5-17', SUM(age_5_17) FROM enrollment
            UNION ALL
            SELECT '18+', SUM(age_18_greater) FROM enrollment
        """
    else:
        query_age = f"""
            SELECT '0-5' AS age_group, SUM(age_0_5) AS total 
            FROM enrollment
            WHERE state = '{selected_state}'
            
            UNION ALL
            
            SELECT '5-17', SUM(age_5_17)
            FROM enrollment
            WHERE state = '{selected_state}'
            
            UNION ALL
            
            SELECT '18+', SUM(age_18_greater)
            FROM enrollment
            WHERE state = '{selected_state}'
        """

    df_age = pd.read_sql(query_age, conn)

    st.subheader("The Age-wise Distribution")
    st.bar_chart(df_age.set_index("age_group")["total"])


else:

    # ---------------------------------------------
    # display heading and selected state name

    st.markdown(f"### Selected State: {selected_state}")


    # -------------------------
    #  Showing Kpi and making kpi query dynamic
    if selected_state == "All":
        query_kpi = """
            SELECT SUM(total_enrollment) AS total
            FROM enrollment
        """
    else:
        query_kpi = f"""
            SELECT SUM(total_enrollment) AS total
            FROM enrollment
            WHERE state = '{selected_state}'
        """

    df_kpi = pd.read_sql(query_kpi, conn)

    total_enrollment = df_kpi["total"].iloc[0]

    st.metric("Total Enrollment", f"{int(total_enrollment):,} ✔")


    # -------------------------------
    # showing monthly data and making monthly trend query dynamic 
    if selected_state == "All":
        query_month = """
            SELECT month,
                SUM(total_enrollment) AS total
            FROM enrollment
            GROUP BY month
            ORDER BY month
        """
    else:
        query_month = f"""
            SELECT month,
                SUM(total_enrollment) AS total
            FROM enrollment
            WHERE state = '{selected_state}'
            GROUP BY month
            ORDER BY month
        """

    df_month = pd.read_sql(query_month, conn)

    peak_row = df_month.loc[df_month["total"].idxmax()]
    peak_month = peak_row["month"]
    peak_value = peak_row["total"]
    st.info(f"📅 {peak_month}th month recorded the highest enrollment volume with {int(peak_value):,} enrollments.")







    # -----------------------------------
    # Top 5 District query
    st.markdown("---")
    

    if selected_state == "All":
        query_district = """
            SELECT district,
                SUM(total_enrollment) AS total
            FROM enrollment
            GROUP BY district
            ORDER BY total DESC
            LIMIT 5
        """
    else:
        query_district = f"""
            SELECT district,
                SUM(total_enrollment) AS total
            FROM enrollment
            WHERE state = '{selected_state}'
            GROUP BY district
            ORDER BY total DESC
            LIMIT 5
        """

    df_district = pd.read_sql(query_district, conn)


    # -------------------------------------------------------
    #  2 Column Layout for monthly trends and top 5 districts

    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader(" 📈 Monthly Trend")
        st.line_chart(df_month.set_index("month")["total"])

    with col2:
        st.subheader("📍 Top 5 District Insights")
        st.bar_chart(df_district.set_index("district")["total"])

    # --------------------------------------------------------

        #  Age Wise distribution
    if selected_state == "All":
        query_age = """
            SELECT '0-5' AS age_group, SUM(age_0_5) AS total FROM enrollment
            UNION ALL
            SELECT '5-17', SUM(age_5_17) FROM enrollment
            UNION ALL
            SELECT '18+', SUM(age_18_greater) FROM enrollment
        """
    else:
        query_age = f"""
            SELECT '0-5' AS age_group, SUM(age_0_5) AS total 
            FROM enrollment
            WHERE state = '{selected_state}'
            
            UNION ALL
            
            SELECT '5-17', SUM(age_5_17)
            FROM enrollment
            WHERE state = '{selected_state}'
            
            UNION ALL
            
            SELECT '18+', SUM(age_18_greater)
            FROM enrollment
            WHERE state = '{selected_state}'
        """

    df_age = pd.read_sql(query_age, conn)

    st.subheader("👶 Age-wise Distribution")
    st.bar_chart(df_age.set_index("age_group")["total"])

    




conn.close()

