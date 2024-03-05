const ops_set = new Set(["+", "-", "*", "/"]);

function calc(op, n1, n2) {
  switch (op) {
    case "+":
      return n1 + n2;
    case "-":
      return n1 - n2;
    case "*":
      return n1 * n2;
    default:
      return n1 / n2;
  }
}
/*
  The popping instance when you find a right most operator
*/
function calculate(expression) {
  const a = expression.split(" ");
  const st = [];
  for (let i = a.length - 1; i >= 0; i--) {
    st.push(a[i]);
    if (ops_set.has(a[i])) {
      const ans = calc(st.pop(), parseInt(st.pop()), parseInt(st.pop()));
      st.push(ans);
    }
  }
  return st[0];
}
const assert = require("assert");

result = calculate("0");
assert.equal(result, 0);

result = calculate("+ 3 4");
assert.equal(result, 3 + 4);

result = calculate("- 3 * 4 5");
assert.equal(result, 3 - 4 * 5); // -17

result = calculate("* + 3 4 5");
assert.equal(result, (3 + 4) * 5); // 35
