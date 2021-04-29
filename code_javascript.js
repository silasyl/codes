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