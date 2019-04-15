$(document).ready(
    function () {
        $.ajax({
            url: "http://localhost:5000/bloglist",
            type: "GET",
            // data: data,
            dataType: "JSON",
            success:function(data){
                console.log(data)
                $.each(data, function (index, item) {
                    $("#bloglist").append("<div class='col-md-12'><h2 class='page-header'>" + data[index].blogtopic + "</h2><p>"+data[index].blogcontent+"</p></div>")
                })
            },
            error:function(data){
                console.log(data)
                alert("内容显示错误")
            }
          });
        }
);

$(document).on('click','#btnaddblog',function(){
    $.ajax({
        url: "http://localhost:5000/addblog",
        type: "GET",
        // contentType: 'application/json',
        // data:"{}",
        // dataType: "JSON",
        success:function(data){
            console.log(data)
            window.location.href="http://localhost:5000/addblog";
        },
        error:function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown)
            alert("内容获取错误")
        }
      });
});

