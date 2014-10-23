/**

Implement a function to check if a binary tree is balanced. For the purpose of this question,  a balanced tree is desfined to be a tree such that the heights of the two subtree of any node never differ by more than one.

**/

public class BalanceTreeChecker{
  
  static class Node {
    int value;
    Node left;
    Node right;
    public Node(int value, Node left, Node right){
      this.value = value;
      this.left = left;
      this.right = right;
    }
  }

  public Boolean checkTree(Node root){
    
    if (root == null){
      return true;
    } else {

      Node left = root.left;
      Node right = root.right;
      
      if (Math.abs(depth(left) - depth(right)) > 1) {
        return false;
      } else {
        return checkTree(left) & checkTree(right);
      }
    }
  }
  
  private int depth(Node node){
    if (node == null){
      return 0;
    } else {
      return Math.max(depth(node.left), depth(node.right)) + 1;
    }
    
  }
  
  
  // Complexity : N*log(N)   [depth = log(N)]
  
 }
