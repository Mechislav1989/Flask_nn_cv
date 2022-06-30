let canvas = document.querySelector(".myCanvas");
let context = canvas.getContext("2d");
const clear = document.querySelector('#clear')
const save = document.querySelector('#result')
canvas.width = 100; 
canvas.height = 100;
var canvastop = canvas.offsetTop
var lastx;
   var lasty;
context.strokeStyle = "#000000";
   context.lineCap = 'round';
   context.lineJoin = 'round';
   context.lineWidth = 5;
function dot(x,y) {
     context.beginPath();
     context.fillStyle = "#000000";
     context.arc(x,y,1,0,Math.PI*2,true);
     context.fill();
     context.stroke();
     context.closePath();
   }
function line(fromx,fromy, tox,toy) {
     context.beginPath();
     context.moveTo(fromx, fromy);
     context.lineTo(tox, toy);
     context.stroke();
     context.closePath();
   }
canvas.ontouchstart = function(event){
     event.preventDefault();
lastx = event.touches[0].clientX;
     lasty = event.touches[0].clientY - canvastop;
dot(lastx,lasty);
   }
canvas.ontouchmove = function(event){
     event.preventDefault();
var newx = event.touches[0].clientX;
     var newy = event.touches[0].clientY - canvastop;
line(lastx,lasty, newx,newy);
lastx = newx;
     lasty = newy;
   }
var Mouse = { x: 0, y: 0 };
 var lastMouse = { x: 0, y: 0 };
 context.fillStyle="white";
 context.fillRect(0,0,canvas.width,canvas.height);
 context.color = "black";
 context.lineWidth = 5;
    context.lineJoin = context.lineCap = 'round';
debug();
canvas.addEventListener( "mousemove", function( e )
 {
  lastMouse.x = Mouse.x;
  lastMouse.y = Mouse.y;
Mouse.x = e.pageX - this.offsetLeft;
  Mouse.y = e.pageY - this.offsetTop;
}, false );
canvas.addEventListener( "mousedown", function( e )
 {
  canvas.addEventListener( "mousemove", onPaint, false );
}, false );
canvas.addEventListener( "mouseup", function()
 {
  canvas.removeEventListener( "mousemove", onPaint, false );
}, false );
var onPaint = function()
 {
  context.lineWidth = context.lineWidth;
  context.lineJoin = "round";
  context.lineCap = "round";
  context.strokeStyle = context.color;
context.beginPath();
  context.moveTo( lastMouse.x, lastMouse.y );
  context.lineTo( Mouse.x, Mouse.y );
  context.closePath();
  context.stroke();
 };
function debug()