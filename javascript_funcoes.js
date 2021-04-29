/* Arquivos javascript usam extensão .js
Linguagem case sensitive
Java usa { } para separar blocos
POO: objeto.atributo e objeto.método()
// Para um comentário. /* Abre e fecha bloco de comentário */

// 1. Prerequisites

// -> Basic knowledge of JS
// ---> Data types: number, string, boolean, array and object
// ---> Operators (+, -, *, /, &&, ||, >=, <=, ...)
// ---> If, For, While

//Output:
console.log('TEXTO')

// Function declaration
function Nome(parâmetros) {

}

function Ola(nome){
	console.log('Ola ' + nome)
	console.log(`Ola ${nome}`) // Template string
}
Ola('Silas') // Vai chamar a função e imprimir Ola Silas

function returnHi() {
	return 'Hi!' // retorna Hi em uma variavel
}
let g = returnHi // Pode armazenar em var, let, const
console.log(g) // A variavel recebeu 'Hi!'

function returnHiTo(name) {
    return `Hi ${name}!`
}
console.log(returnHiTo('Silas')) // função que recebe parâmetro e retorna

// Anonymous function
// Função sem nome, ex:
(function (a, b, c) {
    return a + b + c
})

// Function expression
// Posso atribuir uma função a uma variável, usando função anônima, ex:
const sum = function (a, b) {
    return a + b
}
console.log(sum(1,3)) // Posso chamar sum usando parâmetros nele
const result = sum
console.log(result(1,4)) // Posso chamar outra variável com parâmetros em sum

// Arrow Function is always anonymous
const increment1 = (n) => {
    return n + 1
}

const increment2 = (a,b) => a + b // Depois da seta tudo é return

// IIFE - Immediately Invoked Function Expression
// Posso chamar uma função anônima passando imediatamente seus parâmetros
(function (a, b, c) {
    console.log(`Result: ${a + b + c}`)
})(1, 2, 3); // É necessário fechar com ;

(() => {
    console.log('invoked')
})();

(() => console.log('invoked'))();

// Parâmetros
function logParams(a, b, c) {
    console.log(a, b, c)
}

logParams(1, 2, 3, 4, 5) // Ignora os parâmetros em excesso
logParams(1, 2, 3)
logParams(1, 2) // O parâmetro em falta é undefined

// Pré define valores a parâmetros caso não recebam valor
function defaultParams(a = 1, b = 2, c = 3) {
    console.log(a, b, c)
}

defaultParams(7, 8, 9) // retorna 7, 8, 9
defaultParams(7, 8) // retorna 7, 8, 3

function logNums(nums) {
    for(let n of nums) {
        console.log(n)
    }
}

logNums([1, 2, 3]) // imprime 1 2 3

// spread/rest
// Uso de ... faz com que ele receba um número variável de parâmetros
function logNums(...nums) {
    console.log(Array.isArray(nums)) // retorna true, é array
    console.log(nums)
}

logNums(1, 2, 3, 4, 5, 6) // retorna [1 2 3 4 5 6]

function sumAll(...nums){ // Exemplo de função soma
    let total = 0
    for(let n of nums){
        total += n
    }
    return total
}

// list comprehension
const n1 = b === undefined ? 1 : a
// b = undefined? Se sim n1 = 1, se não n1 = a

for(let i = n1; n1 <= n2 ? i <= n2 : i >= n2; i+= n3){ }
// n1 <= n2? Se sim i <= n2, se não i >= n2

const nums = []
nums.push(i) // Adiciona ao vetor

const var = (el, i, acc, array) => el.score // Recebe elemento, índice, acumulador, array

/*
 * A programming language is said to have
 * First-class functions when functions in
 * that language are treated like any other
 * variable.
 */

const add = function(a, b) {
    return a + b
}
console.log(add(10, 20))

const subtract = (x,y) => x-y
console.log(subtract(10, 20))

/*
 * Functions that operate on other functions,
 * either by taking them as arguments or by
 * returning them, are called higher-order functions.
 */

function run(fn) {
    fn()
}

function sayHello() {
    console.log('Hello!')
}

run(sayHello) // função run chamando função sayHello

run(function(){ // posso chamar função anônima
    console.log('run!')
})

function run(fn) {
    return `Result: ${fn()}`
}
const result = run(Math.random) // Chamando função da biblioteca
console.log(result)

// Chamada de função dentro de função
function finalPrice(tax, price) {
    return price * (1 + tax)
}
console.log(finalPrice(0.0875, 25.1))

// curring, programação funcional
function finalPrice(tax) {
    return function(price){
        return price * (1 + tax)
    }
}
console.log(finalPrice(0.0875)(25.1))

const nycFinalPrice = finalPrice(0.0875) // imposto igual
console.log(nycFinalPrice(25.1)) // preços diferentes
console.log(nycFinalPrice(21.7)) // funções diferentes
console.log(nycFinalPrice(107.9))

// Função map: aplica função em vetor
const numbers = [1, 2, 3, 4, 5, 6]
const numbers3 = []
for(let n of numbers) {
    numbers3.push(n * 2)
}

// Usando map
const numbers2 = numbers.map(function(el) {
    return el*2
})
console.log(numbers2)

const students = [
    { name: 'Jake', score: 6.4},
    { name: 'Susan', score: 8.6},
    { name: 'Emma', score: 9.4},
    { name: 'Peter', score: 9.1},
]

const getScore = el => el.score
console.log(
    students
        .map(getScore) // retorna 6.4 8.6 9.4 9.1
        .map(Math.ceil) // retorna 7 9 10 10
        .map(Math.floor)) // retorna 6 8 9 9

// Função filter: É semelhante ao map, mas para filtrar
// O vetor filtrado tem tamanho igual ou menor até zero ao original
const numbers = [1, 2, 3, 4, 5, 6]

const greaterThanZero = el => el > 0
const greaterThanTen = el => el > 10
const even = el => el % 2 === 0

console.log(numbers.filter(greaterThanZero)) // filtra [1 2 3 4 5 6]
console.log(numbers.filter(greaterThanTen)) // filtra []
console.log(numbers.filter(even)) // filtra [2 4 6]

const students = [
    { name: 'Jake', score: 6.4},
    { name: 'Susan', score: 8.6},
    { name: 'Emma', score: 9.4},
    { name: 'Peter', score: 9.1},
]

const greatStudent = student => student.score >= 9
console.log(students.filter(greatStudent)) // filtra alunos com nota maior que 9

// Reduce: Função que utiliza dois parâmetros
// Realiza a soma de todos os elementos de um vetor
// reduce(função,valor inicial)
const numbers = [1, 2, 3, 4, 5, 6]

const sum = (total, el) => total + el
const total = numbers.reduce(sum, 100)
console.log(total)

const avg = (acc, el, i, array) => {
    if(i === array.length - 1) {
        return (acc + el) / array.length
    } else {
        return acc + el
    }
}
const result = numbers.reduce(avg) // média
console.log(result)