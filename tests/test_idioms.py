from dotloop.document import Document, Documents
from dotloop.task import Task, Tasks
from dotloop.task_list import TaskList, TaskLists
from dotloop.participant import Participant, Participants
from dotloop.folder import Folder, Folders
from dotloop.detail import Details
from dotloop.activity import Activities
from dotloop.contact import Contact, Contacts
from dotloop.account import Account
from dotloop.loop_template import LoopTemplate, LoopTemplates
from dotloop.profile import Profiles
from dotloop.loop import Loop, Loops
from dotloop import Profile
from . import Test


def test_profile():
    p = Profile(123)
    assert isinstance(p, Profile)
    # create tests for expected methods (get, post, patch, delete)

def test_profiles():
    ps = Profiles()
    assert isinstance(ps, Profiles)

def test_loop():
    l = Profile(123).loop(123)
    assert isinstance(l, Loop)

def test_loops():
    ls = Profile(123).loops
    assert isinstance(ls, Loops)

def test_loop_template():
    lt = Profile(123).loop_template(123)
    assert isinstance(lt, LoopTemplate)

def test_loop_templates():
    lts = Profile(123).loop_templates
    assert isinstance(lts, LoopTemplates)

def test_account():
    a = Account()
    assert isinstance(a, Account)

def test_contact():
    c = Contact(123)
    assert isinstance(c, Contact)

def test_contacts():
    c = Contacts()
    assert isinstance(c, Contacts)

def test_loop_activities():
    as_ = Profile(123).loop(123).activities
    assert isinstance(as_, Activities)

def test_loop_details():
    ds = Profile(123).loop(123).details
    assert isinstance(ds, Details)

def test_loop_folder():
    f = Profile(123).loop(123).folder(123)
    assert isinstance(f, Folder)

def test_loop_folders():
    fs = Profile(123).loop(123).folders
    assert isinstance(fs, Folders)

def test_loop_participant():
    p = Profile(123).loop(123).participant(123)
    assert isinstance(p, Participant)

def test_loop_participants():
    ps = Profile(123).loop(123).participants
    assert isinstance(ps, Participants)

def test_loop_task_list():
    tl = Profile(123).loop(123).task_list(123)
    assert isinstance(tl, TaskList)

def test_loop_task_lists():
    tls = Profile(123).loop(123).task_lists
    assert isinstance(tls, TaskLists)

def test_loop_task():
    t = Profile(123).loop(123).task_list(123).task(123)
    assert isinstance(t, Task)

def test_loop_tasks():
    ts = Profile(123).loop(123).task_list(123).tasks
    assert isinstance(ts, Tasks)

def test_loop_document():
    d = Profile(123).loop(123).folder(123).document(123)
    assert isinstance(d, Document)

def test_loop_documents():
    ds = Profile(123).loop(123).folder(123).documents
    assert isinstance(ds, Documents)


tests = [
    Test(func=func)
    for name, func in locals().items()
    if name.startswith('test_')
    and callable(func)
]