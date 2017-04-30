/**
 * Created by mohammadalessa on 4/19/17.
 */


var canvas = document.getElementById("canvas");


var ctx1 = canvas.getContext('2d');
ctx1.fillStyle = 'green';
ctx1.fillRect(0, 115, 300, 35);

var housewall = canvas.getContext('2d');
housewall.fillStyle= 'brown';
housewall.fillRect(100, 55, 80, 60);


var roof = canvas.getContext('2d');
roof.fillStyle = 'red';
roof.beginPath(100,55);
roof.moveTo(180, 55);
roof.lineTo(140, 25);
roof.lineTo(100, 55);
roof.fill();

var chimney = canvas.getContext('2d');
chimney.fillStyle = 'grey';
chimney.beginPath(115,47);
chimney.moveTo(125, 35);
chimney.lineTo(125, 25);
chimney.lineTo(115, 25);
chimney.lineTo(115, 47);
chimney.fill();






// var roof = canvas.getContext('2d');
// roof.fillStyle= 'red';
// housewall.st(100, 55, 80, 60);





// function draw() {
//   var canvas = document.getElementById('canvas');
//   if (canvas.getContext) {
//     var ctx = canvas.getContext('2d');
//
//     ctx.fillRect(25, 25, 100, 100);
//     ctx.clearRect(45, 45, 60, 60);
//     ctx.strokeRect(50, 50, 50, 50);
//   }
// }

