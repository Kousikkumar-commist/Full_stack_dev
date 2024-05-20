/*class Animal{
    constructor(name){
        this.name = world;
        console.log("hello"+this.name)
    }
}
class Animal{
    constructor(name){
        this.name = name;
        console.log("hello " + this.name);
    }
}*/
class Animal{
    constructor(name){
        this.name=name;
        console.log("kousik "+ this.name);
    }
    kousik_fun(){
        console.log("kousik "+ this.name);
    }
}
const a =  new Animal("kumar");
a.kousik_fun();

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  readline.question('Please enter your name: ', name => {
    console.log("Hello",name ); 
    console.log(`Hello,${name}`); // another way
    readline.close();
  });