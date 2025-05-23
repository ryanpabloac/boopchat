const chat_box = $('.chat-box');
const bt_show_popup = $('#new-chat');
const pop_up = $('#pop-up');
const bt_close_popup = pop_up.closest('a')

chat_box.on("click", function() {
    const choosed_chat = $(this).closest('.chat-box');
    const dest_name = choosed_chat.find('.name-chat').text();

    $.ajax({
        url: "/chat",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({'d_username': dest_name}),
        success: function () {
            $("#chat-profile").find("h1").text(dest_name);
        }
    });
});

bt_show_popup.on('click', function() {
        pop_up.fadeIn("fast");
    });

bt_close_popup.on('click', function() {
    pop_up.fadeOut("fast");
});

pop_up.on('click', function() {
    pop_up.fadeOut("fast");
});

$("#pop-up-box").on('click', function(e) {
    e.stopPropagation();
});