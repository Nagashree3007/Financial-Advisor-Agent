# Intelligent Personal Finance Advisor Agent

## Project Overview

The Intelligent Personal Finance Advisor Agent is an AI-powered application that helps users manage their finances through intelligent analysis and personalized recommendations. The application analyzes income, expenses, budgets, savings, investments, and financial goals to provide valuable financial insights.

The project is built using FastAPI, Streamlit, LangChain, and LangGraph, with local CSV files used for data storage and management.

## Features

- Track income and expenses
- Monitor monthly budgets
- Analyze spending patterns
- Manage financial goals
- View investment summaries
- Generate financial reports
- Personalized financial recommendations
- AI-powered conversational assistant

## Technologies Used

- Python
- FastAPI
- Streamlit
- LangChain
- LangGraph
- Pandas
- CSV & JSON Storage

## Project Structure

```text
finance-advisor/
  app/
    api/
    agents/
    graph/
    repository/
    services/
    tools/
    prompts/
    models/
    schemas/
    middleware/
    utils/
    storage/
      users.csv
      income.csv
      expenses.csv
      investments.csv
      goals.csv
      budgets.csv
      transactions.csv
      reports/
      conversation_history.json
    logs/
    main.py
  frontend/
    streamlit_app.py
  requirements.txt
  README.md
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Start the Streamlit application:

```bash
streamlit run frontend/streamlit_app.py
```

## API Endpoints

- POST /chat
- GET /users
- GET /income
- GET /expenses
- GET /transactions
- GET /budgets
- GET /goals
- POST /upload-csv
- GET /health

## Example Queries

- How much did I spend this month?
- Where am I spending the most money?
- How much can I save?
- Am I exceeding my budget?
- Show my investment summary.
- Analyze my spending habits.
- Generate a financial report.
- Provide personalized financial advice.

## Conclusion

This project demonstrates how AI can be used to support personal finance management by providing intelligent insights, financial analysis, and recommendations through an interactive and user-friendly interface.
