import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class TestHBNBCommand(unittest.TestCase):
    """this is the tests class for our console"""
    def setUp(self):
        self.console = HBNBCommand()

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('create')
            self.assertEqual(
                    '** class name missing **\n',
                    mock_out.getvalue()
                    )

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('create MyModel')
            self.assertEqual(
                    '** class doesn\'t exist **\n',
                    mock_out.getvalue()
                    )

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('create BaseModel')
            self.assertEqual('\n', mock_out.getvalue())
            self.assertIsInstance(
                    storage.all()["BaseModel." + mock_out.getvalue().strip()],
                    BaseModel
                    )

    def test_show(self):
        storage._FileStorage__objects = {}
        bm = BaseModel()
        bm.save()
        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('show')
            self.assertEqual('** class name missing **\n', mock_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('show MyModel')
            self.assertEqual(
                    '** class doesn\'t exist **\n',
                    mock_out.getvalue()
                    )

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('show BaseModel')
            self.assertEqual(
                    '** instance id missing **\n',
                    mock_out.getvalue()
                    )

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('show BaseModel {}'.format(bm.id))
            self.assertEqual(str(bm) + '\n', mock_out.getvalue())

    def test_destroy(self):
        storage._FileStorage__objects = {}
        bm = BaseModel()
        bm.save()
        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('destroy')
            self.assertEqual('** class name missing **\n', mock_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('destroy MyModel')
            self.assertEqual(
                    '** class doesn\'t exist **\n',
                    mock_out.getvalue()
                    )

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('destroy BaseModel')
            self.assertEqual(
                    '** instance id missing **\n',
                    mock_out.getvalue()
                    )

        with patch('sys.stdout', new=StringIO()) as mock_out:
            self.console.onecmd('destroy BaseModel {}'.format(bm.id))
            self.assertNotIn(bm, storage.all().values())


if __name__ == "__main__":
    unittest.main()
