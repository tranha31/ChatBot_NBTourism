var status = 0;
var chatBtn = document.getElementById("box-chat-icon");
var closeBtn = document.getElementById("close-btn");

chatBtn.addEventListener("click", closeChatBot)
closeBtn.addEventListener("click", closeChatBot)

/**
 * Đóng mở chat box
 */
function closeChatBot(){
    var boxChat = document.getElementById("content-chat");
    if(boxChat.classList.contains("d-none")){
        boxChat.classList.remove("d-none");
    }
    else{
        boxChat.classList.add("d-none");
        status = 0;
    }
}

var inputChat = $("#input-send-chat");
var btnChat = $("#btn-send-chat");

inputChat.keyup(function(event){
    if(event.keyCode === 13){
        addUserInbox();
        sendChatBox();
    }
})

btnChat.on("click", function(){
    addUserInbox();
    sendChatBox();
});

/**
 * Thêm nội dung chat của user
 */
function addUserInbox(){
    var value = inputChat.val();
    var chat = document.getElementById("chat-content");
    var div = document.createElement("div");
    div.className = "send user-send";
    var p = document.createElement("p");
    p.innerHTML = value;
    div.appendChild(p);
    chat.appendChild(div);

    chat.scrollTop = chat.scrollHeight;
}

/**
 * Thêm nội dung chat của bot
 * @param {Array} content : nội dung chat của bot
 * @param {String} src : đường dẫn ảnh nếu có
 */
function addBotInbox(content, src){
    var chat = document.getElementById("chat-content");
    var div = document.createElement("div");
    div.className = "send bot-send";

    for(var i=0; i<content.length; i++){
        var p = document.createElement("p");
        p.innerHTML = content[i];
        div.appendChild(p); 
    }
    if(src){
        var img = document.createElement("img");
        img.src = src;
        div.appendChild(img);
    }
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

/**
 * Gửi nội dung để lấy intent
 */
function sendChatBox(){
    var value = inputChat.val();
    $.ajax({
        method: "GET",
        url: "https://westeurope.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/d63dcf69-6ba7-45d3-97b3-80cf1083732a/slots/production/predict?verbose=true&show-all-intents=true&log=true&subscription-key=40ed3241b400469bb66e6faff883e5fb&query="+value,
        dataType: "json",
        contentType: "application/json-patch+json",
    })
    .done(function(res){
        excuteRequest(res);
        inputChat.val(null);
    })
}

/**
 * Thực thi yêu cầu user
 * @param {Object} item : đối tượng LUIS trả về 
 */
function excuteRequest(item){
    var intent = String(item.prediction.topIntent);
    if(status == 0){
        if(intent != "batDau"){
            var content = ["TaHa đang ngủ zzz <br> Để bắt đầu hỏi đáp hãy đánh thức TaHa",
                        "Bạn có thể đánh thức TaHa bằng những câu chào!"];
            addBotInbox(content, src);
        }
        else{
            var content = ["Chào bạn, mình là TaHa!!! Rất vui lòng được giúp đỡ bạn",
                        "Bạn nên đặt câu hỏi rõ nghĩa để mình hiểu đúng ý <br> VD: thông tin chùa Bái Đính -> hỏi về danh lam <br> thông tin lễ hội chùa Bái Đính -> hỏi về lễ hội",
                        "Và bạn cần viết đúng tên riêng của danh lam, lễ hội,... "];
            var src = '../content/images/hello.png';
            addBotInbox(content, src);
            status = 1;
        }
    }
    else{
        if(intent == "batDau"){
            var content = ["Chào bạn, mình là TaHa!!! Rất vui lòng được giúp đỡ bạn",
                        "Bạn nên đặt câu hỏi rõ nghĩa để mình hiểu đúng ý <br> VD: thông tin chùa Bái Đính -> hỏi về danh lam <br> thông tin lễ hội chùa Bái Đính -> hỏi về lễ hội",
                        "Và bạn cần viết đúng tên riêng của danh lam, lễ hội,..."];
            var src = '../content/images/hello.png';
            addBotInbox(content, src);
        }
        else if(intent == "tuHaoNB"){
            var content = ["Ninh Bình tuyệt vời!!! <br> Yêu Ninh Bình, yêu bạn!!!"];
            var src = '../content/images/love.png';
            addBotInbox(content, src);
        }
        else if(intent == "danhLam"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.danhLamM ? item.prediction.entities.$instance.danhLamM : "";
                callAPIBackend(1, query);
            }
            else{
                cannotUnderStand();
            }
        }
        else if(intent == "thongTinLeHoi"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.leHoi ? item.prediction.entities.$instance.leHoi : "";
                callAPIBackend(2, query);
            }
            else{
                cannotUnderStand();
            }
        }
        else if(intent == "hoiVeDiaDiem"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.danhLamM ? item.prediction.entities.$instance.danhLamM : "";
                callAPIBackend(3, query);
            }
            else{
                cannotUnderStand();
            }
        }
        else if(intent == "diaDiemLeHoi"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.leHoi ? item.prediction.entities.$instance.leHoi : "";
                callAPIBackend(4, query);
            }
            else{
                cannotUnderStand();
            }
        }
        else if(intent == "hoiVeHoatDongLeHoi"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.leHoi ? item.prediction.entities.$instance.leHoi : "";
                callAPIBackend(5, query);
            }
            else{
                cannotUnderStand();
            }
            
        }
        else if(intent == "hoiVeMucDichLeHoi"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.leHoi ? item.prediction.entities.$instance.leHoi : "";
                callAPIBackend(6, query);
            }
            else{
                cannotUnderStand();
            }
            
        }
        else if(intent == "hoiVeThoiGianLeHoi"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.leHoi ? item.prediction.entities.$instance.leHoi : "";
                callAPIBackend(7, query);
            }
            else{
                cannotUnderStand();
            }
            
        }
        else if(intent == "hoiVeThongTinTour"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.touRR ? item.prediction.entities.$instance.touRR : "";
                callAPIBackend(8, query);
            }
            else{
                cannotUnderStand();
            }
            
        }
        else if(intent == "hoiVeChiPhi"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.touRR ? item.prediction.entities.$instance.touRR : "";
                callAPIBackend(9, query);
            }
            else{
                cannotUnderStand();
            }
            
        }
        else if(intent == "hoiVeLichTrinhTour"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.touRR ? item.prediction.entities.$instance.touRR : "";
                callAPIBackend(10, query);
            }
            else{
                cannotUnderStand();
            }
        }
        else if(intent == "goiYLeHoi"){
            if(item.prediction.entities){
                if(item.prediction.entities.$instance.thanGG){
                    callAPIBackend(11, item.prediction.entities.$instance.thanGG);
                }
                else if(item.prediction.entities.$instance.mucDich){
                    callAPIBackend(12, item.prediction.entities.$instance.mucDich);
                }
                else{
                    cannotUnderStand();
                }
            }
            else{
                cannotUnderStand();
            }
            
        }
        else if(intent == "goiYTour"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.danhLamM ? item.prediction.entities.$instance.danhLamM : "";
                callAPIBackend(13, query);
            }
            else{
                cannotUnderStand();
            }
            
        }
        else if(intent == "goiYNhaHang"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.danhLamM ? item.prediction.entities.$instance.danhLamM : "";
                callAPIBackend(14, query);
            }
            else{
                cannotUnderStand();
            }
        }
        else if(intent == "goiYKhachSan"){
            if(item.prediction.entities){
                var query  = item.prediction.entities.$instance.danhLamM ? item.prediction.entities.$instance.danhLamM : "";
                callAPIBackend(15, query);
            }
            else{
                cannotUnderStand();
            }
        }
        else{
            cannotUnderStand();
        }
    }
}

/**
 * Không hiểu nội dung hoặc không có kq trả về
 */
function cannotUnderStand(){
    var content = ["Rất tiếc, mình không biết câu trả lời :("];
    var src = '../content/images/sad.png';
    addBotInbox(content, src);
}

/**
 * Gọi API backend để trả lời
 * @param {Number} type : loại ý định
 * @param {String} query : đối tượng gọi
 */
function callAPIBackend(type, query){
    query = query[0].text;
    var d = {
        type : type,
        value : query.toLowerCase()
    }

    d = JSON.stringify(d);
    $.ajax({
        method: "POST",
        url: "http://127.0.0.1:5000/api/chat",
        dataType: "json",
        data: d,
        contentType: "application/json-patch+json",
    })
    .done(function(res){
        if(res.code == 404){
            cannotUnderStand();
        }
        else{
            var data = res.data;
            if(data.length == 0){
                cannotUnderStand();
            }
            else{
                beforeBindData(type, data);
            }
        }
    })
    .fail(function(){
        cannotUnderStand();
    })
}

/**
 * Chuan bi truoc khi bind
 * @param {Number} type : loai y dinh 
 * @param {*} data : mang du lieu
 */
function beforeBindData(type, data){
    switch(type){
        case 1:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(data[i].name);
                if(data[i].nameEx != "None"){
                    content.push(`Tên gọi khác: ${data[i].nameEx}`);
                }
                content.push(`Vị trí danh lam: ${data[i].location}`);
                content.push(data[i].info);
                addBotInbox(content, null);
            }
            break;
        case 2:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(data[i].name);
                if(data[i].nameEx != "None"){
                    content.push(`Tên gọi khác: ${data[i].nameEx}`);
                }
                content.push(`Địa điểm tổ chức: ${data[i].location}`);
                content.push(`Thời gian tổ chức: ${data[i].time}`);
                content.push(`Mục đích tổ chức: ${data[i].purpose}`);
                content.push(`Phần lễ: <br> ${data[i].cultral}`);
                if(data[i].activities != "None"){
                    content.push(`Phần hội: <br> ${data[i].activities}`);
                };
                addBotInbox(content, null);
            }
            break;
        case 3:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(`Vị trí: ${data[i].location}`);
                addBotInbox(content, null);
            }
            break;
        case 4:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(`Địa điểm tổ chức: ${data[i].location}`);
                addBotInbox(content, null);
            }
            break;
        case 5:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(`Phần lễ: <br> ${data[i].cultral}`);
                if(data[i].activities != "None"){
                    content.push(`Phần hội: <br> ${data[i].activities}`);
                };
                addBotInbox(content, null);
            }
            break;
        case 6:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(`Mục đích: ${data[i].purpose}`);
                addBotInbox(content, null);
            }
            break;
        case 7:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(`Thời gian tổ chức: ${data[i].time}`);
                addBotInbox(content, null);
            }
            break;
        case 8:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(data[i].name);
                content.push(data[i].description);
                content.push(data[i].condition);
                content.push(`Chi phí gói 1: ${data[i].costPackage1} <br> Thông tin gói 1: ${data[i].infoPackage1}`);
                content.push(`Chi phí gói 2: ${data[i].costPackage2} <br> Thông tin gói 2: ${data[i].infoPackage2}`);
                content.push("Lịch trình:");
                content.push(data[i].planDay);
                if(data[i].planAfter != "None"){
                    content.push(data[i].planAfter);
                }
                addBotInbox(content, null);
            }
            break;
        case 9:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(`Chi phí gói 1: ${data[i].costPackage1} <br> Thông tin gói 1: ${data[i].infoPackage1}`);
                content.push(`Chi phí gói 2: ${data[i].costPackage2} <br> Thông tin gói 2: ${data[i].infoPackage2}`);
                addBotInbox(content, null);
            }
            break;
        case 10:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push("Lịch trình:");
                content.push(data[i].planDay);
                if(data[i].planAfter != "None"){
                    content.push(data[i].planAfter);
                }
                addBotInbox(content, null);
            }
            break;
        case 11:
            for(var i=0; i<data.length; i++){
                var content = []
                content.push(`Lễ hội: ${data[i].name}`);
                if(data[i].nameEx != "None"){
                    content.push(`Tên khác: ${data[i].nameEx}`);
                }
                content.push(".");
                addBotInbox(content, null);
            }
            break;
        case 12:
            var content = [];
            content.push("Danh sách lễ hội bạn có thể tham khảo:");
            addBotInbox(content, null);
            for(var i=0; i<data.length; i++){
                content = []
                content.push(`Lễ hội: ${data[i].name}`);
                if(data[i].nameEx != "None"){
                    content.push(`Tên khác: ${data[i].nameEx}`);
                }
                addBotInbox(content, null);
            }
            break;
        case 13:
            var content = [];
            content.push("Danh sách tour bạn có thể tham khảo:");
            addBotInbox(content, null);
            for(var i=0; i<data.length; i++){
                content = [];
                content.push(`Tour: ${data[i].name}`);
                addBotInbox(content, null);
            }
            break;
        case 14:
            var content = [];
            content.push("Danh sách địa điểm bạn có thể tham khảo:");
            addBotInbox(content, null);
            for(var i=0; i<data.length; i++){
                content = [];
                content.push(`${data[i].name} <br> Địa chỉ: ${data[i].vitri}`);
                addBotInbox(content, null);
            }
            break;
        case 15:
            var content = [];
            content.push("Danh sách địa điểm bạn có thể tham khảo:");
            addBotInbox(content, null);
            for(var i=0; i<data.length; i++){
                content = [];
                content.push(`${data[i].name} <br> Địa chỉ: ${data[i].vitri} <br> Chi phí: ${data[i].gia} VND/đêm <br> ${data[i].link}`);
                addBotInbox(content, null);
            }
            break;
    }
}