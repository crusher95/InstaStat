function uf(r) {
    var id = event.target.id;
    document.getElementById(id).innerHTML = "Unfollowing..";
    unfollow(id);

}
function f(r) {
    var id = event.target.id;
    document.getElementById(id).innerHTML = "Following..";
    follow(id);

}

function unfollow(id) {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 ) {
           if(xmlhttp.status == 200){
                   document.getElementById(id).innerHTML = xmlhttp.responseText;
           }
           else if(xmlhttp.status == 400) {
document.getElementById(id).innerHTML = "Some Error occured"
              //alert('There was an error 400')
           }
           else {
document.getElementById(id).innerHTML = "Some Error occured"
           }
        }
    };

    xmlhttp.open("GET", "http://localhost:5000/unfollow?id=" + id, true);
    xmlhttp.send();
}

function follow(id) {
    var xmlhttp;

    if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();

    }

    else {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 ) {
           if(xmlhttp.status == 200){

                   document.getElementById(id).innerHTML = xmlhttp.responseText;

           }
           else if(xmlhttp.status == 400) {
document.getElementById(id).innerHTML = "Some Error occured"
           }
           else {
document.getElementById(id).innerHTML = "Some Error occured"
           }
        }
    };

    xmlhttp.open("GET", "http://localhost:5000/follow?id=" + id, true);
    xmlhttp.send();
}
