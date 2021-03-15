from pathlib import Path

# Get git root
git_root = Path(__file__).parent.parent

no_git_str = '.git structure does not exist'


class GitInfo:
    """
    Provides git repo information

    :param input_path: Full path containing the .git contents
    """
    def __init__(self, input_path: str = git_root):
        self.input_path = input_path
        self.head_path = Path(self.input_path) / ".git" / "HEAD"
        self.branch = self.get_active_branch_name()
        commit_tuple = self.get_latest_commit()
        self.commit = commit_tuple[0]
        self.short_commit = commit_tuple[1]

    def get_active_branch_name(self):
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

    def get_latest_commit(self):
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
