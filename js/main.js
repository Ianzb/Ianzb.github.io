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
    $("head").append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    $("#header").load("./template/header.html")
    $("#footer").load("./template/footer.html")
}
function addPage(name, page) {
    pageList[name] = page
}
function addPages(pages) {
    for (const [k, v] of Object.entries(pages)) {
        addPage(k, v)
    }
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