$(document).ready(function() {
    $("#loginCard").hide().slideDown(800);

    $("#passwordEye").click(function() {
        if ($("#passwordEye").html() == "visibility_off") {
            $("#passwordEye").html("visibility");
            $("#password").attr('type', 'text');
        } else {
            $("#passwordEye").html("visibility_off");
            $("#password").attr('type', 'password');
        }
    });

    $("#password2Eye").click(function() {
        if ($("#password2Eye").html() == "visibility_off") {
            $("#password2Eye").html("visibility");
            $("#password2").attr('type', 'text');
        } else {
            $("#password2Eye").html("visibility_off");
            $("#password2").attr('type', 'password');
        }
    });

});

