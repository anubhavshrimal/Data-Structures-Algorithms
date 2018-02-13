"""
Implementation of Trie data structure.
"""


class Node:
    def __init__(self, value=None, isComplete=False):
        self.isComplete = isComplete
        self.children = {}
        self.value = value


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        """
        Add the given word into the trie
        :param word: A String (word) to be added in the trie
        """
        chars = list(word)

        curr_node = self.root

        for ch in chars:
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            else:
                new_node = Node(value=ch)
                curr_node.children[ch] = new_node
                curr_node = new_node

        curr_node.isComplete = True

    def search(self, word):
        """
        Searches if the word is present in the Trie or not
        :param word: String (word) to be searched in the trie
        :return: last Node of the searched word if present else None
        """
        chars = list(word)

        curr_node = self.root

        for ch in chars:
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            else:
                return None

        if curr_node.isComplete is True:
            return curr_node

        return None

    def delete(self, word):
        """
        Deletes the given String (word) from the trie
        :param word: Word (String) to be deleted
        :return: True is deleted, False if word not present in the Trie
        """
        chars = list(word)
        n = len(chars)

        curr_node = self.root
        last_complete_node = None
        child_of_last_complete = None

        for i, ch in enumerate(chars):
            if (curr_node.isComplete or len(curr_node.children.keys()) > 1) and i < n-1:
                last_complete_node = curr_node
                child_of_last_complete = ch
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            else:
                return False

        curr_node.isComplete = False
        if len(curr_node.children.keys()) > 0:
            last_complete_node = None

        if last_complete_node is not None:
            del last_complete_node.children[child_of_last_complete]

        return True


trie = Trie()
trie.add_word("anubhav")
trie.add_word("anubshrimal")
trie.add_word("anubhavshrimal")
trie.add_word("data_structures")

if trie.search("anubhav") is not None:
    print("anubhav is present in the Trie")
else:
    print("anubhav is NOT present in the Trie")

trie.delete("anubhav")

if trie.search("anubhav") is not None:
    print("anubhav is present in the Trie")
else:
    print("anubhav is NOT present in the Trie")
