var geturlparm = function(){
    parm =  window.location.search
    if(parm.indexOf('?') === -1) return null; //如果url中没有传参直接返回空
    parm   = parm.substring(1, parm.length);
    var blogid = parm.split("&")[0].split("=")[1];
    return blogid
};


$(document).ready(
    blogid = geturlparm(),
    $.ajax({
        url: "http://localhost:5000/revblog?blogid="+blogid,
        type: "POST",
        // contentType: 'application/json',
        // data:"{}",
        dataType: "JSON",
        success:function(data){
            blogid = data["blogid"]
            blogtopic = data["blogtopic"]
            blogcontent = data["blogcontent"]
            $("#blogtopic").val(blogtopic)
            $("#blogcontent").val(blogcontent)
        },
        error:function(jqXHR, textStatus, errorThrown){
            console.log(errorThrown)
            alert("内容获取错误")
        }
    }),
);

