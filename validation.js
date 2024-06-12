$(function () {
    $("#place_error_message").hide();



    $("#fname_error_message").hide();
    $("#sname_error_message").hide();
    $("#email_error_meassage").hide();
    $("#password_error_message").hide();
    $("#retype_password_error_message").hide();
    $("#phone_error_message").hide();
    $("#address_error_message").hide();
    $("#father_error_message").hide();
    $("#blood_error_message").hide();
    $("#pincode_error_message").hide();
    $("#dob_error_message").hide();
    $("#state_error_message").hide();
    $("#occupation_error_message").hide();
    $("#proof_error_message").hide();
    $("#photo_error_message").hide();
    $("#md_error_message").hide();


    var error_place = false;


    var error_fname = false;
    var error_sname = false;
    var error_email = false;
    var error_password = false;
    var error_retype_password = false;
    var error_phone = false;
    var error_address = false;
    var error_husband = false;
    var error_father = false;
    var error_blood = false;
    var error_pincode = false;
    var error_dob = false;
    var error_state = false;
    var error_occupation = false;
    var error_proof = false;
    var error_photo = false;
    var error_md = false;

    $("#form_proof").focusout(function () {
        check_proof();
    });

    $("#form_photo").focusout(function () {
        check_photo();
    });



    $("#form_place").keyup(function () {
        check_place();
    });


    $("#form_fname").keyup(function () {
        check_fname();
    });

    $("#form_sname").keyup(function () {
        check_sname();
    });

    $("#form_email").keyup(function () {
        check_email();
    });

    $("#form_password").keyup(function () {
        check_password();
    });

    $("#form_retype_password").keyup(function () {
        check_retype_password();
    });

    $("#form_phone").keyup(function () {
        check_phone();
    });

    $("#form_address").keyup(function () {
        check_address();
    });

    $("#form_father").keyup(function () {
        check_father();
    });

    $("#form_blood").keyup(function () {
        check_blood();
    });

    $("#state").keyup(function () {
        check_state();
    });

    $("#form_occupation").keyup(function () {
        check_occupation();
    });

    $("#form_pincode").keyup(function () {
        check_pincode();
    });

    $("#form_dob").keyup(function () {
        check_dob();
    });

    $("#form_dname").keyup(function () {
        check_dname();
    });
    $("#form_md").keyup(function () {
        check_mdname();
    });
    $("#form_fees").keyup(function () {
        check_fees();
    });

    function check_proof() {
        var dname = $("#form_proof").val();
        if (dname == "") {
            $("#proof_error_message").html("This column cannot be blank");
            $("#proof_error_message").show();
            $("#form_proof").css("border-bottom", "2px solid #F90A0A");
            error_proof = true;
        } else {
            $("#proof_error_message").hide();
            $("#form_proof").css("border-bottom", "2px solid #34F458");
        }
    }
    function check_photo() {
        var dname = $("#form_photo").val();
        if (dname == "") {
            $("#photo_error_message").html("This column cannot be blank");
            $("#photo_error_message").show();
            $("#form_photo").css("border-bottom", "2px solid #F90A0A");
            error_photo = true;
        } else {
            $("#photo_error_message").hide();
            $("#form_photo").css("border-bottom", "2px solid #34F458");
        }
    }
    // function check_dname() {
    //     var dname = $("#form_dname").val();
    //     var pattern = /^[ A-Za-z_@./#&+-]*$/;
    //     if (pattern.test(dname) && dname !== "") {
    //         $("#fname_error_message").hide();
    //         $("#form_dname").css("border-bottom", "2px solid #34F458");
    //     } else if (dname == "") {
    //         $("#fname_error_message").html("This column cannot be blank");
    //         $("#fname_error_message").show();
    //         $("#form_dname").css("border-bottom", "2px solid #F90A0A");
    //         error_fname = true;
    //     } else {
    //         $("#fname_error_message").html("It should contain only charachters");
    //         $("#fname_error_message").show();
    //         $("#form_dname").css("border-bottom", "2px solid #F90A0A");
    //         error_fname = true;
    //     }
    // }
    function check_dname() {
        var pattern = /^[ A-Za-z_@./#&+-]*$/;
        var fname = $("#form_dname").val();
        if (pattern.test(fname) && fname !== "") {
            $("#dname_error_message").hide();
            $("#form_dname").css("border-bottom", "2px solid #34F458");
        } else if (fname == "") {
            $("#dname_error_message").html("This column cannot be blank");
            $("#dname_error_message").show();
            $("#form_dname").css("border-bottom", "2px solid #F90A0A");
            error_fname = true;
        } else {
            $("#dname_error_message").html("It should contain only charachters");
            $("#dname_error_message").show();
            $("#form_dname").css("border-bottom", "2px solid #F90A0A");
            error_fname = true;
        }
    }
    function check_mdname() {
        var pattern = /^[ A-Za-z_@./#&+-]*$/;
        var fname = $("#form_md").val();
        if (pattern.test(fname) && fname !== "") {
            $("#md_error_message").hide();
            $("#form_md").css("border-bottom", "2px solid #34F458");
        } else if (fname == "") {
            $("#md_error_message").html("This column cannot be blank");
            $("#md_error_message").show();
            $("#form_md").css("border-bottom", "2px solid #F90A0A");
            error_md = true;
        } else {
            $("#md_error_message").html("It should contain only charachters");
            $("#md_error_message").show();
            $("#form_md").css("border-bottom", "2px solid #F90A0A");
            error_md = true;
        }
    }

    function check_phone() {
        var phone = $("#form_phone").val();
        var pattern = /^[6,7,8,9][0-9]{0,9}$/;
        if (phone.length == 10 && pattern.test(phone)) {
            $("#phone_error_message").hide();
            $("#form_phone").css("border-bottom", "2px solid #34F458");
        } else if (phone == "") {
            $("#phone_error_message").html("Phone number cannot be blank");
            $("#phone_error_message").show();
            $("form_phone").css("border-bottom", "2px solid #F90A0A");
            error_phone = true;
        } else {
            $("#phone_error_message").html("Enter valid phone number");
            $("#phone_error_message").show();
            $("form_phone").css("border-bottom", "2px solid #F90A0A");
            error_phone = true;
        }
    }

    function check_place() {
        var pattern = /^[a-zA-Z/s]*$/;
        var place = $("#form_place").val();
        if (pattern.test(place) && place !== "") {
            $("#place_error_message").hide();
            $("#form_place").css("border-bottom", "2px solid #34F458");
        } else if (place == "") {
            $("#place_error_message").html("This column cannot be blank");
            $("#place_error_message").show();
            $("#form_place").css("border-bottom", "2px solid #F90A0A");
            error_sname = true;
        } else {
            $("#place_error_message").html("It should contain only charachters");
            $("#place_error_message").show();
            $("#form_place").css("border-bottom", "2px solid #F90A0A");
            error_place = true;
        }
    } 
    
    
    
    
    function check_fname() {
        var pattern = /^[a-zA-Z/s]*$/;
        var fname = $("#form_fname").val();
        if (pattern.test(fname) && fname !== "") {
            $("#fname_error_message").hide();
            $("#form_fname").css("border-bottom", "2px solid #34F458");
        } else if (fname == "") {
            $("#fname_error_message").html("This column cannot be blank");
            $("#fname_error_message").show();
            $("#form_fname").css("border-bottom", "2px solid #F90A0A");
            error_fname = true;
        } else {
            $("#fname_error_message").html("It should contain only charachters");
            $("#fname_error_message").show();
            $("#form_fname").css("border-bottom", "2px solid #F90A0A");
            error_fname = true;
        }
    }

    function check_sname() {
        var pattern = /^[a-zA-Z]*$/;
        var sname = $("#form_sname").val();
        if (pattern.test(sname) && sname !== "") {
            $("#sname_error_message").hide();
            $("#form_sname").css("border-bottom", "2px solid #34F458");
        } else if (sname == "") {
            $("#sname_error_message").html("This column cannot be blank");
            $("#sname_error_message").show();
            $("form_sname").css("border-bottom", "2px solid #F90A0A");
            error_fname = true;
        } else {
            $("#sname_error_message").html("It should contain only characters");
            $("#sname_error_message").show();
            $("form_sname").css("border-bottom", "2px solid #F90A0A");
            error_sname = true;
        }
    }

    function check_password() {
        var password = $("#form_password").val();
        var patternn = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%&])(.{8,20}$)/;
        if (patternn.test(password) && password !== "") {
            $("#password_error_message").hide();
            $("#form_password").css("border-bottom", "2px solid #34F458");
        } else if (password == "") {
            $("#password_error_message").html("Password cannot be blank");
            $("#password_error_message").show();
            $("form_password").css("border-bottom", "2px solid #F90A0A");
            error_password = true;
        } else {
            $("#password_error_message").html("Atleast 8 characters and should in proper format");
            $("#password_error_message").show();
            $("#form_password").css("border-bottom", "2px solid #F90A0A");
            error_password = true;
        }
    }

    function check_retype_password() {
        var password = $("#form_password").val();
        var retype_password = $("#form_retype_password").val();
        if (password !== retype_password) {
            $("#retype_password_error_message").html("   Password is not matching");
            $("#retype_password_error_message").show();
            $("#retype_form_password").css("border-bottom", "2px solid #F90A0A");
            error_retype_password = true;
        } else {
            $("#retype_password_error_message").hide();
            $("#form_retype_password").css("border-bottom", "2px solid #34F458");
        }
    }
    function check_email() {
        var pattern =
            /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-z\-0-9]+\.)+[a-z]{2,}))$/;
        var email = $("#form_email").val();
        if (pattern.test(email) && email !== "") {
            document.getElementById("form_email").style.borderBottom = "2px solid rgb(52, 244, 88)";
            $("#email_error_message").hide();
            $("#form_email").css("border-bottom", "2px solid rgb(52, 244, 88)");
            console.log("test....")
            // $("form_email").css("border-bottom", "2px solid #34F458");   
        } else {
            $("#email_error_message").html("Email should be in proper format and cannot be blank");
            $("#email_error_message").show();
            $("#form_email").css("border-bottom", "2px solid #F90A0A");
            error_email = true;
        }
    }

    function check_address() {
        var fname = $("#form_address").val();
        if (fname == "") {
            $("#address_error_message").html("Address cannot be blank");
            $("#address_error_message").show();
            $("form_address").css("border-bottom", "2px solid #F90A0A");
            error_address = true;
        } else {
            $("#address_error_message").hide();
            $("#form_address").css("border-bottom", "2px solid #34F458");
        }
    }

    function check_father() {
        var fname = $("#form_father").val();
        var pattern = /^[ a-zA-Z]*$/;
        if (pattern.test(fname) && fname !== "") {
            $("#father_error_message").hide();
            $("#form_father").css("border-bottom", "2px solid #34F458");
        } else {
            $("#father_error_message").html("This column should only character and cannot be blank");
            $("#father_error_message").show();
            $("form_father").css("border-bottom", "2px solid #F90A0A");
            error_father = true;
        }
    }

    function check_blood() {
        var fname = $("#form_blood").val();
        if (fname == "") {
            $("#blood_error_message").html("This column cannot be blank");
            $("#blood_error_message").show();
            $("form_blood").css("border-bottom", "2px solid #F90A0A");
            error_blood = true;
        } else {
            $("#blood_error_message").hide();
            $("#form_blood").css("border-bottom", "2px solid #34F458");
        }
    }

    function check_occupation() {
        var fname = $("#form_occupation").val();
        if (fname == "") {
            $("#occupation_error_message").html("This column cannot be blank");
            $("#occupation_error_message").show();
            $("form_occupation").css("border-bottom", "2px solid #F90A0A");
            error_occupation = true;
        } else {
            $("#occupation_error_message").hide();
            $("#form_occupation").css("border-bottom", "2px solid #34F458");
        }
    }

    function check_state() {
        var fname = $("#state").val();
        if (fname == "") {
            $("#state_error_message").html("This column cannot be blank");
            $("#state_error_message").show();
            $("state").css("border-bottom", "2px solid #F90A0A");
            error_state = true;
        } else {
            $("#state_error_message").hide();
            $("#state_occupation").css("border-bottom", "2px solid #34F458");
        }
    }
    function check_dob() {
        var fname = $("#form_dob").val();
        if (fname == "") {
            $("#dob_error_message").html("This column cannot be blank");
            $("#dob_error_message").show();
            $("form_dob").css("border-bottom", "2px solid #F90A0A");
            error_dob = true;
        } else {
            $("#dob_error_message").hide();
            $("#form_dob").css("border-bottom", "2px solid #34F458");
        }
    }
    function check_pincode() {
        var fname = $("#form_pincode").val();
        if (fname.length == 6) {
            if (isNaN(fname)) {
                $("#pincode_error_message").html("Not a number");
                $("#pincode_error_message").show();
                $("#form_pincode").css("border-bottom", "2px solid #F90A0A");
                error_pincode = true;
            } else {
                $("#pincode_error_message").hide();
                $("#form_pincode").css("border-bottom", "2px solid #34F458");
            }
            $("#pincode_error_message").hide();
            $("#form_pincode").css("border-bottom", "2px solid #34F458");
        } else if (fname == "") {
            $("#pincode_error_message").html("Cannot be blank");
            $("#pincode_error_message").show();
            $("#form_pincode").css("border-bottom", "2px solid #F90A0A");
            error_pincode = true;
        } else {
            $("#pincode_error_message").html("Enter valid pincode");
            $("#pincode_error_message").show();
            $("#form_pincode").css("border-bottom", "2px solid #F90A0A");
            error_pincode = true;
        }
    }
    function check_fees() {
        var fname = $("#form_fees").val();
        if (fname.length == 3) {
            if (isNaN(fname)) {
                $("#fees_error_message").html("Not a number");
                $("#fees_error_message").show();
                $("#form_fees").css("border-bottom", "2px solid #F90A0A");
                error_pincode = true;
            } else {
                $("#fees_error_message").hide();
                $("#form_fees").css("border-bottom", "2px solid #34F458");
            }
            $("#fees_error_message").hide();
            $("#form_fees").css("border-bottom", "2px solid #34F458");
        } else if (fname == "") {
            $("#fees_error_message").html("Cannot be blank");
            $("#fees_error_message").show();
            $("#form_fees").css("border-bottom", "2px solid #F90A0A");
            error_pincode = true;
        } else {
            $("#fees_error_message").html("Enter valid fees");
            $("#fees_error_message").show();
            $("#form_fees").css("border-bottom", "2px solid #F90A0A");
            error_pincode = true;
        }
    }
    // $("#updation_form").submit(function () {
    //     error_password = false;
    //     error_retype_password = false;

    //     check_password();
    //     check_retype_password();

    //     if (error_password === false && error_retype_password === false) {
    //         return true;
    //     } else {
    //         alert("Please fill the form Correctly");

    //         return false;
    //     }
    // });

    $("#registration_form").submit(function () {
        error_fname = false;
        error_sname = false;
        error_email = false;
        error_password = false;
        error_retype_password = false;
        error_phone = false;
        error_address = false;
        //error_husband = false;
        error_father = false;
        error_blood = false;
        error_pincode = false;
        error_dob = false;
        error_state = false;
        error_occupation = false;
        error_place = false;

        check_fname();
        check_sname();
        check_email();
        check_password();
        check_retype_password();
        check_address();
        check_blood();
        check_dob();
        check_father();
        check_occupation();
        check_pincode();
        //check_husband();
        check_state();
        check_phone();
        check_dname();

        if (
            error_place === false &&
            error_fname === false &&
            error_sname === false &&
            error_email === false &&
            error_address === false &&
            error_blood === false &&
            error_dob === false &&
            error_father === false &&
            error_occupation === false &&
            error_pincode === false &&
            error_state === false &&
            error_phone === false &&
            error_password === false &&
            error_retype_password === false
        ) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
    $("#add").submit(function () {
        error_place = false;
        error_fname = false;
        error_fname = false;
        error_email = false;
        error_password = false;
        error_address = false;
        error_blood = false;
        error_pincode = false;

        error_photo = false;
        error_proof = false;
        error_phone = false;

        check_place();
        check_sname();
        check_email();
        check_password();
        check_address();
        check_blood();
        check_pincode();
        check_phone();
        check_dname();
        check_proof();
        check_photo();
        check_fees();

        if (
            error_place === false &&
            error_fname === false &&
            error_email === false &&
            error_address === false &&
            error_blood === false &&
            error_pincode === false &&
            error_phone === false &&
            error_password === false &&
            error_photo === false &&
            error_proof === false
        ) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
    $("#add-staff").submit(function () {
        error_place === false;

        error_sname = false;
        error_fname = false;
        error_email = false;
        error_password = false;
        error_address = false;

        error_photo = false;

        error_phone = false;
        check_place();

        check_dname();
        check_email();
        check_password();
        check_address();

        check_phone();
        check_sname();

        check_photo();

        if (
            error_place === false &&
            error_sname === false &&
            error_fname === false &&
            error_email === false &&
            error_address === false &&
            error_phone === false &&
            error_password === false &&
            error_photo === false
        ) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
    $("#appoinment").submit(function () {
        error_fname = false;
        check_dname();
        if (error_fname === false) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });

    $("#update_dr").submit(function () {
        error_fname = false;
        error_address = false;
        error_pincode = false;
        error_md = false;

        error_phone = false;

        check_dname();
        check_mdname();
        check_address();
        check_pincode();
        check_phone();

        if (
            error_fname === false &&
            error_address === false &&
            error_md === false &&
            error_pincode === false &&
            error_phone === false
        ) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
    $("#update_p").submit(function () {
        error_fname = false;
        error_sname = false;

        error_phone = false;
        error_address = false;
        //error_husband = false;
        error_father = false;
        error_blood = false;
        error_pincode = false;

        check_fname();
        check_sname();

        check_blood();

        check_father();
        check_address();
        check_pincode();
        //check_husband();

        check_phone();

        if (
            error_fname === false &&
            error_sname === false &&
            error_address === false &&
            error_blood === false &&
            error_father === false &&
            error_pincode === false &&
            error_phone === false
        ) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
    $("#login").submit(function () {
        error_email = false;
        error_password = false;

        check_email();
        check_password();
        if (error_email === false && error_password === false) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
    $("#cpass").submit(function () {
        error_password = false;
        error_retype_password = false;

        check_password();
        check_retype_password();
        if (error_password === false && error_retype_password === false) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
    $("#cate").submit(function () {
        error_father = false;

        check_father();
        if (error_father === false) {
            return true;
        } else {
            alert("Please fill the form Correctly");

            return false;
        }
    });
});
