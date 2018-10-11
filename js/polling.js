var xmlhttp;
var currenttimeout;

function initAjax()
{
        // code for IE7+, Firefox, Chrome, Opera, Safari
        if (window.XMLHttpRequest)
        {
                xmlhttp=new XMLHttpRequest();
        }
        // code for IE6, IE5
        else
        {
                xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }

}

function processDateResult()
{
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
                var obj = JSON.parse( xmlhttp.responseText);
                var element = document.getElementById("thepara")
                if( element )
                {
                        element.innerHTML = "<P>" + obj.returnstring + "</P>"
                }
        }
        if( currenttimeout) clearTimeout( currenttimeout );
        currenttimeout = setTimeout( pollStatus, 5000 );
}

function callAjax( url , change_function )
{
        if( ! xmlhttp )
        {
                initAjax();
        }

        xmlhttp.onreadystatechange = change_function;
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
}

function pollStatus()
{
        callAjax( "/cgi-bin/polling.cgi", processDateResult);
}
