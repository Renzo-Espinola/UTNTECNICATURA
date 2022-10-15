// TIpos de datos en Javascript
/*
Multiples lineas
La sintaxis en lo que s comentarios
es muy similar a la de java
realmente diriamos que es identica
*/
var nombre = "Ariel"; //Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre =12.3;
console.log(typeof nombre);
var numero = 3000; //Tipo Numerico
console.log(numero);

var objeto = {
    nombre: "Ariel",
    apellido: "Betancud",
    telefono: "2614567893"
}
console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(typeof bandera)

//Tipo de dato Funcion
function miFuncion(){}
console.log(typeof miFuncion)

//TIpo de dato Symbol
var simbolo = Symbol("Mi simbolo")
console.log(typeof simbolo)

//Tipo de dato Clase
class Persona{
	constructor(nombre,apellido){
		this.nombre = nombre;
		this.apellido = apellido;
	}
}

console.log(typeof Persona);


