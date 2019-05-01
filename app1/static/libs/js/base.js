var tree = [
    {

        text: 'Parent 1',

        href: '#parent1',


        tags: ['4'],
        
        nodes: [

          {

            text: 'Child 1',

            href: '#child1',

            tags: ['2'],

            nodes: [

              {
                
                text: 'Grandchild 1',

                href: '#grandchild1',

                tags: ['0']

              },

              {

                text: 'Grandchild 2',

                href: '#grandchild2',

                tags: ['0']

              }

            ]

          },

          {

            text: 'Child 2',

            href: '#child2',

            tags: ['0']

          }

        ]

      },

      {

        text: 'Parent 2',

        href: '#parent2',

        tags: ['0']

      },

      {

        text: 'Parent 3',

        href: '#parent3',

         tags: ['0']

      },

      {

        text: 'Parent 4',

        href: '#parent4',

         tags: ['0']

      },

      {

        text: 'Parent 5',

        href: '#parent5',

         tags: ['0']

      },

  ];

function getTree() {
  // Some logic to retrieve, or generate tree structure
  return tree;
}

$(document).ready(
    $('#tree').treeview({
        data: getTree(),
        // backColor: "#FFFFFF",
        // color: "#428bca",
        // enableLinks: true,
        // collapseIcon: 'glyphicon glyphicon-flash', // 折叠图标，默认 min
        // expandIcon: 'glyphicon glyphicon-earphone', // 展开图标，默认 plus
        
    }),

    $('#tree').on('nodeSelected',function(event, data) { 
      // 事件代码... 
      if(data.state.expanded){ 
        //处于展开状态则折叠 
        $('#tree').treeview('collapseNode', data.nodeId); 
      } 
      else { 
        //展开 
        $('#tree').treeview('expandNode', data.nodeId); 
      } 
    }),
    
    // $('#tree').on('nodeUnselected',function(event, data) { 
    //   // 事件代码... 
    //   if(data.state.expanded){ 
    //     //处于展开状态则折叠 
    //     $('#tree').treeview('collapseNode', data.nodeId,); 
    //   } 
    //   else { 
    //     //展开 
    //     $('#tree').treeview('expandNode', data.nodeId); 
    //   } 
    // })

);

$(document).on('click','#adropindex',function(){
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

$(document).on('click','#adropaddblog',function(){
  $.ajax({
      // url: "http://localhost:5000/addblog",
      url: "./addblog",
      type: "GET",
      // contentType: 'application/json',
      // data:"{}",
      // dataType: "JSON",
      success:function(data){
          console.log(data)
          // window.location.href="http://localhost:5000/addblog";
          window.location.href="./addblog";
      },
      error:function(jqXHR, textStatus, errorThrown){
          console.log(errorThrown)
          alert("内容获取错误")
      }
    });
});

$(document).on('click','#navindex',function(){
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

$(document).on('click','#navaddblog',function(){
  $.ajax({
      // url: "http://localhost:5000/addblog",
      url: "./addblog",
      type: "GET",
      // contentType: 'application/json',
      // data:"{}",
      // dataType: "JSON",
      success:function(data){
          console.log(data)
          // window.location.href="http://localhost:5000/addblog";
          window.location.href="./addblog";
      },
      error:function(jqXHR, textStatus, errorThrown){
          console.log(errorThrown)
          alert("内容获取错误")
      }
    });
});

$(document).on('click','#navreg',function(){
  $.ajax({
      // url: "http://localhost:5000/addblog",
      url: "./reg",
      type: "GET",
      // contentType: 'application/json',
      // data:"{}",
      // dataType: "JSON",
      success:function(data){
          console.log(data)
          // window.location.href="http://localhost:5000/addblog";
          window.location.href="./reg";
      },
      error:function(jqXHR, textStatus, errorThrown){
          console.log(errorThrown)
          alert("内容获取错误")
      }
    });
});

$(document).on('click','#navlog',function(){
  $.ajax({
      // url: "http://localhost:5000/addblog",
      url: "./login",
      type: "GET",
      // contentType: 'application/json',
      // data:"{}",
      // dataType: "JSON",
      success:function(data){
          console.log(data)
          // window.location.href="http://localhost:5000/addblog";
          window.location.href="./login";
      },
      error:function(jqXHR, textStatus, errorThrown){
          console.log(errorThrown)
          alert("内容获取错误")
      }
    });
});