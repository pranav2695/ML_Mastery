## Feature Importance
we calculate the feature importance with the help of the node importance, then we sum the node importance of same feature together divided Total sum of all the node importance.  
Now how to calculate the node importance there is a formual for that we use that to calculate the node importance. 

## Prepruning & Post prunning 
we have lot of overfitting in the decision tree so thats why we have these technique. 
overfitting happens because we dont have any stopping creteria. 
we can remove the overfitting by removing the unecessary nodes
this method halts the tree construction early. it can be done in various ways: by setting a limit on the maximum depth of a tree, setting a limit on the minimum number of instances that must be in a node to allow a split, or stopping when a split results in the improvement of the model accuracybelow a cetain threshold. 
## Different Method of pruning
- Maximum depth 
- Minimum number of samples 
- Minimum decrease in gini impurity 
- Number of leaf node 
- Min Number of sample in leaf nodes
- Maximum features 
## Post pruning    
This method allows the decision tree to fully grow then prune the tree based on the error complexity trade off. the basic idea is to replace a whole subtree by a leaf node, and assign the most common class in that subtree to the leaf node.
## Advantages of pre pruning 
- simplicity 
- computational efficiency 
- reduced overfitting 
- improved interpretability 
## Disadvantage 
- risk of underfitting 
- required fine tuning : every new data we need to do the fine tunning again.
- short sighedness - can prune good nodes if they come after a bad node 