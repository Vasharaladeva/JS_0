const arr = [1,2,3];
const arr2 = [...arr,4];

console.log(arr2);

const person = {
    name: 'bambi',
    age: 666
};

const person2 = {
    ...person,
    email: 'qwe@saqwe'
};

console.log(person2);