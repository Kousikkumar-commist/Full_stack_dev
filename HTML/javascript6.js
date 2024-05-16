/*class Greeting {
  constructor(message) {
    this.message = message;
  }

  displayMessage() {
    console.log(this.message);
  }
}

const greeting = new Greeting("Hello, World!");
greeting.displayMessage();*/
let obj = {
  name: 'John',
  greet: function() {
    let self = this;
    console.log(this.name,date); 
    setTimeout(function() {
      console.log(self.name); 
    }, 1000);
  }
};
const date= new Date("2001-01-20");

obj.greet();