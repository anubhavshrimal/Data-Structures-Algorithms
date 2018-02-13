"""
Implementation of Trie data structure.
"""


class Node:
    def __init__(self, value=None, isComplete=False):
        self.isComplete = isComplete
        self.children = {}
        self.value = value
        self.isPrefixOf = 0


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
            # The substring till this node will now become a prefix of newly added word
            curr_node.isPrefixOf += 1

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

        val = self._delete(self.root, word)
        return True if val == 1 or val == 0 else False

    def _delete(self, node, chars):
        """
        Recursive Helper function to delete the word and decreement the isPrefix of values
        :param node: current node looking at
        :param chars: array of characters to look for
        :return: 1 is word is deleted, 0 if word is deleted and
        """

        # if the chars array is empty
        if len(chars) == 0:
            # check if the word is present in the trie
            if node.isComplete:
                node.isComplete = False

                # check if the word was a prefix of any other words in trie
                # if so, decrement isPrefixOf and return 0, as no deletions are required
                if len(node.children.keys()) > 0:
                    node.isPrefixOf -= 1
                    return 0

                # if word was not a prefix then we need to go up in the trie
                # and find the lowest parent which forms a new word in trie
                return 1
            # if word is not present in the trie
            return -1

        # check if the character is present in current node's children
        if chars[0] in node.children:
            # recursive call for remaining characters in the respective child
            val = self._delete(node.children[chars[0]], chars[1:])

            # if word was found but lowest parent which forms new word is not found
            if val == 1:
                if node.isComplete or len(node.children.keys()) > 1:
                    del node.children[chars[0]]
                    node.isPrefixOf -= 1
                    val = 0
            # if word was found and lowest parent which forms new word was also found
            # simply reduce the isPrefixOf value of the node
            elif val == 0:
                node.isPrefixOf -= 1
            return val

        return -1


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

print("Number of words in trie:", trie.root.isPrefixOf)
