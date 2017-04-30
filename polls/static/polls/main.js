/**
 * Created by mohammadalessa on 4/17/17.
 */
var statusColor = {
    good: "green",
    bad: "red"
}


function checkUserName(username){
    if(username.length < 4){
        return {
            status: "bad",
            reason: "username us too short"
        };
    }
    else if(username.length > 15){
        return {
            status: "bad",
            reason: "username us too long"
        };
    }
    else{
        return {
            status:"good",
            reason:"all good",
        }
    }
}

function updateForm(){
    var username = document.getElementById("myinput").value;
    var x = checkUserName(username);
    var sp = document.getElementById("statusplace");
    var sb = document.getElementById("submitbtn");
    sp.innerHTML = x.reason;
    sp.style = "color:" + statusColor[x.status];
    if(x.status == "good")
    {
        sb.disabled = false;
    }
    else
    {
        sb.disabled = true;
    }

}

//linking the function updateForm to the tag that has the ID "myinput"
// document.getElementById("myinput").onkeyup = updateForm;

function updateProgressBar(div, value)
{
    console.log(div);
    console.log(value);
    div.style = "width:" + value + "%";
    if(value>100)
    {
        div.className ='progress-bar progress-bar-danger progress-bar-striped';
        div.innerHTML = value + "% Stop!!Go back!";
    }
    else
    {
        div.className ='progress-bar progress-bar-success progress-bar-striped';
        div.innerHTML = value + "% Complete (success)" ;
    }
}

var progress = 0;

var pbar = document.getElementById("myprogressbar");
var username = document.getElementById("myinput");
username.onkeyup = function(){
    progress_raw = (document.getElementById("myinput").value.length/15)*100;
    progress = Math.ceil(progress_raw);
    // console.log(document.getElementById("myinput").value.length)
    updateProgressBar(pbar,progress);
    updateForm();
}