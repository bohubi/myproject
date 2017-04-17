/**
 * Created by mohammadalessa on 4/16/17.
 */
// console.log("mama");
//
// function mklist(n){
//     var ls = [];
//     for(var i = 0; i<n ; i+=1){
//         ls.push(i);
//     }
//     return ls;
// }
//
//
// function sumlist(m) {
//     var total = 0;
//     for (var i = 0; i<m.length; i++){
//         total = total + m[i];
//     }
//     return total;
// }
//
//
// console.log(sumlist(mklist(100)));

var statusColor = {
    good: "blue",
    bad: "red"
}

function checkUserName(username){
    if (username.length < 4){
        return {
            status : 'bad',
            reason : 'username is too short'
        };
    } else if (username.length > 15){
        return {
            status : 'bad',
            reason : 'username is too long'
        };
    } else {
        return {
            status : 'good',
            reason : 'all good'
        };
    }
}


function updateForm(){
    var username = document.getElementById("myinput").value;
    var x = checkUserName(username);
    var sp = document.getElementById("statusplace");
    var sb = document.getElementById("submitbtn");
    sp.innerHTML = x.reason;
    sp.style = "color:" + statusColor[x.status];
    if(x.status == "good"){
        sb.disabled = false;
    } else {
        sb.disabled = true;
    }
}
