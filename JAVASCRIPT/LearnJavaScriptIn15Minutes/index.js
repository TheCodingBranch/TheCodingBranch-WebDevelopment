var anything = "I Love 🌮🌮🌮";
console.log(anything);

let verdict = false;
console.log("The verdict is " + verdict);
verdict = true;
console.log("Just kidding the verdict is " + verdict);

const zero = 0;
console.log(`${zero} the hero`);

// zero = zero + 7;
// console.log(zero);

const listOfFruit = ["apples", "oranges", "strawberries"];
console.log(listOfFruit);

let num = 0;

// num = num + 1;
// num = num - 1;
// num = num * 2;
// num = num / 2;

num = 5;
num = num % 2;
console.log(num);

while (num < 10) {
  num++;
  console.log(`The num is ${num}`);
}

for (let number = 1; number < 11; number++) {
  console.log(`The number is ${number}`);
}

function countToTen() {
  for (let number = 1; number < 11; number++) {
    // console.log(`The number is ${number}`);
    if (number % 2 === 0 || number === 6) {
      console.log("Number is even");
    } else {
      console.log("Number is odd");
    }
  }
}

countToTen();

const multiplyByTwo = function (functionInput, multiply) {
  functionInput = functionInput * multiply;
  return functionInput;
};

console.log(multiplyByTwo(5, 2));
