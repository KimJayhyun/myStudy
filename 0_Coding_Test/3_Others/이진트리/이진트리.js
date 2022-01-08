class Node
{
    constructor(data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

function makingTree(arr, root, i)
{
    if (i < arr.length)
    {
        root = new Node(arr[i]);
        root.left = makingTree(arr, root.left, 2*i + 1);
        root.right = makingTree(arr, root.right, 2*i + 2);
    }
    
    return root;
}

let arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
let root;

let tree = makingTree(arr, root, 0)
console.log(tree.left.data)