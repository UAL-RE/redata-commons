from pathlib import Path
from typing import Tuple

# Get git root
git_root = Path(__file__).parent.parent

no_git_str = '.git structure does not exist'


class GitInfo:
    """
    Provides ``git`` repo information

    :param input_path: Full path containing the ``.git`` contents

    :ivar input_path: Full path containing the ``.git`` contents
    :ivar head_path: Full path of the ``.git`` HEAD
    :ivar branch: Active branch name
    :ivar commit: Full hash
    :ivar short_commit: short hash commit
    """
    def __init__(self, input_path: str):
        self.input_path: str = input_path
        self.head_path: Path = Path(self.input_path) / ".git" / "HEAD"
        self.branch: str = self.get_active_branch_name()
        commit_tuple: tuple = self.get_latest_commit()
        self.commit: str = commit_tuple[0]
        self.short_commit: str = commit_tuple[1]

    def get_active_branch_name(self) -> str:
        """Retrieve active branch name"""
        if self.head_path.exists():
            with self.head_path.open("r") as f:
                content = f.read().splitlines()

            for line in content:
                if line[0:4] == "ref:":
                    return line.partition("refs/heads/")[2]
                else:
                    return f"HEAD detached : {content[0]}"
        else:
            return no_git_str

    def get_latest_commit(self) -> Tuple[str, str]:
        """Retrieve latest commit hash"""
        if self.head_path.exists():
            with self.head_path.open("r") as f:
                content = f.read().splitlines()

            for line in content:
                if line[0:4] == "ref:":
                    ref_path = Path(self.input_path) / ".git" / f"{line.partition(' ')[2]}"
                    with ref_path.open('r') as g:
                        commit = g.read().splitlines()
                else:
                    commit = content

            return commit[0], commit[0][:7]  # full and short hash
        else:
            return no_git_str, ''
