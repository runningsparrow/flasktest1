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
                    $("#bloglist").append("<div class='col-md-12'><h2 class='page-header'>" + data[index].blogtopic + "</h2><p>"+data[index].blogcontent+"</p></div>"+
                    "<div class='col-md-12'><button class='btn btn-info revbtn'>修改</button> <button class='btn btn-info delbtn'>删除</button><input type='hidden' value='"+
                    data[index].blogid+"'></div>")
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

$(document).on('click','.revbtn',function(){
    // console.log($(this).parent().find('input').val())
    blogid = $(this).parent().find('input').val()
    window.location.href="http://localhost:5000/revblog?blogid="+blogid
});

$(document).on('click','.delbtn',function(){
    blogid = $(this).parent().find('input').val(),
    console.log(blogid),
    $.ajax({
        url: "http://localhost:5000/delblog",
        type: "POST",
        contentType: 'application/json',
        data:JSON.stringify({"blogid":blogid}),
        dataType: "JSON",
        success:function(data){
            console.log(data)
            window.location.reload()
        },
        error:function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown)
            alert("内容获取错误")
        }
    })
});

