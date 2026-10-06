from __future__ import annotations

from datetime import datetime
from pathlib import Path
import json
import sys

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.agents.finance_agent import finance_agent
from app.services.container import container
from app.tools.finance_tools import build_finance_tools
from app.utils.data_generator import generate_synthetic_data_if_missing


generate_synthetic_data_if_missing()

st.set_page_config(
    page_title="Smart Financial Planning Assistant",
    page_icon="💰",
    layout="wide",
)

st.markdown(
    """
<style>
.main {
    background-color: #f8fafc;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}

.block-container {
    padding-top: 2rem;
}
</style>
""",
    unsafe_allow_html=True,
)

st.title("💰 FinSight AI")
st.caption("AI Powered Personal Finance Assistant")

users = container.repository.get_users()

user_map = {
    f"{u['user_id']} - {u['name']}": u["user_id"]
    for u in users
}

finance = container.finance_service
tools = build_finance_tools()

# ================= SIDEBAR =================

with st.sidebar:

    st.header("👤 User Profile")

    selected_user_label = st.selectbox(
        "Select User",
        list(user_map.keys())
    )

    selected_user = user_map[selected_user_label]

    selected_month = st.text_input(
        "Month (YYYY-MM)",
        value=datetime.today().strftime("%Y-%m")
    )

# ================= TABS =================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📊 Dashboard",
        "🤖 AI Advisor",
        "💵 Budget & Savings",
        "📈 Investments",
        "📑 Reports",
    ]
)

# =========================================================
# DASHBOARD
# =========================================================

with tab1:

    st.subheader("Financial Overview")

    totals = container.repository.calculate_totals(
        selected_user,
        selected_month,
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Income",
        f"₹{totals['total_income']:,.0f}"
    )

    col2.metric(
        "Expenses",
        f"₹{totals['total_expense']:,.0f}"
    )

    col3.metric(
        "Savings",
        f"₹{totals['savings']:,.0f}"
    )

    col4.metric(
        "Savings Rate",
        f"{totals['savings_rate']:.1f}%"
    )

    st.divider()

    charts = finance.create_charts(
        selected_user,
        selected_month
    )

    left, right = st.columns(2)

    with left:
        st.subheader("Expense Trends")

        if "monthly_expenses" in charts:
            st.pyplot(charts["monthly_expenses"])

    with right:
        st.subheader("Income vs Expenses")

        if "income_vs_expense" in charts:
            st.pyplot(charts["income_vs_expense"])

# =========================================================
# AI ADVISOR
# =========================================================

with tab2:

    st.subheader("🤖 Personal Finance Advisor")

    question = st.chat_input(
        "Ask a finance question..."
    )

    if question:

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):

            with st.spinner("Analyzing your finances..."):

                try:

                    result = finance_agent.chat(
                        selected_user,
                        question,
                    )

                    st.write(
                        result.get(
                            "answer",
                            "No answer generated."
                        )
                    )

                    with st.expander(
                        "Analysis Details"
                    ):
                        st.json(
                            result.get(
                                "analysis",
                                {}
                            )
                        )

                except Exception as exc:
                    st.error(exc)

# =========================================================
# BUDGET & SAVINGS
# =========================================================

with tab3:

    st.subheader("Budget & Savings")

    budget = finance.budget_status(
        selected_user,
        selected_month,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Budget Limit",
        f"₹{budget['budget_limit']:,.0f}"
    )

    c2.metric(
        "Spent",
        f"₹{budget['spent']:,.0f}"
    )

    c3.metric(
        "Usage %",
        f"{budget['usage_pct']:.1f}%"
    )

    if budget["is_exceeded"]:
        st.error("⚠ Budget Exceeded")
    else:
        st.success("✅ Within Budget")

    st.divider()

    st.subheader("Recommendations")

    recommendations = finance.personalized_recommendations(
        selected_user,
        selected_month,
    )

    for recommendation in recommendations:
        st.write(f"✅ {recommendation}")

# =========================================================
# INVESTMENTS
# =========================================================

with tab4:

    st.subheader("Investment Portfolio")

    investments = finance.investment_summary(
        selected_user
    )

    st.metric(
        "Total Investments",
        f"₹{investments['total']:,.0f}"
    )

    df = pd.DataFrame(
        investments["by_asset"].items(),
        columns=[
            "Asset Type",
            "Amount",
        ],
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    charts = finance.create_charts(
        selected_user,
        selected_month,
    )

    if "investment_allocation" in charts:
        st.pyplot(
            charts["investment_allocation"]
        )

# =========================================================
# REPORTS
# =========================================================

with tab5:

    st.subheader("📑 Monthly Financial Report")

    if st.button("Generate Report"):

        try:

            report_raw = tools[
                "financial_report_generator"
            ].invoke(
                {
                    "user_id": selected_user,
                    "month": selected_month,
                }
            )

            report = json.loads(report_raw)

            st.success("✅ Report generated successfully")

            report_data = report["report"]

            # -------------------------------------------------
            # Financial Summary
            # -------------------------------------------------

            st.subheader("📊 Financial Summary")

            totals = report_data["totals"]

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Income",
                f"₹{totals['total_income']:,.0f}"
            )

            c2.metric(
                "Expense",
                f"₹{totals['total_expense']:,.0f}"
            )

            c3.metric(
                "Savings",
                f"₹{totals['savings']:,.0f}"
            )

            c4.metric(
                "Savings Rate",
                f"{totals['savings_rate']:.1f}%"
            )

            st.divider()

            # -------------------------------------------------
            # Spending Breakdown
            # -------------------------------------------------

            st.subheader("💸 Spending Breakdown")

            spending_df = pd.DataFrame(
                report_data["spending"]["by_category"].items(),
                columns=["Category", "Amount"]
            )

            st.dataframe(
                spending_df,
                use_container_width=True
            )

            # -------------------------------------------------
            # Budget Status
            # -------------------------------------------------

            st.subheader("💰 Budget Status")

            budget = report_data["budget"]

            budget_df = pd.DataFrame(
                [{
                    "Budget Limit": budget["budget_limit"],
                    "Spent": budget["spent"],
                    "Usage (%)": round(
                        budget["usage_pct"],
                        2
                    ),
                    "Exceeded": budget["is_exceeded"]
                }]
            )

            st.dataframe(
                budget_df,
                use_container_width=True
            )

            # -------------------------------------------------
            # Investment Allocation
            # -------------------------------------------------

            st.subheader("📈 Investment Allocation")

            investment_df = pd.DataFrame(
                report_data["investments"]["by_asset"].items(),
                columns=["Asset Type", "Amount"]
            )

            st.dataframe(
                investment_df,
                use_container_width=True
            )

            # -------------------------------------------------
            # Financial Goals
            # -------------------------------------------------

            st.subheader("🎯 Financial Goals")

            goals_df = pd.DataFrame(
                report_data["goals"]
            )

            st.dataframe(
                goals_df,
                use_container_width=True
            )

            # -------------------------------------------------
            # Recommendations
            # -------------------------------------------------

            st.subheader("✅ Recommendations")

            for recommendation in report_data.get(
                "recommendations",
                []
            ):
                st.success(recommendation)

            # -------------------------------------------------
            # Risks
            # -------------------------------------------------

            st.subheader("⚠ Risks")

            risks = report_data.get(
                "risks",
                []
            )

            if risks:
                for risk in risks:
                    st.warning(risk)
            else:
                st.success(
                    "No significant financial risks detected."
                )

        except Exception as exc:
            st.error(
                f"Report generation failed: {exc}"
            )