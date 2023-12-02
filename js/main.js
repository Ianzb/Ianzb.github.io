function copyString(string) {
    var input = document.createElement("input");
    input.value = string;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
}
function load() {
    $("#header").load("../template/header.html")
    $("#footer").load("../template/footer.html")
}
function loadPage(name, page) {
    $(name).load(page)
}