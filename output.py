
#!/usr/bin/env python3

from typing import Any, List, Optional
from pydantic import BaseModel, Field


class MyClass21(BaseModel):
    href: str

class MyClass20(BaseModel):
    href: str

class MyClass19(BaseModel):
    href: str

class MyClass18(BaseModel):
    href: str

class MyClass17(BaseModel):
    href: str

class MyClass16(BaseModel):
    href: str

class MyClass15(BaseModel):
    href: str

class MyClass14(BaseModel):
    href: str

class MyClass13(BaseModel):
    self: MyClass14
    html: MyClass15
    issue: MyClass16
    comments: MyClass17
    review_comments: MyClass18
    review_comment: MyClass19
    commits: MyClass20
    statuses: MyClass21

class MyClass12(BaseModel):
    key: str
    name: str
    spdx_id: str
    url: str
    node_id: str

class MyClass11(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: int

class MyClass10(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    private: int
    owner: MyClass11
    html_url: str
    description: Optional[Any] = None  # TODO: This is an assumption for None/null
    fork: int
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: Optional[Any] = None  # TODO: This is an assumption for None/null
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    has_issues: int
    has_projects: int
    has_downloads: int
    has_wiki: int
    has_pages: int
    has_discussions: int
    forks_count: int
    mirror_url: Optional[Any] = None  # TODO: This is an assumption for None/null
    archived: int
    disabled: int
    open_issues_count: int
    license: MyClass12
    allow_forking: int
    is_template: int
    web_commit_signoff_required: int
    topics: List[Any] = Field(default_factory=list)  # TODO: This is an assumption for empty lists
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str

class MyClass9(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: int

class MyClass8(BaseModel):
    label: str
    ref: str
    sha: str
    user: MyClass9
    repo: MyClass10

class MyClass7(BaseModel):
    key: str
    name: str
    spdx_id: str
    url: str
    node_id: str

class MyClass6(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: int

class MyClass5(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    private: int
    owner: MyClass6
    html_url: str
    description: Optional[Any] = None  # TODO: This is an assumption for None/null
    fork: int
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: Optional[Any] = None  # TODO: This is an assumption for None/null
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    has_issues: int
    has_projects: int
    has_downloads: int
    has_wiki: int
    has_pages: int
    has_discussions: int
    forks_count: int
    mirror_url: Optional[Any] = None  # TODO: This is an assumption for None/null
    archived: int
    disabled: int
    open_issues_count: int
    license: MyClass7
    allow_forking: int
    is_template: int
    web_commit_signoff_required: int
    topics: List[Any] = Field(default_factory=list)  # TODO: This is an assumption for empty lists
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str

class MyClass4(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: int

class MyClass3(BaseModel):
    label: str
    ref: str
    sha: str
    user: MyClass4
    repo: MyClass5

class MyClass2(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    user_view_type: str
    site_admin: int

class MyClass1(BaseModel):
    url: str
    id: int
    node_id: str
    html_url: str
    diff_url: str
    patch_url: str
    issue_url: str
    number: int
    state: str
    locked: int
    title: str
    user: MyClass2
    body: str
    created_at: str
    updated_at: str
    closed_at: Optional[Any] = None  # TODO: This is an assumption for None/null
    merged_at: Optional[Any] = None  # TODO: This is an assumption for None/null
    merge_commit_sha: Optional[Any] = None  # TODO: This is an assumption for None/null
    assignee: Optional[Any] = None  # TODO: This is an assumption for None/null
    assignees: List[Any] = Field(default_factory=list)  # TODO: This is an assumption for empty lists
    requested_reviewers: List[Any] = Field(default_factory=list)  # TODO: This is an assumption for empty lists
    requested_teams: List[Any] = Field(default_factory=list)  # TODO: This is an assumption for empty lists
    labels: List[Any] = Field(default_factory=list)  # TODO: This is an assumption for empty lists
    milestone: Optional[Any] = None  # TODO: This is an assumption for None/null
    draft: int
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    head: MyClass3
    base: MyClass8
    _links: MyClass13
    author_association: str
    auto_merge: Optional[Any] = None  # TODO: This is an assumption for None/null
    active_lock_reason: Optional[Any] = None  # TODO: This is an assumption for None/null
    merged: int
    mergeable: Optional[Any] = None  # TODO: This is an assumption for None/null
    rebaseable: Optional[Any] = None  # TODO: This is an assumption for None/null
    mergeable_state: str
    merged_by: Optional[Any] = None  # TODO: This is an assumption for None/null
    comments: int
    review_comments: int
    maintainer_can_modify: int
    commits: int
    additions: int
    deletions: int
    changed_files: int



def parse_test():
    import json
    # import yaml # UNCOMMENT FOR USE WITH YAML
    with open("input.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        # data = yaml.safe_load(f) # UNCOMMENT FOR USE WITH YAML AND COMMENT ABOVE LINE
    assert isinstance(data, dict)
    my_class_1 = MyClass1.model_validate(data)
    print("my_class_1")
    print(my_class_1)

if __name__ == "__main__":
    parse_test()
