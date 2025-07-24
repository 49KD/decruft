from pytest import fixture
from .decruft import read_recursively


@fixture
def project_dir():
    return "./exmaple_dir"


def test_recursive_read(project_dir):
    expected_import_set = {
        "os",
        "sys",
        "numpy",
        "collections",
        "mypackage",
        "external_lib",
        "json",
    }
    found_imports = read_recursively(project_dir)
    assert found_imports == expected_import_set
