/* Arquivos java usam extensão .java (pasta src source)
Arquivos executáveis usam extensão .class (pasta bin binário)
Linguagem case sensitive
Termina cada linha com ;
Java usa { } para separar blocos
POO: objeto.atributo e objeto.método()
// Para um comentário. /* Abre e fecha bloco de comentário */

public static void main(String[] args){ //1a linha do main
//Programa
}

// Variáveis
int x; // inteiro
float y; // número decimal
double z; // double
String nome = "Texto"; // string. Para imprimir " usar \"
int[] vetor = new int[4]; // vetor de 4
int[][] matriz = new int[4][4]; // matriz de 4x4
String[] vetor = new String[4]; // string de 4
String[] vetor = {"A","B","C"}; // string com valores

// Entrada e saída de dados
System.out.println("Texto ou variavel"); // output
System.in; // input

import java.util.Scanner;
Scanner ler = new Scanner(System.in);
String nome = ler.next();

Scanner ler_num = new Scanner(System.in);
int num = ler_num.nextInt();

Scanner ler_num2 = new Scanner(System.in);
float num2 = ler_num2.nextFloat();

System.out.println("Meu nome é "+nome+" e tenho "+num+" anos");

/* Operadores:
+  soma
-  subtração
*  produto
/  divisão
%  módulo
++ contador +1
-- contador -1
x+=1 contador*/

/* Operadores relacionais:
== igual a
!= diferente de
>  maior que
<  menor que
>= maior ou igual a
<= menor ou igual a*/

/* Operadores lógicos:
&& e
|| ou
!  não*/

// for(valor inicial;condição;incremento) { }
for (int i=0; i<=10; i++) { }
for (int i=0; i<vetor.length; i++) { }

String[] vetor = {"A","B","C"};
for (String x:vetor) {		// for each de um vetor
	System.out.println(x);  // x recebe cada item do vetor
}

// while(condição) { }
int i = 0
while (i<3) {
	System.out.println(i);
	i++
}

// do { } while (condição);

// if (condição) { }
// else { }
String nome = "João";
if (nome.equals("Joana")){ // equals compara strings
	System.out.println("Igual")
}

/*switch
switch (variável) {
	case 1: ação
	break;
	case 2: ação
	break;
	default: ação
	break;
}*/

// Tratamento de exceções
// try { } catch (Exception e) { }
// Age em casos de erro no try como divisão por zero