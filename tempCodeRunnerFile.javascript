class Greeting {
    constructor(message) {
      this.message = message;
    }
  
    displayMessage() {
      console.log(this.message);
    }
  }
  
  const greeting = new Greeting("Hello, World!");
  greeting.displayMessage(); // Output: "Hello, World!"