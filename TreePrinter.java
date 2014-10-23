/**
 * Sample input:
 *
 *          1
 *         / \
 *        3   5
 *       /   / \
 *      2   4   7
 *     / \   \
 *    9   6   8
 
 *
 * Expected output:
 *    1
 *    3 5
 *    2 4 7
 *    9 6 8
 *    ==========
 */
class TreePrinter {
 
  static class Node {
    int value;
    Node left;
    Node right;
    public Node(int value, Node left, Node right) {
      this.value = value;
      this.left = left;
      this.right = right;
    }
  }
 
  public void printTree(Node root) {
    
    List<Node> nodesToPrint = new ArrayList<Node>();   
    if (!(root == null)){
        nodesToPrint.add(root);
    }
    printNodeList(nodesToPrint);
    
  }

   public void printNodeList(List<Node> nodesToPrint){
    
    List<Node> childrenNodesToPrint = new ArrayList<Node>();
    
    for (Node node : nodesToPrint){
        System.out.print(node.value + " ");
        
        Node leftNode = root.left;
        if (!(leftNode == null)){
             childrenNodesToPrint.add(leftNode);
        }
        
        Node rightNode = root.right;
        if (!(rightNode == null)){
             childrenNodesToPrint.add(rightNode);
        }
     }
     
     System.out.println("");
     printNodeList(childrenNodesToPrint);
        
   }
  
}
