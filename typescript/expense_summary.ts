type Expense = { name: string; amount: number };
const expenses: Expense[] = [
  { name: "Hosting", amount: 12 },
  { name: "Domain", amount: 10 },
  { name: "Coffee", amount: 4.5 },
];
const total = expenses.reduce((sum, item) => sum + item.amount, 0);
console.table(expenses);
console.log(`Total: $${total.toFixed(2)}`);
