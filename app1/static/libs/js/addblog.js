$(document).on('click','#goindexbtn',function(){
    $.ajax({
        // url: "http://localhost:5000/",
        url: "./",
        type: "GET",
        // contentType: 'application/json',
        // data:"{}",
        // dataType: "JSON",
        success:function(data){
            console.log(data)
            // window.location.href="http://localhost:5000/";
            window.location.href="./";
        },
        error:function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown)
            alert("内容获取错误")
        }
      });
});
