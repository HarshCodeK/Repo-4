import pytest
from megaproject.sandbox import Workspace,SandboxError
def test_read_inside(tmp_path):
    (tmp_path/"a.txt").write_text("hello"); assert Workspace(tmp_path).read("a.txt")=="hello"
def test_escape(tmp_path):
    with pytest.raises(SandboxError): Workspace(tmp_path).read("../secret")
def test_symlink_escape(tmp_path):
    outside=tmp_path.parent/"outside-x"; outside.write_text("secret"); (tmp_path/"link").symlink_to(outside)
    with pytest.raises(SandboxError): Workspace(tmp_path).read("link")
