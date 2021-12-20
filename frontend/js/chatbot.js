var chatBtn = document.getElementById("box-chat-icon");
var closeBtn = document.getElementById("close-btn");

chatBtn.addEventListener("click", closeChatBot)
closeBtn.addEventListener("click", closeChatBot)

function closeChatBot(){
    var boxChat = document.getElementById("content-chat");
    if(boxChat.classList.contains("d-none")){
        boxChat.classList.remove("d-none");
    }
    else{
        boxChat.classList.add("d-none");
    }
}

