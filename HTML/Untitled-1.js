// Array of quotes
const quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
];

// Function to generate a random quote
function generateRandomQuote() {
    // Generate a random index within the range of the quotes array length
    const index = Math.floor(Math.random() * quotes.length);
    // Return the quote at the random index
    return quotes[index];
}

// Generate and display a random quote
const randomQuote = generateRandomQuote();
console.log("Random Quote:", randomQuote);