let canvas = document.querySelector(".myCanvas");
let context = canvas.getContext("2d");
const clear = document.querySelector('#clear')
const save = document.querySelector('#predict')
canvas.width = 100; 
canvas.height = 100;
                 
var mouse = {x:0, y:0};
var draw = false;

context.lineWidth = 5;
context.lineJoin = 'round';
context.lineCap = 'round';
             
canvas.addEventListener("mousedown", function(e){
                 
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
    draw = true;
    context.beginPath();
    context.moveTo(mouse.x, mouse.y);
});

canvas.addEventListener("mousemove", function(e){
                 
    if(draw==true){
                 
        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
        context.lineTo(mouse.x, mouse.y);
        context.stroke();
        }
});

canvas.addEventListener("mouseup", function(e){
                 
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
    context.lineTo(mouse.x, mouse.y);
    context.stroke();
    context.closePath();
    draw = false;
});

clear.addEventListener('click', function() {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height);
})

// var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
// if (save) {
// save.addEventListener('click', function() {
//     let img = canvas.toDataURL('image/jpg');
//     $.ajax({
//         type: "POST",
//         // url: "/hook",
//         url: $SCRIPT_ROOT + "/predict/",
//         data:img,
//         success: function(data){
//             $('#result').text(' Predicted Output: '+data);}
//     })
// });
// };    
// }).done(function(response){
//      document.querySelector('#answer').innerHTML = response
// })
// }
// $("#result").click(function(){
//     var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
//     var canvasObj = document.getElementById("canvas");
//     var img = canvasObj.toDataURL();
//     $.ajax({
//       type: "POST",
//       url: $SCRIPT_ROOT + "/predict/",
//       data: img,
//       success: function(data){
//         $('#result').text(' Predicted Output: '+data);
//       }
//     });
// });