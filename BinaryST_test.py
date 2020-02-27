from BinaryST import BST 
import unittest

class BSTTestCase(unittest.TestCase):

	def test_bstTest(self):
		bst=BST()

		#Test Case for add
		bst.add(10,"Value for A")
		
		self.assertEqual(bst.size_(),1) 		#Check for size. TRUE

		bst.add(5,"Value for B")
		self.assertEqual(bst.size_(),2)		#Check for size. TRUE

		bst.add(15,"Value for C")
		self.assertEqual(bst.size_(),3)		#Check for size. TRUE

		self.assertListEqual(bst.inorder(),[5,10,15])	

		bst.add(11,"Value for D")			#Add value to check Traversal
		bst.add(20,"Value for E")			#Add value to check Traversal


		self.assertListEqual(bst.inorder(),[5,10,11,15,20])

		self.assertListEqual(bst.postorder(),[5,11,20,15,10])

		self.assertListEqual(bst.preorder(),[10,5,15,11,20])

		self.assertListEqual(bst.LargestKey(),[20])
		self.assertListEqual(bst.SmallestKey(),[5])
		self.assertListEqual(bst.search(20),[1])
		

if __name__=="__main__":
	unittest.main()