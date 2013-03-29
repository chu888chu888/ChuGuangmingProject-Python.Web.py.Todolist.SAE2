function validateEmail(email) {
    var reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(email);
}
//生成GUID
function G() {
    return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1)
}
$(document).ready(function () {
    $(".modalbox").fancybox();
    $("#contact").submit(function () {
        return false;
    });


    $("#send").on("click", function () {
        var emailval = $("#email").val();
        var msgval = $("#msg").val();
        var msglen = msgval.length;
        var mailvalid = validateEmail(emailval);

        if (mailvalid == false) {
            $("#email").addClass("error");
        }
        else if (mailvalid == true) {
            $("#email").removeClass("error");
        }

        if (msglen < 4) {
            $("#msg").addClass("error");
        }
        else if (msglen >= 4) {
            $("#msg").removeClass("error");
        }

        if (mailvalid == true && msglen >= 4) {
            // if both validate we attempt to send the e-mail
            // first we hide the submit btn so the user doesnt click twice
            $("#send").replaceWith("<em>发送中...</em>");
            var guid = (G() + G() + "-" + G() + "-" + G() + "-" +
                G() + "-" + G() + G() + G()).toUpperCase();
            $.ajax({
                type: 'POST',
                url: '/todo/sendmail?' + guid,
                data: $("#contact").serialize(),
                success: function (values) {
                    if (values == "OK") {

                        $("#contact").fadeOut("fast", function () {
                            $(this).before("<p><strong>发送成功!你的留言已经发送到管理员的信箱, 谢谢 :)</strong></p>");
                            setTimeout("$.fancybox.close()", 1000);
                        });
                    }
                    else {
                        $("#contact").fadeOut("fast", function () {
                            $(this).before("<p><strong>发送失败请再试 :)</strong></p>");
                            setTimeout("$.fancybox.close()", 1000);
                        });
                    }
                }
            });
        }
    });
});







