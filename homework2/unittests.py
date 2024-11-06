import unittest
from unittest.mock import patch
from hw2 import generate_plantuml_code, get_commits

class TestDependencyVisualizer(unittest.TestCase):

    @patch('subprocess.run')
    def test_get_commits(self, mock_run):
        mock_run.return_value.stdout = "commit1\ncommit2\ncommit3"
        commits = get_commits('C:\\Users\\user\\Desktop\\OCW')
        self.assertEqual(commits, ['commit1', 'commit2', 'commit3'])

    def test_generate_plantuml_code(self):
        commits = ['commit1', 'commit2', 'commit3']
        expected_output = (
            "@startuml\n"
            "digraph G {\n"
            '  "commit1" -> "commit2"\n'
            '  "commit2" -> "commit3"\n'
            "}\n"
            "@enduml"
        )
        self.assertEqual(generate_plantuml_code(commits), expected_output)

if __name__ == '__main__':
    unittest.main()