const f = () =>{
    let username = $("#imagen").val()
    const data = {
        username
    }
    $.ajax({
        type: "post",
        url: "/escribir",
        data: data,
        dataType: "json",
        success: function (response) {
            document.getElementById("img").setAttribute("src","static/imagenes/"+response["filename"]);
        },
        error: function (response) {
            alert("error")
        }
    });
}