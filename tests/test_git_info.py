from pathlib import Path

from redata.commons.git_info import GitInfo, no_git_str
from redata.commons.git_info import __file__ as gi_file


def test_GitInfo():
    # Test for local or GitHub Actions via checkout/clone
    gi = GitInfo(input_path=Path(gi_file).parent.parent.parent)

    assert isinstance(gi.branch, str)

    assert isinstance(gi.commit, str)
    assert isinstance(gi.short_commit, str)
    assert len(gi.short_commit) == 7

    # Check for packaged case
    gi = GitInfo(input_path=Path(gi_file))
    assert gi.branch == no_git_str

    assert gi.commit == no_git_str
    assert len(gi.short_commit) == 0
