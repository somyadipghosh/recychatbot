var quotes = [
  ""Recycling is an investment in the future we will leave to the next generation.",
    "When you put the 'can' in the recycling bin, you're putting a 'yes' in the future.",
    "Recycling turns things into other things, which is like magic.",
    "Recycling is a simple act with huge benefits for our environment and future.",
    "Waste not, want not. Recycle today for a better tomorrow.",
    "The greatest threat to our planet is the belief that someone else will save it. Be the change, recycle.",
    "Recycling is not just a choice, it's a responsibility we all share.",
    "Every day is Earth Day when you recycle.",
    "Recycling: Because there is no Planet B.",
    "Don't trash our future. Recycle it.",
    "Recycling is the right thing to do, and it's easier than you think.",
    "One person's trash is another person's treasure – through recycling."
  ];
  
const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
console.log(randomQuote);

  
const dia = document.querySelector(".dia");
  const quoteElement = document.getElementById("quote");
  quoteElement.textContent = randomQuote;

const loading = document.getElementById('loading');
const form = document.querySelector('form');

form.addEventListener('submit', () => {
  loading.style.display = 'block';
});







var animationContainer = document.getElementById('loading');
var animationDataUrl = 'https://assets10.lottiefiles.com/packages/lf20_poqmycwy.json';

var animData = {
  container: animationContainer,
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: animationDataUrl
};

var anim = bodymovin.loadAnimation(animData);




const textarea = document.querySelector('textarea');

textarea.addEventListener('input', function() {
  this.style.height = 'auto';
  this.style.height = this.scrollHeight + 'px';
});

var animateButton = function(e) {

  e.preventDefault;
  //reset animation
  e.target.classList.remove('animate');
  
  e.target.classList.add('animate');
  setTimeout(function(){
    e.target.classList.remove('animate');
  },700);
};




