const chat_box = $('.chat-box');
const bt_show_popup = $('#new-chat');

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

bt_show_popup.click(function() {
    const pop_up = $('#pop-up');
    
    if (pop_up.hasClass('unshow')) {
        pop_up.removeCLass('unshow');
    } else {
        pop_up.addClass('unshow');
    }
});