var tl = new TimelineMax({ repeat:-1});
var bulina = $('.loader li');
tl.add(
  TweenMax.staggerFromTo(
      $('.loader li'),0.4,
      {
           top:"25px",
        alpha:0.3,
           ease:Power2.easeIn
           
      },
      {
           top:"50px",
        alpha:0.6,
           ease:Power2.easeOut
      },
      0.08
    )
  
);

tl.add(
  TweenMax.staggerFromTo(
      $('.loader li'),0.4,
      {
           top:"50px",
        alpha:0.6,
           ease:Power2.easeIn
           
      },
      {
           top:"0px",
        alpha:0.9,
           ease:Power2.easeOut,
        delay:-0.4
      },
      0.08
    )
  
);


tl.add(
  TweenMax.staggerFromTo(
      $('.loader li'),0.4,
      {
           top:"0px",
        alpha:0.9,
           ease:Power2.easeIn
           
      },
      {
           top:"25px",
        alpha:0.3,
           ease:Power2.easeOut,
        delay:-0.4
      },
      0.08
    )
  
);


    
tl.play()