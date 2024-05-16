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
        let name = prompt("Please enter your name:");
        console.log("Hello, " + name);
    }
}
const a =  new Animal("kumar");
a.kousik_fun();