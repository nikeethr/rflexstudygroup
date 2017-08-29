import unittest
import encryption

class TestEncryption(unittest.TestCase):
    def test_empty_string(self):
        s = ''
        e = encryption.encrypted_str(s)
        a = ''
        self.assertEqual(e,a)

    def test_single_element_string(self):
        s = 'a'
        e = encryption.encrypted_str(s)
        a = 'a'
        self.assertEqual(e,a)

    def test_perfect_square(self):
        s = 'a cat walked under a ladder'
        e = encryption.encrypted_str(s)
        a = 'aauae clnlr akda teed wdrd'
        self.assertEqual(e,a)

    def test_irrational_square(self):
        s = 'a black cat walked under the ladder'
        e = encryption.encrypted_str(s)
        a = 'ackea baerd ltdtd awuhe caner kldl'
        self.assertEqual(e,a)

    def test_example(self):
        s = 'if man was meant to stay on the ground god would have given us roots'
        e = encryption.encrypted_str(s)
        a = 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau'
        self.assertEqual(e,a)

if __name__ == '__main__':
    unittest.main(exit=False)
