Phase 3: Project Design

1. Introduction

The Project Design phase explains the structure and working process of the PocketSmart AI application. It describes how the user provides input and how the application calculates and displays the budget results.

2. System Architecture

The application follows a simple input-process-output model.

- Input: User name, monthly income, and expense details.
- Processing: Calculate total expenses and remaining balance.
- Recommendation: Generate a basic savings recommendation based on the remaining balance.
- Output: Display the budget summary on the screen.

3. Input Design

The application collects the following information from the user:

- Name
- Monthly income
- Food expenses
- Travel expenses
- Shopping expenses
- Education expenses
- Other expenses

4. Process Design

1. Start the application.
2. Enter the user's name.
3. Enter the monthly income.
4. Enter expenses for each category.
5. Click the Calculate Budget button.
6. Calculate the total expenses.
7. Calculate the remaining balance.
8. Display the budget summary and recommendation.

5. Output Design

The application displays:

- Total Expenses
- Remaining Balance
- Savings Recommendation
- Budget Summary

6. Calculation Design

Total Expenses = Food + Travel + Shopping + Education + Other

Remaining Balance = Monthly Income - Total Expenses

If the remaining balance is positive, the application displays a positive balance message and savings recommendation. Otherwise, it displays an appropriate warning or budget message.

7. User Interface Design

The application is developed using Streamlit. It provides text input for the user's name, number inputs for income and expenses, and a button to calculate the budget. Results are displayed clearly on the application page.

8. Conclusion

The design provides a clear structure for developing PocketSmart AI. It defines the input fields, calculation process, recommendation logic, and output display.
flowchart TD
    A([Start]) --> B[Enter Name and Monthly Income]
    B --> C[Enter Expense Details]
    C --> D[Click Calculate Budget]
    D --> E[Calculate Total Expenses]
    E --> F[Calculate Remaining Balance]
    F --> G[Display Budget Summary]
    G --> H[Show Recommendation]
    H --> I([End])