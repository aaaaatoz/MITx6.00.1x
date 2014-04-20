# Paste your entire definition of the Family class in the following box.
class Family(object):
    def __init__(self, founder):
        self.names_to_nodes = {}
        self.root = Member(founder)
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:   
            # create Member node for a child   
            c_member = Member(c)   
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member
            # set child's parent
            c_member.add_parent(mom_node)
            # set the parent's child
            mom_node.add_child(c_member) 

    def is_parent(self, mother, kid):
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        a_node = self.names_to_nodes[a]
        b_node = self.names_to_nodes[b]
        temp_a = a_node
        temp_b = b_node
        #get the ancestor list
        a_ancestor = [a_node,]
        b_ancestor = [b_node,]
        if a_node == b_node:
            return (-1,0)
        while True:
            if temp_a:
                #build the ancestor list
                a_ancestor.append(temp_a.get_parent())
                temp_a = temp_a.get_parent()
                if temp_a in b_ancestor:
                    # main code here
                    cousintype = b_ancestor.index(temp_a) -1
                    degreesremoved = len(a_ancestor) - b_ancestor.index(temp_a) - 1
                    break

            if  temp_b:
                b_ancestor.append(temp_b.get_parent())
                temp_b = temp_b.get_parent()
                if temp_b in a_ancestor:
                    cousintype = a_ancestor.index(temp_b) -1
                    degreesremoved = len(b_ancestor) - a_ancestor.index(temp_b) - 1
                    break
        return (cousintype,degreesremoved)
