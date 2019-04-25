var tree = [
    {

        text: 'Parent 1',

        href: '#parent1',


        tags: ['4'],
        
        state: { // 初始化的状态（支持 4 种）
            checked: true, // 是否可勾选
            disabled: false, // 是否可用
            expanded: true, // 是否可折叠
            selected: false // 是否可选中
        },

        nodes: [

          {

            text: 'Child 1',

            href: '#child1',

            tags: ['2'],

            state: { // 初始化的状态（支持 4 种）
                checked: true, // 是否可勾选
                disabled: false, // 是否可用
                expanded: true, // 是否可折叠
                selected: false // 是否可选中
            },

            nodes: [

              {
                state: { // 初始化的状态（支持 4 种）
                    checked: true, // 是否可勾选
                    disabled: false, // 是否可用
                    expanded: true, // 是否可折叠
                    selected: false // 是否可选中
                },

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

        href: '#parent5'  ,

        tags: ['0']

      }
  ];

  function getTree() {
    // Some logic to retrieve, or generate tree structure
    return tree;
  }

$(document).ready(
    $('#tree').treeview({
        data: getTree(),
        backColor: "#FFFFFF",
        color: "#428bca",
        enableLinks: true,
        collapseIcon: 'glyphicon glyphicon-flash', // 折叠图标，默认 min
        expandIcon: 'glyphicon glyphicon-earphone', // 展开图标，默认 plus
        
    }),
    
);