import java.io.*;
import java.util.*;

/*
Given a sorted (increasing order) array with unique integer elements, create a Binary Search Tree of _minimal_ height.

... and then print it :)

*/


public class TreeBuilder {
  
  public static class Node {

    Node left;
    Node right;
    int value;

    public Node(int value, Node left, Node right){
      this.value = value;
      this.right = right;
      this.left = left;
    }
  }

 
  public static class TreeUtils {
    
    public static Node buildTree(Integer[] nodeList, int start, int end){
      
     if (start == end){
         return new Node(nodeList[start], null, null);
     } else if (end - start == 1) {
         Node leftNode = new Node(nodeList[start], null, null);
         return new Node(nodeList[end], leftNode, null);
    
     }  else {
         // get root index
         int rootIndex = start + (end - start) / 2;  
         Integer rootValue = nodeList[rootIndex];
         Node leftNode = buildTree(nodeList,start,rootIndex -1);
         Node rightNode = buildTree(nodeList, rootIndex+ 1, end);
         return new Node(rootValue, leftNode, rightNode);
      }

    }
    
    
    public static void printTree(Node root) {
    
      Queue<Node> nodesToPrint = new LinkedList<Node>();   

      if (!(root == null)){
          nodesToPrint.add(root);
      }

     Queue<Node> childrenNodesToPrint = new LinkedList<Node>();

     while (true) {
        while (!nodesToPrint.isEmpty()){
            Node node = nodesToPrint.remove();
            System.out.print(node.value + " ");

            Node leftNode = node.left;
            if (!(leftNode == null)){
                 childrenNodesToPrint.add(leftNode);
            }

            Node rightNode = node.right;
            if (!(rightNode == null)){
                 childrenNodesToPrint.add(rightNode);
            }
         }

         System.out.println("");

       if (childrenNodesToPrint.isEmpty()){
         // No more nodes!
         break;

       } else {
         nodesToPrint.addAll(childrenNodesToPrint);
         childrenNodesToPrint.clear();

       }
      }
    }
  }
  
  
  public static void main(String[] args){
    Integer[] t1 = new Integer[7];
    t1[0] = 1;
    t1[1] = 3;
    t1[2] = 5;
    t1[3] = 7;
    t1[4] = 10;
    t1[5] = 14;
    t1[6] = 30;

    Node tree = TreeUtils.buildTree(t1, 0, t1.length -1);
    TreeUtils.printTree(tree);
  }


}


   
