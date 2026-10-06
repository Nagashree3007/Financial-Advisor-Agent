# Intelligent Personal Finance Advisor Agent

## Project Overview

The Intelligent Personal Finance Advisor Agent is an AI-powered financial management application that helps users monitor, analyze, and improve their financial health through intelligent insights and recommendations.

The system enables users to track income, expenses, budgets, investments, and financial goals while providing personalized financial guidance through a conversational AI assistant.

Built using FastAPI, Streamlit, LangChain, and LangGraph, the application combines financial analytics with AI-driven decision-making to create a simple and effective personal finance management platform.

---

## Key Features

- User profile management
- Income tracking and analysis
- Expense management
- Budget planning and monitoring
- Financial goal tracking
- Investment portfolio management
- Transaction history management
- Financial report generation
- AI-powered conversational assistant
- Personalized financial recommendations
- Spending pattern analysis
- CSV data upload and processing
- Conversation history storage

---

## Technologies Used

### Backend
- Python
- FastAPI
- Pydantic

### Frontend
- Streamlit

### AI Frameworks
- LangChain
- LangGraph

### Data Processing
- Pandas

### Storage
- CSV Files
- JSON Files

---

## Project Architecture

```text
┌─────────────────────┐
│      Streamlit      │
│      Frontend       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       FastAPI       │
│      Backend API    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Service Layer     │
│ Business Logic      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Repository Layer    │
│ Data Management     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ CSV / JSON Storage  │
└─────────────────────┘

           │
           ▼

┌─────────────────────┐
│ LangChain +         │
│ LangGraph Agent     │
└─────────────────────┘
```

---

## Project Structure

```text
Financial-Advisor-Agent/
│
├── app/
│   ├── api/
│   ├── agents/
│   ├── graph/
│   ├── repository/
│   ├── services/
│   ├── tools/
│   ├── prompts/
│   ├── models/
│   ├── schemas/
│   ├── middleware/
│   ├── utils/
│   ├── storage/
│   │   ├── users.csv
│   │   ├── income.csv
│   │   ├── expenses.csv
│   │   ├── investments.csv
│   │   ├── goals.csv
│   │   ├── budgets.csv
│   │   ├── transactions.csv
│   │   ├── reports/
│   │   └── conversation_history.json
│   │
│   ├── logs/
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

## Running the Application

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### 3. Start Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## API Endpoints

### Chat & AI Services

```http
POST /chat
```

### User Data

```http
GET /users
```

### Income Data

```http
GET /income
```

### Expense Data

```http
GET /expenses
```

### Transactions

```http
GET /transactions
```

### Budget Management

```http
GET /budgets
```

### Financial Goals

```http
GET /goals
```

### File Upload

```http
POST /upload-csv
```

### Health Check

```http
GET /health
```

---

## Example User Queries

- How much did I spend this month?
- What is my total income?
- Am I exceeding my budget?
- Which category has the highest expenses?
- How much can I save this month?
- Show my investment portfolio summary.
- Analyze my spending habits.
- Generate a financial report.
- Suggest ways to reduce expenses.
- Provide personalized financial advice.

---

## Data Storage

The application currently uses local CSV and JSON files for storing:

- Users
- Income Records
- Expense Records
- Transactions
- Budgets
- Investments
- Financial Goals
- Conversation History
- Generated Reports

---

## Future Enhancements

- Database integration (PostgreSQL/MySQL)
- User authentication and authorization
- Multi-user support
- Real-time expense tracking
- Email report generation
- Cloud deployment (Azure/AWS)
- Advanced investment analysis
- Financial forecasting
- Mobile application support

---

## Conclusion

The Intelligent Personal Finance Advisor Agent demonstrates the integration of FastAPI, Streamlit, LangChain, and LangGraph to build an intelligent personal finance management platform.

The application helps users track income, monitor expenses, manage budgets, analyze spending behavior, maintain financial goals, and receive AI-driven insights through an interactive conversational interface, making personal finance management simpler and more effective.
