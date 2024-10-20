var pageList = {}
function copyString(string) {
    var input = document.createElement("input");
    input.value = string;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
}
function loadTemplate() {
    $("#header").load("./template/header.html")
    $("#footer").load("./template/footer.html")
}
function addPage(name, page) {
    pageList[name] = page
}

function getUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;
}
function loadPage() {
    var page = getUrlParam("page")
    $("body").load(pageList[page])
}