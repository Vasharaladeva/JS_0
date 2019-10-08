const nums = [1,2,3,4];
nums.push(5);


const sayHello = name => console.log(`shambri ${name}`);

const frutas = ['platano','manzana','mandarina'];

frutas.forEach((frutas,index) => console.log(frutas));

const SoloFruta = frutas.map((fruta) => frutas.slice(0,-1));
console.log(SoloFruta);

const people = [
    {id:1, name: 'qwe'},
    {id:2, name: 'rw'},
    {id:3, name: 'werwe'},
]

const people2 = people.filter(person => person.id !== 2);
console.log(people2);

const arr = [1,2,3];
const arr2 = [...arr,4];

console.log(arr2);