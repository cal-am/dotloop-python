from typing import Callable, Optional, TypedDict, List


class Test(TypedDict):
    func: Callable[[], None]
    name: Optional[str]
    should_raise: Optional[bool]


def test_all(tests: List[Test]):
    error_count = 0
    fail_count = 0

    for test in tests:
        try:
            test['func']()
        except AssertionError as e:
            print(f'FAIL:\n\tName: {test.get("name", test["func"].__name__)}\n\tProblem: {e.__class__.__name__} -- {str(e)}\n')
            fail_count += 1
        except Exception as e:
            print(f'ERROR:\n\tName: {test.get("name", test["func"].__name__)}\n\tProblem: {e.__class__.__name__} -- {str(e)}\n')
            error_count += 1
            
    print(f'RESULTS:\n\tFails: {fail_count}\n\tErrors: {error_count}\n\tSuccesses: {len(tests) - error_count - fail_count}')



# Import tests
from . import test_authentication
from . import test_idioms


tests = []
tests.extend(test_authentication.tests)
tests.extend(test_idioms.tests)