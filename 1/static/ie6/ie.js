function ie() {
    var isIE = !!window.ActiveXObject;
    var isIE6 = isIE && !window.XMLHttpRequest;
    var isIE8 = isIE && !!document.documentMode;
    var isIE7 = isIE && !isIE6 && !isIE8;
    if (isIE) {
        if (isIE6) {
            var style = document.createElement('link');
            style.href = '/static/skins/ie7/skinIE6.css';
            style.rel = 'stylesheet';
            style.type = 'text/css';
            document.getElementsByTagName('HEAD').item(0).appendChild(style);
            alert("ie6");
        }
        else if (isIE8) {
            var style = document.createElement('link');
            style.href = '/static/skins/ie7/skinIE7.css';
            style.rel = 'stylesheet';
            style.type = 'text/css';
            document.getElementsByTagName('HEAD').item(0).appendChild(style);
            alert("ie8");
        }
        else if (isIE7) {
            var style = document.createElement('link');
            style.href = '/static/skins/ie7/skinIE7.css';
            style.rel = 'stylesheet';
            style.type = 'text/css';
            document.getElementsByTagName('HEAD').item(0).appendChild(style);
            alert("ie7");
        }
    }

}


//第一次页面的加载时候调用事件
if (window.addEventListener) {
    window.addEventListener("load", ie, false);
}
else if (window.attachEvent) {
    window.attachEvent("onload", ie);
}
else {
    window.onload = ie;
}
