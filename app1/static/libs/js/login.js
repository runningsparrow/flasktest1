$(document).ready(
    function () {
        var options = { 
            target:        '#logresult',   // 用服务器返回的数据 更新 id为output1的内容.
            beforeSubmit:  showRequest,  // 提交前
            success:       showResponse,  // 提交后 
            error: showerror,
            //另外的一些属性: 
            //url:       url         // 默认是form的action，如果写的话，会覆盖from的action. 
            //type:      type        // 默认是form的method，如果写的话，会覆盖from的method.('get' or 'post').
            //dataType:  null        // 'xml', 'script', or 'json' (接受服务端返回的类型.) 
            //clearForm: true        // 成功提交后，清除所有的表单元素的值.
            resetForm: false        // 成功提交后，重置所有的表单元素的值.
            //由于某种原因,提交陷入无限等待之中,timeout参数就是用来限制请求的时间,
            //当请求大于3秒后，跳出请求. 
            //timeout:   3000 
        }; 
     
        //'ajaxForm' 方式的表单 .
        $('#logform').ajaxForm(options);  
        //或者 'ajaxSubmit' 方式的提交.
        //$('#myForm').submit(function() { 
        //    $(this).ajaxSubmit(options); 
        //    return false; //来阻止浏览器提交.
        //}); 
    } 
);

// 提交前
function showRequest(formData, jqForm, options) { 
    // formdata是数组对象,在这里，我们使用$.param()方法把他转化为字符串.
    //   var queryString = $.param(formData); //组装数据，插件会自动提交数据
    //   alert(queryString); //类似 ： name=1&add=2  
    // alert(formData)
    //return true; 
    
} 

//提交后
function showResponse(responseText, statusText)  { 
    //    alert('状态: ' + statusText + '\n 返回的内容是: \n' + responseText); 
    console.log('状态: ' + statusText + '\n 返回的内容是: \n' + responseText);
    // var jsondata = JSON.parse(responseText);

    console.log(responseText["msg"]);
    console.log(responseText["status"]);
    console.log(responseText["data"]);


    $('#logresult').html(responseText["msg"])   
    $('#token').html(responseText["data"]) 
} 

function showerror(responseText, statusText){
    console.log('状态: ' + statusText + '\n 返回的内容是: \n' + responseText);
    console.log(responseText["msg"]);
    console.log(responseText["status"]);
    console.log(responseText["data"]);
}

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