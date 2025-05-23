const chat_box = $('.chat-box');

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