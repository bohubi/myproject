/**
 * Created by mohammadalessa on 4/18/17.
 * to do a colored box <div> and will change color, size, and rotate as we touch it with the mouse (onmousemove)
 */

console.log("Hello");


var mybox = document.getElementById("mybox");
mybox.style = "position:fixed; left:150px; top:50px; width:50px; height: 50px; background-color:red;";

var x = 150;
var y = 50;
var r =1;
var g =1;
var b =1;
var dgree = 0;
var wdth = 50;
var hght = 50;


mybox.onmousemove = function(){
    x += Math.round(Math.random() * 20) - 10;
    y += Math.round(Math.random() * 20) - 10;
    r = Math.round(Math.random() * 255);
    g = Math.round(Math.random() * 255);
    b = Math.round(Math.random() * 255);
    wdth += Math.random() * 10;
    hght += Math.random() * 10;
    dgree += 10;

    console.log(r,g,b,x,y);

    mybox.style = "position:fixed; left:" + x + "px; top:" + y + "px; width:"+ wdth +"px; height:" + hght +"px; background-color:rgb("+ r  +","+ g +","+ b +"); transform:rotate("+dgree+"deg);";
};