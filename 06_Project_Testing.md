Phase 6: Project Testing

1. Introduction

The Project Testing phase checks whether the PocketSmart AI application works correctly. Testing helps identify errors and verify that the budget calculations and recommendations produce the expected results.

2. Objectives of Testing

- Verify the income and expense inputs.
- Check the total expense calculation.
- Check the remaining balance calculation.
- Verify the recommendation messages.
- Identify errors and improve reliability.

3. Testing Method

Manual testing is used by entering different sample values into the application and comparing the displayed results with the expected results.

4. Test Cases

Test Case| Input / Condition| Expected Result
TC01| Enter a valid name| Name is accepted
TC02| Income = ₹20,000; expenses total ₹10,000| Remaining balance = ₹10,000
TC03| Income = ₹15,000; expenses total ₹15,000| Remaining balance = ₹0
TC04| Income = ₹10,000; expenses total ₹12,000| Remaining balance = -₹2,000
TC05| Enter expenses in all five categories| Total expenses equal the sum of all categories
TC06| Enter zero expenses| Total expenses = ₹0
TC07| Enter a negative income or expense| Input should be rejected if validation is implemented

5. Sample Calculation

Monthly Income = ₹20,000

- Food = ₹3,000
- Travel = ₹2,000
- Shopping = ₹1,500
- Education = ₹2,500
- Other = ₹1,000

Total Expenses = ₹10,000

Remaining Balance = ₹20,000 - ₹10,000 = ₹10,000

Expected Result: The application displays total expenses of ₹10,000 and a remaining balance of ₹10,000.

6. Error Handling

Invalid inputs, such as non-numeric values or negative amounts, should be handled appropriately. Input validation must be implemented in the application for these checks to pass.

7. Testing Results

Record the actual result of each test after running the application. Mark each test as Pass or Fail based on whether the actual result matches the expected result.

8. Conclusion

Testing helps verify the accuracy of PocketSmart AI's budget calculations and identify areas that need improvement. The application should be considered tested only after the test cases have been executed and their results recorded.
