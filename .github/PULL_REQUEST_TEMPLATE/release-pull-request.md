<!-- Create a new Release issue before using this template -->

**Description**
<!-- Do not push the release tag until this PR is merged -->
This pull request updates redata-commons v0.xx.x -> v0.xx.0. Closes #<insert associated issue number>

<!-- You may create the pull request after editing the Title and Description above. -->
<!-- The remaining steps can be completed after PR creation -->
  
**Check**
- [ ] Title and description have been updated.
- [ ] Verified the correct branch is being merged by checking the text immediately below the PR title.

**Begin a new release**
:warning: Do not publish the release until this PR is merged :warning:
- [ ] Go to the [New Release](../releases/new) page
- [ ] In the `Choose a tag` dropdown, enter a new tag name corresponding to the new version. E.g., `v1.0.1`. Then click "Create new tag on publish"
- [ ] The `Target` should be the main or master branch.
- [ ] Click the `Generate release notes` button. Review the notes for accuracy
- [ ] Save the release as Draft.

**Update Documentation in the Branch**
- [ ] Copy the generated release notes from the previous step to the top of `CHANGELOG.md`
- [ ] Update `README.md` (if needed)
- [ ] Update ReadTheDocs documentation (if needed). If changes were made, [verify](https://app.readthedocs.org/projects/redata-commons/builds/) that ReadTheDocs successfully built the Documentation

**Release**
- [ ] Merge this PR
- [ ] Return to [Releases](../releases) and publish the draft release
- [ ] Verify that the version was successfully published to PyPi. This should happen automatically when the release is published
- [ ] Verify that [ReadTheDocs (latest)](https://redata-commons.readthedocs.io/en/latest/) reflects the updates made (if any)
